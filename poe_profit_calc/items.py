from dataclasses import dataclass
from enum import Enum


class PoeNinjaSource(Enum):
    CURRENCY = "Currency"
    UNIQUE_ARMOUR = "UniqueArmour"
    UNIQUE_JEWEL = "UniqueJewel"


@dataclass
class Item:
    """Poe item information.

    poe_ninja_x attributes are used to get the item price from poe.ninja api.

    The URL https://poe.ninja/api/data/currencyoverview?league=Settlers&type=Currency
    would give 'currencyoverview' as the category and 'Currency' as the type. The name
    would be found in the

    Attributes:
        name (int): Item name in pretty form.
        droprate (str): Chance to drop (0 to 1).
        poe_ninja_name (str): Item name in poe.ninja api.
        poe_ninja_category (str): Item category in poe.ninja api.
        poe_ninja_type (str): Item type in poe.ninja api.
    """

    name: str
    droprate: float
    source: PoeNinjaSource


class Dawnbreaker(Item):
    name = "Dawnbreaker"
    droprate = 0.33
    source = PoeNinjaSource.UNIQUE_ARMOUR


class Dawnstrider(Item):
    name = "Dawnstrider"
    droprate = 0.65
    source = PoeNinjaSource.UNIQUE_ARMOUR


class DissolutionOfTheFlesh(Item):
    name = "Dissolution of the Flesh"
    droprate = 0.33
    source = PoeNinjaSource.UNIQUE_JEWEL


class ForbiddenFlame(Item):
    name = "Forbidden Flame"
    droprate = 0.05
    source = PoeNinjaSource.UNIQUE_JEWEL


class ExceptionalEldritchEmber(Item):
    name = "Exceptional Eldritch Ember"
    droprate = 0.15
    source = PoeNinjaSource.CURRENCY


class EldritchOrbOfAnnulment(Item):
    name = "Eldritch Orb of Annulment"
    droprate = 0.05
    source = PoeNinjaSource.CURRENCY


class EldritchChaosOrb(Item):
    name = "Eldritch Chaos Orb"
    droprate = 0.05
    source = PoeNinjaSource.CURRENCY


class EldritchExaltedOrb(Item):
    name = "Eldritch Exalted Orb"
    droprate = 0.05
    source = PoeNinjaSource.CURRENCY
