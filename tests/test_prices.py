import json
import pathlib
import pytest
from poe_profit_calc.prices import process_currencyoverview, process_itemoverview
from poe_profit_calc.items import EldritchChaosOrb, EldritchExaltedOrb, Dawnbreaker, Dawnstrider


class TestParseQuestions:
    @pytest.fixture(scope="session")
    def currency_data(self):
        file = pathlib.Path("tests/poe_ninja_data/currencyoverview_currency.json")
        with open(file, "r") as f:
            return json.loads(f.read())

    @pytest.fixture(scope="session")
    def uniquearmour_data(self):
        file = pathlib.Path("tests/poe_ninja_data/itemoverview_uniquearmour.json")
        with open(file, "r") as f:
            return json.loads(f.read())

    def test_process_currencyoverview(self, currency_data):
        items = {EldritchChaosOrb, EldritchExaltedOrb}
        parsed_data = process_currencyoverview(currency_data, items)
        assert parsed_data == {
            EldritchChaosOrb: 47.56,
            EldritchExaltedOrb: 10,
        }

    def test_process_itemoverview(self, uniquearmour_data):
        items = {Dawnbreaker, Dawnstrider}
        parsed_data = process_itemoverview(uniquearmour_data, items)
        assert parsed_data == {
            Dawnbreaker: 5,
            Dawnstrider: 2,
        }
