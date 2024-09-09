from time import time
from poe_profit_calc.items import Item, PoeNinjaSource
from poe_profit_calc.fetcher import Fetcher, FetchError
from poe_profit_calc.sourcemappings import ENDPOINT_MAPPING
from itertools import groupby


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
        # TODO: check if res[item] actually exists. It doesn't if the item is not in the response.
        self.item_prices.update({item: {"price": res[item], "time": t} for item in items_to_fetch})
        return {item: self.item_prices[item]["price"] for item in items}


def fetch_prices(
    items: set[Item], fetcher: Fetcher, source_mapping=ENDPOINT_MAPPING
) -> dict[Item, float]:
    groups = group_by_source(items, source_mapping)
    item_prices = {}

    for data_source, item_group in groups.items():
        try:
            data = fetcher.fetch_data(data_source)
        except FetchError as e:
            print(e)
            data = {}
        item_prices.update(extract_prices(data, item_group))
    return item_prices


def group_by_source(
    items: set[Item], source_mapping: dict[PoeNinjaSource, str]
) -> dict[str, set[Item]]:
    groups = {}
    for item in items:
        source = source_mapping[item.matcher.source]
        if source not in groups:
            groups[source] = {item}
        else:
            groups[source].add(item)
    return groups


def extract_prices(data, items: set[Item]) -> dict[Item, float]:
    item_prices = {}
    unprocessed_items = items.copy()
    for item_data in data.get("lines", {}):
        if len(item_prices) == len(items):
            break
        for item in unprocessed_items:
            if price := item.matcher.price_if_match(item_data):
                item_prices[item] = price
                unprocessed_items.remove(item)
                break
    return item_prices
