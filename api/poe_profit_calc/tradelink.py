import json
from urllib.parse import quote
from poe_profit_calc.globals import TRADE_URL
from collections import defaultdict


def create_trade_link(
    name: str,
    type: str,
    identified: bool | None = None,
    min_ilvl: int | None = None,
    max_ilvl: int | None = None,
):
    base_query = defaultdict(dict)
    base_query.update(
        {
            "query": {
                "status": {"option": "online"},
                "name": name,
                "type": type,
                "stats": [{"type": "and", "filters": []}],
                "filters": {
                    "misc_filters": {"filters": build_filters(identified, min_ilvl, max_ilvl)}
                },
            },
            "sort": {"price": "asc"},
        }
    )
    encoded_query = quote(json.dumps(base_query))
    return f"{TRADE_URL}?q={encoded_query}"


def build_filters(
    identified: bool | None = None, min_ilvl: int | None = None, max_ilvl: int | None = None
):
    filters = defaultdict(dict)
    if identified is not None:
        filters["identified"].update({"option": "true" if identified else "false"})
    if min_ilvl is not None:
        filters["ilvl"].update({"min": min_ilvl})
    if max_ilvl is not None:
        filters["ilvl"].update({"max": max_ilvl})
    return filters
