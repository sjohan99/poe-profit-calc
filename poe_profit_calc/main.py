from poe_profit_calc.fetcher import FileFetcher, HttpFetcher
from poe_profit_calc.prices import Prices, fetch_prices
from poe_profit_calc.items import Item
from poe_profit_calc.bosses import *
from poe_profit_calc.sourcemappings import FILE_PATH_MAPPING
from fastapi import FastAPI
import os


if os.getenv("POE_RUN_MODE") == "local":
    prices = Prices(fetcher=FileFetcher(), source_mapping=FILE_PATH_MAPPING)
else:
    prices = Prices(
        fetcher=HttpFetcher(),
    )

BOSSES = {
    "the_searing_exarch": TheSearingExarch,
    "the_shaper": TheShaper,
    "the_shaper_uber": TheShaperUber,
    "the_elder": TheElder,
    "the_elder_uber": TheElderUber,
}


def format_drop_prices(item_prices: dict[Item, float], drop_items: set[Item]):
    return [
        {
            "name": item.name,
            "price": item_prices.get(item, 0),
            "droprate": item.droprate,
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
    item_prices = prices.get_prices(items)
    return {
        "boss": boss_data.name,
        "drops": format_drop_prices(item_prices, boss_data.drops),
        "entrance_items": format_entrance_prices(item_prices, boss_data.entrance_items),
    }


app = FastAPI()


@app.get("/")
async def main_route():
    return "Hello, world!"


@app.get("/data/{boss}")
def get_boss_data(boss: str):
    return get_boss_drops(boss)
