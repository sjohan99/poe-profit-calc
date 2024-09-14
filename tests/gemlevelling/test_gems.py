import pathlib
import pytest
from poe_profit_calc.gemlevelling.gems import (
    GemProfit,
    calculate_profitability,
    omit_double_corrupted_and_ignored_gems,
    parse,
    Gem,
    group_gems,
    GemType,
)
from tests.test_utils import approx


class TestParseQuestions:
    @pytest.fixture(scope="session")
    def gem_data(self) -> bytes:
        file = pathlib.Path(pathlib.Path(__file__).parent, "data/itemoverview_skillgem.json")
        with open(file, "rb") as f:
            return f.read()

    @pytest.fixture
    def gems(self) -> set[Gem]:
        return {
            Gem("Enlighten Support", 2290.4, 4, 0, True, type=GemType.EXCEPTIONAL),
            Gem("Enlighten Support", 400.0, 3, 0, False, type=GemType.EXCEPTIONAL),
            Gem("Volatility Support", 88808.09, 21, 23, True),
            Gem("Double Strike", 0.96, 20, 0, True),
        }

    @pytest.fixture
    def vaal_gem_set(self) -> set[Gem]:
        return {
            Gem("Grace", 3, 1, 0, False),
            Gem("Grace", 10, 20, 0, False),
            Gem("Grace", 9, 1, 20, False),
            Gem("Grace", 34, 20, 20, False),
            Gem("Grace", 5, 20, 0, True),
            Gem("Grace", 24, 20, 20, True),
            Gem("Grace", 40, 21, 0, True),
            Gem("Grace", 123, 21, 20, True),
            Gem("Grace", 30, 20, 23, True),
            Gem("Vaal Grace", 6, 1, 0, True),
            Gem("Vaal Grace", 8, 20, 0, True),
            Gem("Vaal Grace", 26, 20, 20, True),
        }

    def test_parse(self, gem_data, gems):
        parsed_gems = parse(gem_data)
        assert {gem.name for gem in parsed_gems} == {gem.name for gem in gems}

    def test_group_gems_places_different_in_different_groups(self, gems):
        grouped_gems = group_gems(gems)
        assert grouped_gems == {
            "Enlighten Support": {
                Gem(
                    "Enlighten Support",
                    2290.4,
                    4,
                    0,
                    True,
                ),
                Gem(
                    "Enlighten Support",
                    400,
                    3,
                    0,
                    False,
                ),
            },
            "Volatility Support": {Gem("Volatility Support", 88808.09, 21, 23, True)},
            "Double Strike": {Gem("Double Strike", 0.96, 20, 0, True)},
        }

    def test_group_gems_does_not_remove_vaal_gems(self, vaal_gem_set):
        grouped_gems = group_gems(vaal_gem_set)
        assert grouped_gems == {"Grace": vaal_gem_set}

    def test_omit_double_corrupted_gems(self, gems):
        non_double_corrupted_gems = omit_double_corrupted_and_ignored_gems(gems)
        assert non_double_corrupted_gems == {
            Gem(
                "Enlighten Support",
                2290.4,
                4,
                0,
                True,
            ),
            Gem(
                "Enlighten Support",
                400,
                3,
                0,
                False,
            ),
            Gem("Double Strike", 0.96, 20, 0, True),
        }

    def test_calculate_profitability(self, vaal_gem_set):
        profitability = calculate_profitability("Grace", vaal_gem_set)
        approx(
            profitability,
            GemProfit(
                Gem("Grace", 3, 1, 0, False),
                7,
                7.125,
                10.475,
                0.125,
                3.475,
                2,
            ),
        )
