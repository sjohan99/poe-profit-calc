from time import time
from poe_profit_calc.items import Item, PoeNinjaSource
from poe_profit_calc.fetcher import Fetcher, FetchError
from poe_profit_calc.sourcemappings import ENDPOINT_MAPPING


class Prices:
    def __init__(
        self,
        fetcher: Fetcher,
        source_mapping: dict[PoeNinjaSource, str] = ENDPOINT_MAPPING,
        cache_time_seconds=1800,
    ):
        self.fetcher = fetcher
        self.source_mapping = source_mapping
        self.cache_time_seconds = cache_time_seconds
        self.item_prices = {}

    def get_prices(self, items: set[Item]) -> dict[Item, float]:
        t = time()
        items_to_fetch = set()
        for item in items:
            if item not in self.item_prices:
                items_to_fetch.add(item)
            elif abs(self.item_prices[item].get("time") - t) > self.cache_time_seconds:
                items_to_fetch.add(item)
        res = fetch_prices(items_to_fetch, self.fetcher, self.source_mapping)
        self.item_prices.update({item: {"price": res[item], "time": t} for item in items_to_fetch})
        return {item: self.item_prices[item]["price"] for item in items}


def fetch_prices(
    items: set[Item], fetcher: Fetcher, source_mapping=ENDPOINT_MAPPING
) -> dict[Item, float]:
    item_sources = {item: source_mapping[item.source] for item in items}
    item_data = {}
    for item, item_source in item_sources.items():
        try:
            data = fetcher.fetch_data(item_source)
        except FetchError as e:
            print(e)
            data = {}
        item_data[item] = data
    item_prices = {}
    for item, data in item_data.items():
        process_function = PROCESSOR_MAPPING[item.source]
        item_prices.update(process_function(data, items))
    return item_prices


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
    PoeNinjaSource.INVITATION: process_itemoverview,
    PoeNinjaSource.FRAGMENT: process_currencyoverview,
    PoeNinjaSource.UNIQUE_ACCESSORY: process_itemoverview,
    PoeNinjaSource.UNIQUE_FLASK: process_itemoverview,
    PoeNinjaSource.UNIQUE_WEAPON: process_itemoverview,
}
