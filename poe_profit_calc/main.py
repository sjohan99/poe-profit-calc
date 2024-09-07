from poe_profit_calc.prices import fetch_prices
from poe_profit_calc.items import EldritchChaosOrb, DissolutionOfTheFlesh

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_route():
    pretty_prices = {}
    item_prices = fetch_prices({EldritchChaosOrb, DissolutionOfTheFlesh})
    for item, price in item_prices.items():
        pretty_prices[item.name] = round(price)
    return pretty_prices
