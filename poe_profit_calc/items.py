from dataclasses import dataclass
from enum import Enum


class PoeNinjaSource(Enum):
    CURRENCY = "Currency"
    UNIQUE_ARMOUR = "UniqueArmour"
    UNIQUE_JEWEL = "UniqueJewel"
    INVITATION = "Invitation"
    FRAGMENT = "Fragment"
    UNIQUE_ACCESSORY = "UniqueAccessory"
    UNIQUE_FLASK = "UniqueFlask"
    UNIQUE_WEAPON = "UniqueWeapon"


@dataclass
class Item:
    name: str
    droprate: float
    source: PoeNinjaSource


class IncandescentInvitation(Item):
    name = "Incandescent Invitation"
    droprate = 0
    source = PoeNinjaSource.INVITATION


class ScreamingInvitation(Item):
    name = "Screaming Invitation"
    droprate = 0
    source = PoeNinjaSource.INVITATION


class PolaricInvitation(Item):
    name = "Polaric Invitation"
    droprate = 0
    source = PoeNinjaSource.INVITATION


class WrithingInvitation(Item):
    name = "Writhing Invitation"
    droprate = 0
    source = PoeNinjaSource.INVITATION


class DevouringFragment(Item):
    name = "Devouring Fragment"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class RealityFragment(Item):
    name = "Reality Fragment"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class DecayingFragment(Item):
    name = "Decaying Fragment"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class BlazingFragment(Item):
    name = "Blazing Fragment"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class AwakeningFragment(Item):
    name = "Awakening Fragment"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class CosmicFragment(Item):
    name = "Cosmic Fragment"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class SynthesisingFragment(Item):
    name = "Synthesising Fragment"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class FragmentOfEmptiness(Item):
    name = "Fragment of Emptiness"
    droprate = 0.5
    source = PoeNinjaSource.FRAGMENT


class FragmentOfTerror(Item):
    name = "Fragment of Terror"
    droprate = 0.5
    source = PoeNinjaSource.FRAGMENT


class FragmentOfKnowledge(Item):
    name = "Fragment of Knowledge"
    droprate = 0.5
    source = PoeNinjaSource.FRAGMENT


class FragmentOfShape(Item):
    name = "Fragment of Shape"
    droprate = 0.5
    source = PoeNinjaSource.FRAGMENT


class FragmentOfConstriction(Item):
    name = "Fragment of Constriction"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class FragmentOfEnslavement(Item):
    name = "Fragment of Enslavement"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class FragmentOfEradication(Item):
    name = "Fragment of Eradication"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class FragmentOfPurification(Item):
    name = "Fragment of Purification"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class FragmentOfThePhoenix(Item):
    name = "Fragment of the Phoenix"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class FragmentOfTheHydra(Item):
    name = "Fragment of the Hydra"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class FragmentOfTheMinotaur(Item):
    name = "Fragment of the Minotaur"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class FragmentOfTheChimera(Item):
    name = "Fragment of the Chimera"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


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


class ShapersTouch(Item):
    name = "Shaper's Touch"
    droprate = 0.56
    source = PoeNinjaSource.UNIQUE_ARMOUR


class VoidWalker(Item):
    name = "Voidwalker"
    droprate = 0.33
    source = PoeNinjaSource.UNIQUE_ARMOUR


class SolsticeVigil(Item):
    name = "Solstice Vigil"
    droprate = 0.1
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class DyingSun(Item):
    name = "Dying Sun"
    droprate = 0.01
    source = PoeNinjaSource.UNIQUE_FLASK


class OrbOfDominance(Item):
    name = "Orb of Dominance"
    droprate = 0.01
    source = PoeNinjaSource.CURRENCY


class EchoesOfCreation(Item):
    name = "Echoes of Creation"
    droprate = 0.46
    source = PoeNinjaSource.UNIQUE_ARMOUR


class TheTidesOfTime(Item):
    name = "The Tides of Time"
    droprate = 0.33
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class EntropicDevastation(Item):
    name = "Entropic Devastation"
    droprate = 0.20
    source = PoeNinjaSource.UNIQUE_JEWEL


class StarForge(Item):
    name = "Starforge"
    droprate = 0.05
    source = PoeNinjaSource.UNIQUE_WEAPON


class SublimeVision(Item):
    name = "Sublime Vision"
    droprate = 0.025
    source = PoeNinjaSource.UNIQUE_JEWEL


class CosmicReliquaryKey(Item):
    name = "Cosmic Reliquary Key"
    droprate = 0.01
    source = PoeNinjaSource.FRAGMENT
