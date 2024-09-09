import json
import pathlib
import pytest
from poe_profit_calc.prices import extract_prices, group_by_source
from poe_profit_calc.items import *


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

    @pytest.fixture(scope="session")
    def gem_data(self):
        file = pathlib.Path("tests/poe_ninja_data/itemoverview_skillgem.json")
        with open(file, "r") as f:
            return json.loads(f.read())

    def test_process_currency(self, currency_data):
        items = {EldritchChaosOrb, EldritchExaltedOrb}
        parsed_data = extract_prices(currency_data, items)
        assert parsed_data == {
            EldritchChaosOrb: 47.56,
            EldritchExaltedOrb: 10,
        }

    def test_process_armour(self, uniquearmour_data):
        items = {Dawnbreaker, Dawnstrider}
        parsed_data = extract_prices(uniquearmour_data, items)
        assert parsed_data == {
            Dawnbreaker: 5,
            Dawnstrider: 2,
        }

    def test_process_gem(self, gem_data):
        items = {AwakenedAddedChaosDamageSupport, AwakenedEnlightenSupport}
        parsed_data = extract_prices(gem_data, items)
        assert parsed_data == {
            AwakenedAddedChaosDamageSupport: 15,
            AwakenedEnlightenSupport: 51476.74,
        }

    def test_group_by_source(self):
        items = {
            AwakenedAddedChaosDamageSupport,
            AwakenedEnlightenSupport,
            EldritchExaltedOrb,
            Dawnbreaker,
            EldritchChaosOrb,
        }
        source_mapping = {
            PoeNinjaSource.CURRENCY: "1",
            PoeNinjaSource.UNIQUE_ARMOUR: "2",
            PoeNinjaSource.SKILL_GEM: "3",
        }
        grouped = group_by_source(items, source_mapping)
        assert grouped == {
            "1": {EldritchExaltedOrb, EldritchChaosOrb},
            "2": {Dawnbreaker},
            "3": {AwakenedAddedChaosDamageSupport, AwakenedEnlightenSupport},
        }
