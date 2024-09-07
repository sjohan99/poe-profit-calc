from poe_profit_calc.items import *


@dataclass
class Boss:
    """Poe boss information.

    Attributes:
        name (str): Boss name.
        entrance_items (dict[Item, int]): Items required to enter the boss fight, with the item as the key and the quantity as the value.
        drops (List[ItemInfo]): All Items that the boss drops.
    """

    name: str
    entrance_items: dict[Item, int]
    drops: set[Item]


class TheSearingExarch(Boss):
    name = "The Searing Exarch"
    entrance_items = {IncandescentInvitation: 1}
    drops = {
        Dawnbreaker,
        Dawnstrider,
        DissolutionOfTheFlesh,
        ForbiddenFlame,
        ExceptionalEldritchEmber,
        EldritchOrbOfAnnulment,
        EldritchChaosOrb,
        EldritchExaltedOrb,
    }


class TheShaper(Boss):
    name = "The Shaper"
    entrance_items = {
        FragmentOfTheHydra: 1,
        FragmentOfTheMinotaur: 1,
        FragmentOfThePhoenix: 1,
        FragmentOfTheChimera: 1,
    }
    drops = {
        ShapersTouch,
        VoidWalker,
        SolsticeVigil,
        DyingSun,
        FragmentOfKnowledge,
        FragmentOfShape,
        OrbOfDominance,
    }


class TheShaperUber(Boss):
    name = "The Shaper Uber"
    entrance_items = {
        CosmicFragment: 5,
    }
    drops = {
        EchoesOfCreation,
        TheTidesOfTime,
        EntropicDevastation,
        StarForge,
        SublimeVision,
        CosmicReliquaryKey,
        FragmentOfKnowledge,
        FragmentOfShape,
        OrbOfDominance,
    }
