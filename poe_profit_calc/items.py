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
    DIVINATION_CARD = "DivinationCard"


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


class BaransCrest(Item):
    name = "Baran's Crest"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class DroxsCrest(Item):
    name = "Drox's Crest"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class VeritaniasCrest(Item):
    name = "Veritania's Crest"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class AlHezminsCrest(Item):
    name = "Al-Hezmin's Crest"
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


class OrbOfDominanceShaper(Item):
    name = "Orb of Dominance"
    droprate = 0.01
    source = PoeNinjaSource.CURRENCY


class OrbOfDominanceElder(Item):
    name = "Orb of Dominance"
    droprate = 0.05
    source = PoeNinjaSource.CURRENCY


class OrbOfDominanceSirus(Item):
    name = "Orb of Dominance"
    droprate = 0.05
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


class BlashphemersGrasp(Item):
    name = "Blasphemer's Grasp"
    droprate = 0.25
    source = PoeNinjaSource.UNIQUE_ARMOUR


class CyclopeanCoil(Item):
    name = "Cyclopean Coil"
    droprate = 0.25
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class Nebuloch(Item):
    name = "Nebuloch"
    droprate = 0.1
    source = PoeNinjaSource.UNIQUE_WEAPON


class Hopeshredder(Item):
    name = "Hopeshredder"
    droprate = 0.1
    source = PoeNinjaSource.UNIQUE_WEAPON


class Shimmeron(Item):
    name = "Shimmeron"
    droprate = 0.1
    source = PoeNinjaSource.UNIQUE_WEAPON


class Impresence(Item):
    name = "Impresence"
    droprate = 0.2
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class TwoModWatcherEye(Item):
    name = "Watcher's Eye"
    droprate = 0.35
    source = PoeNinjaSource.UNIQUE_JEWEL


class ThreeModWatcherEye(Item):
    name = "Watcher's Eye"
    droprate = 0.35
    source = PoeNinjaSource.UNIQUE_JEWEL


class MarkOfTheShaper(Item):
    name = "Mark of the Shaper"
    droprate = 0.35
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class MarkOfTheElder(Item):
    name = "Mark of the Elder"
    droprate = 0.35
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class Voidfletcher(Item):
    name = "Voidfletcher"
    droprate = 0.25
    source = PoeNinjaSource.UNIQUE_ARMOUR


class Indigon(Item):
    name = "Indigon"
    droprate = 0.4
    source = PoeNinjaSource.UNIQUE_ARMOUR


class Disintegrator(Item):
    name = "Disintegrator"
    droprate = 0.01
    source = PoeNinjaSource.UNIQUE_WEAPON


class TheGulf(Item):
    name = "The Gulf"
    droprate = 0.04
    source = PoeNinjaSource.DIVINATION_CARD


class VoidOfTheElements(Item):
    name = "Void of the Elements"
    droprate = 0.04
    source = PoeNinjaSource.DIVINATION_CARD


class HandsOfTheHighTemplar(Item):
    name = "Hands of the High Templar"
    droprate = 0.45
    source = PoeNinjaSource.UNIQUE_ARMOUR


class CrownOfTheInwardEye(Item):
    name = "Crown of the Inward Eye"
    droprate = 0.38
    source = PoeNinjaSource.UNIQUE_ARMOUR


class TheBurdenOfTruth(Item):
    name = "The Burden of Truth"
    droprate = 0.15
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class ThreadOfHope(Item):
    name = "Thread of Hope"
    droprate = 0.2
    source = PoeNinjaSource.UNIQUE_JEWEL


class ThreadOfHopeMassive(Item):
    name = "Thread of Hope"
    droprate = 0.55
    source = PoeNinjaSource.UNIQUE_JEWEL


class AwakenersOrb(Item):
    name = "Awakener's Orb"
    droprate = 0.15
    source = PoeNinjaSource.CURRENCY


class AFateWorseThanDeath(Item):
    name = "A Fate Worse Than Death"
    droprate = 0.05
    source = PoeNinjaSource.DIVINATION_CARD


class TheTempestRising(Item):
    name = "The Tempest Rising"
    droprate = 0.35
    source = PoeNinjaSource.UNIQUE_ARMOUR


class OriathsEnd(Item):
    name = "Oriath's End"
    droprate = 0.09
    source = PoeNinjaSource.UNIQUE_FLASK


class TheSaviour(Item):
    name = "The Saviour"
    droprate = 0.01
    source = PoeNinjaSource.UNIQUE_WEAPON


class OublietteReliquaryKey(Item):
    name = "Oubliette Reliquary Key"
    droprate = 0.015
    source = PoeNinjaSource.FRAGMENT
