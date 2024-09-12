import logging
import sys
import time
from cachetools import cached, TTLCache
from poe_profit_calc.fetcher import FileFetcher, HttpFetcher
from poe_profit_calc.logger import LoggingFormatter
from poe_profit_calc.prices import Prices
from poe_profit_calc.items import Item
from poe_profit_calc.bosses import *
from poe_profit_calc.sourcemappings import FILE_PATH_MAPPING
from poe_profit_calc.gemlevelling.gems import GemProfit, create_profitability_report, parse
from fastapi import FastAPI, HTTPException
import os


def initialize_logging():
    logFormatter = LoggingFormatter()
    logging_handlers = [
        logging.StreamHandler(sys.stdout),
    ]
    for handler in logging_handlers:
        handler.setFormatter(logFormatter)
    logging.basicConfig(level=logging.INFO, handlers=logging_handlers)


initialize_logging()


if os.getenv("POE_RUN_MODE") == "local":
    price_fetcher = Prices(fetcher=FileFetcher(), source_mapping=FILE_PATH_MAPPING)
    logging.info("Running in local mode")
else:
    price_fetcher = Prices(
        fetcher=HttpFetcher(),
    )
    logging.info("Running in production mode")

BOSSES: dict[str, Boss] = {
    "the_searing_exarch": TheSearingExarch,
    "the_searing_exarch_uber": TheSearingExarchUber,
    "the_eater_of_worlds": TheEaterOfWorlds,
    "the_eater_of_worlds_uber": TheEaterOfWorldsUber,
    "the_shaper": TheShaper,
    "the_shaper_uber": TheShaperUber,
    "the_elder": TheElder,
    "the_elder_uber": TheElderUber,
    "the_elder_uber_uber": TheElderUberUber,
    "sirus": Sirus,
    "sirus_uber": SirusUber,
    "the_maven": TheMaven,
    "the_maven_uber": TheMavenUber,
    "venarius": Venarius,
    "venarius_uber": VenariusUber,
}


@cached(cache=TTLCache(maxsize=128, ttl=3600))
def summary():
    summaries = []
    for boss in BOSSES.values():
        price_fetcher.price_items(boss.drops.union(set(boss.entrance_items)))
        value = 0
        value += sum(item.price * item.droprate for item in boss.drops)
        value -= sum(item.price * quantity for item, quantity in boss.entrance_items.items())
        summaries.append(
            {
                "boss_name": boss.name,
                "value": value,
                "reliable": all(
                    item.reliable for item in boss.drops.union(set(boss.entrance_items))
                ),
                "img": boss.get_img(),
            }
        )
    summaries.sort(key=lambda x: x["value"], reverse=True)
    return {"bosses": summaries}


def format_drop_prices(items: set[Item]):
    return [
        {
            "name": item.name,
            "price": item.price,
            "droprate": item.droprate,
            "reliable": item.reliable,
            "trade_link": item.trade_link,
            "img": item.img,
        }
        for item in items
    ]


def format_entrance_prices(entrance_items: dict[Item, int]):
    return [
        {
            "name": item.name,
            "price": item.price,
            "quantity": quantity,
            "img": item.img,
        }
        for item, quantity in entrance_items.items()
    ]


def get_boss_drops(boss: str):
    boss_data = BOSSES.get(boss, None)
    if not boss_data:
        logging.info(f"User requested non-existing boss: {boss}")
        raise HTTPException(status_code=404, detail="Boss not found")
    items = boss_data.drops.union(set(boss_data.entrance_items))
    item_prices = price_fetcher.price_items(items)
    return {
        "boss": boss_data.name,
        "drops": format_drop_prices(boss_data.drops),
        "entrance_items": format_entrance_prices(boss_data.entrance_items),
    }


app = FastAPI()


@app.get("/")
async def main_route():
    return "Hello, world!"


@app.get("/data/boss/{boss}")
def get_boss_data(boss: str):
    return get_boss_drops(boss)


@app.get("/data/summary")
def get_summary():
    return summary()


@app.get("/data/gems/summary")
def get_gem_summary():
    raw_data = price_fetcher.get_raw_endpoint(PoeNinjaSource.SKILL_GEM)
    parsed_data = parse(raw_data)
    pr = create_profitability_report(parsed_data)
    response = {
        "gems": [
            {
                "name": k,
                "level_profit": v.level_profit,
                "level_c_profit": v.level_c_profit,
                "level_q_c_profit": v.level_q_c_profit,
                "xp_adjusted_level_profit": v.xp_adjusted_level_profit,
                "xp_adjusted_c_profit": v.xp_adjusted_c_profit,
                "xp_adjusted_q_c_profit": v.xp_adjusted_q_c_profit,
                "vaal_orb_profit": v.vaal_orb_profit,
                "vaal_orb_20q_profit": v.vaal_orb_20q_profit,
                "vaal_level_profit": v.vaal_level_profit,
            }
            for k, v in pr.items()
        ]
    }
    response["gems"].sort(key=lambda x: x["level_profit"], reverse=True)
    return response
