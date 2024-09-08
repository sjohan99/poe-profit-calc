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
    SKILL_GEM = "SkillGem"
    UNIQUE_MAP = "UniqueMap"


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


class AwakenedAddedColdDamageSupport(Item):
    name = "Awakened Added Cold Damage Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedAddedFireDamageSupport(Item):
    name = "Awakened Added Fire Damage Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedAddedLightningDamageSupport(Item):
    name = "Awakened Added Lightning Damage Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedAncestralCallSupport(Item):
    name = "Awakened Ancestral Call Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedArrowNovaSupport(Item):
    name = "Awakened Arrow Nova Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedChainSupport(Item):
    name = "Awakened Chain Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedBlasphemySupport(Item):
    name = "Awakened Blasphemy Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedBurningDamageSupport(Item):
    name = "Awakened Burning Damage Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedCastOnCriticalStrikeSupport(Item):
    name = "Awakened Cast On Critical Strike Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedCastWhileChannellingSupport(Item):
    name = "Awakened Cast While Channelling Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedColdPenetrationSupport(Item):
    name = "Awakened Cold Penetration Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedDeadlyAilmentsSupport(Item):
    name = "Awakened Deadly Ailments Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedEnhanceSupport(Item):
    name = "Awakened Enhance Support"
    droprate = 0.005
    source = PoeNinjaSource.SKILL_GEM


class AwakenedForkSupport(Item):
    name = "Awakened Fork Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedGreaterMultipleProjectilesSupport(Item):
    name = "Awakened Greater Multiple Projectiles Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedSwiftAfflictionSupport(Item):
    name = "Awakened Swift Affliction Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedViciousProjectilesSupport(Item):
    name = "Awakened Vicious Projectiles Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedVoidManipulationSupport(Item):
    name = "Awakened Void Manipulation Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedAddedChaosDamageSupport(Item):
    name = "Awakened Added Chaos Damage Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedControlledDestructionSupport(Item):
    name = "Awakened Controlled Destruction Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedElementalFocusSupport(Item):
    name = "Awakened Elemental Focus Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedEnlightenSupport(Item):
    name = "Awakened Enlighten Support"
    droprate = 0.005
    source = PoeNinjaSource.SKILL_GEM


class AwakenedHextouchSupport(Item):
    name = "Awakened Hextouch Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedIncreasedAreaOfEffectSupport(Item):
    name = "Awakened Increased Area of Effect Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedLightningPenetrationSupport(Item):
    name = "Awakened Lightning Penetration Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedMinionDamageSupport(Item):
    name = "Awakened Minion Damage Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedSpellCascadeSupport(Item):
    name = "Awakened Spell Cascade Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedSpellEchoSupport(Item):
    name = "Awakened Spell Echo Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedUnboundAilmentsSupport(Item):
    name = "Awakened Unbound Ailments Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedUnleashSupport(Item):
    name = "Awakened Unleash Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedBruitalitySupport(Item):
    name = "Awakened Brutality Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedElementalDamageWithAttacksSupport(Item):
    name = "Awakened Elemental Damage with Attacks Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedEmpowerSupport(Item):
    name = "Awakened Empower Support"
    droprate = 0.005
    source = PoeNinjaSource.SKILL_GEM


class AwakenedFirePenetrationSupport(Item):
    name = "Awakened Fire Penetration Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedGenerositySupport(Item):
    name = "Awakened Generosity Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedMeleePhysicalDamageSupport(Item):
    name = "Awakened Melee Physical Damage Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedMeleeSplashSupport(Item):
    name = "Awakened Melee Splash Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class AwakenedMultistrikeSupport(Item):
    name = "Awakened Multistrike Support"
    droprate = 0.25
    source = PoeNinjaSource.SKILL_GEM


class TheMavensWrit(Item):
    name = "The Maven's Writ"
    droprate = 0
    source = PoeNinjaSource.FRAGMENT


class LegacyOfFury(Item):
    name = "Legacy of Fury"
    droprate = 0.45
    source = PoeNinjaSource.UNIQUE_ARMOUR


class GravensSecret(Item):
    name = "Graven's Secret"
    droprate = 0.16
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class ArnsAnguish(Item):
    name = "Arn's Anguish"
    droprate = 0.16
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class OlesyasDelight(Item):
    name = "Olesya's Delight"
    droprate = 0.16
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class DoppelgangerGuise(Item):
    name = "Doppelgänger Guise"
    droprate = 0.06
    source = PoeNinjaSource.UNIQUE_ARMOUR


class Echoforge(Item):
    name = "Echoforge"
    droprate = 0.01
    source = PoeNinjaSource.UNIQUE_WEAPON


class OrbOfConflict(Item):
    name = "Orb of Conflict"
    droprate = 0.35
    source = PoeNinjaSource.CURRENCY


class ViridisVeil(Item):
    name = "Viridi's Veil"
    droprate = 0.55
    source = PoeNinjaSource.UNIQUE_ARMOUR


class ImpossibleEscape(Item):
    name = "Impossible Escape"
    droprate = 0.33
    source = PoeNinjaSource.UNIQUE_JEWEL


class Progenesis(Item):
    name = "Progenesis"
    droprate = 0.11
    source = PoeNinjaSource.UNIQUE_FLASK


class GraceOfTheGoddess(Item):
    name = "Grace of the Goddess"
    droprate = 0.05
    source = PoeNinjaSource.UNIQUE_WEAPON


class CurioOfPotential(Item):
    name = "Curio of Potential"
    droprate = 0.05
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class ShinyReliquaryKey(Item):
    name = "Shiny Reliquary Key"
    droprate = 0.015
    source = PoeNinjaSource.FRAGMENT


