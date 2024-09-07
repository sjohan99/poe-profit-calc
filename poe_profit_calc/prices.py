import requests
from cachetools import TTLCache, cached
from poe_profit_calc.items import Item, PoeNinjaSource

BASE_NINJA_URL = "https://poe.ninja/api/data/"
LEAGUE = "Settlers"

ENDPOINT_MAPPING = {
    PoeNinjaSource.CURRENCY: f"{BASE_NINJA_URL}currencyoverview?league={LEAGUE}&type=Currency",
    PoeNinjaSource.UNIQUE_ARMOUR: f"{BASE_NINJA_URL}itemoverview?league={LEAGUE}&type=UniqueArmour",
    PoeNinjaSource.UNIQUE_JEWEL: f"{BASE_NINJA_URL}itemoverview?league={LEAGUE}&type=UniqueJewel",
}


def fetch_prices(items: set[Item]):
    item_endpoints = {item: ENDPOINT_MAPPING[item.source] for item in items}
    item_data = {}
    for item, endpoint in item_endpoints.items():
        data = fetch_data(endpoint)
        item_data[item] = data
    item_prices = {}
    for item, data in item_data.items():
        process_function = PROCESSOR_MAPPING[item.source]
        item_prices.update(process_function(data, items))
    return item_prices


@cached(cache=TTLCache(maxsize=8196, ttl=1800))
def fetch_data(endpoint: str):
    print(f"Fetching data from {endpoint}")
    response = requests.get(endpoint)
    if response.status_code != 200:
        print(f"Failed to fetch data from {endpoint}")
        return {}
    return response.json()


def process_currencyoverview(data, items: set[Item]):
    item_prices = {}
    for currency in data.get("lines", {}):
        if len(item_prices) == len(items):
            break
        for item in items:
            if item.name == currency.get("currencyTypeName", ""):
                price = currency.get("chaosEquivalent", -1)
                item_prices[item] = price
    return item_prices


def process_itemoverview(data, items: set[Item]):
    item_prices = {}
    for item_data in data.get("lines", {}):
        if len(item_prices) == len(items):
            break
        for item in items:
            if item.name == item_data.get("name", "") and "-relic" not in item_data.get(
                "detailsId", ""
            ):
                price = item_data.get("chaosValue", -1)
                item_prices[item] = price
    return item_prices


PROCESSOR_MAPPING = {
    PoeNinjaSource.CURRENCY: process_currencyoverview,
    PoeNinjaSource.UNIQUE_ARMOUR: process_itemoverview,
    PoeNinjaSource.UNIQUE_JEWEL: process_itemoverview,
}
