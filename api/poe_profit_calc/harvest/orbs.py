import msgspec

PRIMAL_LIFEFORCE_PER_ORB_REROLL = 30

orb_weights = {
    "Abyssal Delirium Orb": 35,
    "Armoursmith's Delirium Orb": 736,
    "Blacksmith's Delirium Orb": 698,
    "Blighted Delirium Orb": 50,
    "Cartographer's Delirium Orb": 85,
    "Diviner's Delirium Orb": 161,
    "Fine Delirium Orb": 605,
    "Foreboding Delirium Orb": 99,
    "Fossilised Delirium Orb": 31,
    "Fragmented Delirium Orb": 53,
    "Jeweller's Delirium Orb": 765,
    "Obscured Delirium Orb": 26,
    "Singular Delirium Orb": 74,
    "Skittering Delirium Orb": 24,
    "Thaumaturge's Delirium Orb": 47,
    "Timeless Delirium Orb": 41,
    "Whispering Delirium Orb": 93,
}

total_orb_weight = sum(orb_weights.values())


class Orb(msgspec.Struct):
    name: str
    chaosValue: float
    icon: str | None = None
    reroll_weight: int = msgspec.field(default=0)

    def __post_init__(self):
        self.reroll_weight = orb_weights.get(self.name, 0)

    def __hash__(self) -> int:
        return hash(self.name)


class OrbData(msgspec.Struct):
    lines: set[Orb]


def parse(json_b: bytes) -> set[Orb]:
    try:
        parsed = msgspec.json.decode(json_b, type=OrbData)
        return parsed.lines
    except msgspec.DecodeError:
        return set()


def calculate_profits(orbs: set[Orb], primal_lifeforce_cost: float) -> dict[Orb, float]:
    """
    Calculates the expected profit for from rerolling each orb in `orbs`

    Parameters:
        orbs (set[Orb]): All orbs to be considered in the calculation.
        primal_lifeforce_cost (float): The cost of 1 primal lifeforce in chaos orbs.
    Returns:
        A dictionary mapping each orb to its expected profit from rerolling (a single orb).
    """
    orb_profits = {}
    for orb in orbs:
        other_orbs = orbs - {orb}
        other_orbs_weight = total_orb_weight - orb.reroll_weight
        expected_new_value = sum(
            [(orb2.reroll_weight / other_orbs_weight) * orb2.chaosValue for orb2 in other_orbs]
        )
        cost = orb.chaosValue + primal_lifeforce_cost * 30
        orb_profits[orb] = expected_new_value - cost
    return orb_profits