class TheGluttonousTide(Item):
    name = "The Gluttonous Tide"
    droprate = 0.5
    source = PoeNinjaSource.UNIQUE_WEAPON


class InextricableFate(Item):
    name = "Inextricable Fate"
    droprate = 0.5
    source = PoeNinjaSource.UNIQUE_ARMOUR


class MeldingOfTheFlesh(Item):
    name = "Melding of the Flesh"
    droprate = 0.02
    source = PoeNinjaSource.UNIQUE_JEWEL


class ForbiddenFlesh(Item):
    name = "Forbidden Flesh"
    droprate = 0.05
    source = PoeNinjaSource.UNIQUE_JEWEL


class ExceptionalEldritchIchor(Item):
    name = "Exceptional Eldritch Ichor"
    droprate = 0.15
    source = PoeNinjaSource.CURRENCY


class Nimis(Item):
    name = "Nimis"
    droprate = 0.01
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class RavenousPassion(Item):
    name = "Ravenous Passion"
    droprate = 0.66
    source = PoeNinjaSource.UNIQUE_ARMOUR


class AshesOfTheStars(Item):
    name = "Ashes of the Stars"
    droprate = 0.33
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class ForbiddenFleshUber(Item):
    name = "Forbidden Flesh"
    droprate = 0.05
    source = PoeNinjaSource.UNIQUE_JEWEL


class VisceralReliquaryKey(Item):
    name = "Visceral Reliquary Key"
    droprate = 0.01
    source = PoeNinjaSource.FRAGMENT


class CurioOfConsumption(Item):
    name = "Curio of Consumption"
    droprate = 0.05
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class TheAnnihilatingLight(Item):
    name = "The Annihilating Light"
    droprate = 0.475
    source = PoeNinjaSource.UNIQUE_WEAPON


class AnnihilationsApproach(Item):
    name = "Annihilation's Approach"
    droprate = 0.25
    source = PoeNinjaSource.UNIQUE_ARMOUR


class TheCelestialBrace(Item):
    name = "The Celestial Brace"
    droprate = 0.25
    source = PoeNinjaSource.UNIQUE_ARMOUR


class CrystallisedOmniscience(Item):
    name = "Crystallised Omniscience"
    droprate = 0.025
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class ForbiddenFlameUber(Item):
    name = "Forbidden Flame"
    droprate = 0.05
    source = PoeNinjaSource.UNIQUE_JEWEL


class ArchiveReliquaryKey(Item):
    name = "Archive Reliquary Key"
    droprate = 0.015
    source = PoeNinjaSource.FRAGMENT


class CurioOfAbsorption(Item):
    name = "Curio of Absorption"
    droprate = 0.05
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class CallOfTheVoid(Item):
    name = "Call of the Void"
    droprate = 0.5
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class TheDevourerOfMinds(Item):
    name = "The Devourer of Minds"
    droprate = 0.3
    source = PoeNinjaSource.UNIQUE_ARMOUR


class SoulAscension(Item):
    name = "Soul Ascension"
    droprate = 0.1
    source = PoeNinjaSource.UNIQUE_ARMOUR


class TheEternityShroud(Item):
    name = "The Eternity Shroud"
    droprate = 0.09
    source = PoeNinjaSource.UNIQUE_ARMOUR


class Voidforge(Item):
    name = "Voidforge"
    droprate = 0.01
    source = PoeNinjaSource.UNIQUE_WEAPON


class CurioOfDecay(Item):
    name = "Curio of Decay"
    droprate = 0.05
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class DecayingReliquaryKey(Item):
    name = "Decaying Reliquary Key"
    droprate = 0.015
    source = PoeNinjaSource.FRAGMENT


class OfferingToTheSerpent(Item):
    name = "Offering to the Serpent"
    droprate = 0.45
    source = PoeNinjaSource.UNIQUE_ARMOUR


class Perepiteia(Item):
    name = "Perepiteia"
    droprate = 0.45
    source = PoeNinjaSource.UNIQUE_ARMOUR


class GarbOfTheEphemeral(Item):
    name = "Garb of the Ephemeral"
    droprate = 0.08
    source = PoeNinjaSource.UNIQUE_ARMOUR


class BottledFaith(Item):
    name = "Bottled Faith"
    droprate = 0.02
    source = PoeNinjaSource.UNIQUE_FLASK


class TheHook(Item):
    name = "The Hook"
    droprate = 0.05
    source = PoeNinjaSource.DIVINATION_CARD


class MaskOfTheTribunal(Item):
    name = "Mask of the Tribunal"
    droprate = 0.4
    source = PoeNinjaSource.UNIQUE_ARMOUR


class Nebulis(Item):
    name = "Nebulis"
    droprate = 0.33
    source = PoeNinjaSource.UNIQUE_WEAPON


class CircleOfAmbition(Item):
    name = "Circle of Ambition"
    droprate = 0.17
    source = PoeNinjaSource.UNIQUE_ACCESSORY


class TheApostate(Item):
    name = "The Apostate"
    droprate = 0.08
    source = PoeNinjaSource.UNIQUE_ARMOUR


class RationalDoctrine(Item):
    name = "Rational Doctrine"
    droprate = 0.02
    source = PoeNinjaSource.UNIQUE_JEWEL


class ForgottenReliquaryKey(Item):
    name = "Forgotten Reliquary Key"
    droprate = 0.015
    source = PoeNinjaSource.FRAGMENT


class Cortex(Item):
    name = "Cortex"
    droprate = 0.01
    source = PoeNinjaSource.UNIQUE_MAP
