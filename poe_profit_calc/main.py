from cachetools import cached, TTLCache
from poe_profit_calc.fetcher import FileFetcher, HttpFetcher
from poe_profit_calc.prices import Prices, fetch_prices
from poe_profit_calc.items import Item
from poe_profit_calc.bosses import *
from poe_profit_calc.sourcemappings import FILE_PATH_MAPPING
from fastapi import FastAPI
import os


if os.getenv("POE_RUN_MODE") == "local":
    price_fetcher = Prices(fetcher=FileFetcher(), source_mapping=FILE_PATH_MAPPING)
else:
    prices_fetcher = Prices(
        fetcher=HttpFetcher(),
    )

BOSSES = {
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
        prices = price_fetcher.get_prices(boss.drops.union(set(boss.entrance_items)))
        value = 0
        awakened_gems = [item for item in boss.drops if "Awakened" in item.name]
        other_items = [item for item in boss.drops if "Awakened" not in item.name]
        if awakened_gems:
            value += sum(prices.get(item, 0) * item.droprate for item in awakened_gems) / len(
                awakened_gems
            )
        value += sum(prices.get(item, 0) * item.droprate for item in other_items)
        value -= sum(
            prices.get(item, 0) * quantity for item, quantity in boss.entrance_items.items()
        )
        summaries.append({"boss_name": boss.name, "value": value})
    summaries.sort(key=lambda x: x["value"], reverse=True)
    return {"bosses": summaries}


def format_drop_prices(item_prices: dict[Item, float], drop_items: set[Item]):
    n_awakened_gems = len([item for item in drop_items if "Awakened" in item.name])
    return [
        {
            "name": item.name,
            "price": item_prices.get(item, 0),
            "droprate": (
                item.droprate / n_awakened_gems if "Awakened" in item.name else item.droprate
            ),
            "reliable": item.reliable,
            "trade_link": item.trade_link,
        }
        for item in drop_items
    ]


def format_entrance_prices(item_prices: dict[Item, float], entrance_items: dict[Item, int]):
    return [
        {
            "name": item.name,
            "price": item_prices.get(item, 0),
            "quantity": quantity,
        }
        for item, quantity in entrance_items.items()
    ]


def get_boss_drops(boss: str):
    boss_data = BOSSES.get(boss, None)
    items = boss_data.drops.union(set(boss_data.entrance_items))
    item_prices = price_fetcher.get_prices(items)
    return {
        "boss": boss_data.name,
        "drops": format_drop_prices(item_prices, boss_data.drops),
        "entrance_items": format_entrance_prices(item_prices, boss_data.entrance_items),
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
