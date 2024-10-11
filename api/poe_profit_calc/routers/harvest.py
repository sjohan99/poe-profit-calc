from cachetools import TTLCache, cached
from fastapi import APIRouter
from poe_profit_calc.harvest import (
    Orb,
    calculate_profits,
    parse,
    PrimalCrystallisedLifeforce,
    PRIMAL_LIFEFORCE_PER_ORB_REROLL,
    total_orb_weight,
)
from poe_profit_calc.items import Item
from poe_profit_calc.setup.setup import App
from poe_profit_calc.sources import PoeNinjaSource
from pydantic import BaseModel

router = APIRouter(
    prefix="/harvest",
)

price_fetcher = App.get_instance().price_fetcher


class RerollItemData(BaseModel):
    name: str
    chaos_value: float
    icon: str | None = None
    reroll_weight: int = 0
    expected_reroll_profit: float
    lifeforce_per_reroll: int

    @staticmethod
    def from_orb(orb: Orb, profit: float):
        return RerollItemData(
            name=orb.name,
            chaos_value=orb.chaosValue,
            icon=orb.icon,
            reroll_weight=orb.reroll_weight,
            expected_reroll_profit=profit,
            lifeforce_per_reroll=PRIMAL_LIFEFORCE_PER_ORB_REROLL,
        )


class Lifeforce(BaseModel):
    name: str
    chaos_value: float
    icon: str | None = None

    @staticmethod
    def from_item(lifeforce: Item):
        return Lifeforce(
            name=lifeforce.name,
            chaos_value=lifeforce.price,
            icon=lifeforce.img,
        )


class RerollSummary(BaseModel):
    items: list[RerollItemData]
    lifeforce: Lifeforce
    total_weight: int


@router.get("/orbs")
@cached(cache=TTLCache(maxsize=128, ttl=1800))
def get_orb_summary() -> RerollSummary:
    primal_lifeforce = PrimalCrystallisedLifeforce
    price_fetcher.price_items({primal_lifeforce})
    raw_data = price_fetcher.get_raw_endpoint(PoeNinjaSource.DELIRIUM_ORB)
    parsed_data = parse(raw_data)
    profits = calculate_profits(parsed_data, primal_lifeforce.price)
    orb_data = [RerollItemData.from_orb(orb, profit) for orb, profit in profits.items()]
    orb_data.sort(key=lambda x: x.expected_reroll_profit, reverse=True)
    lifeforce = Lifeforce.from_item(primal_lifeforce)
    summary = RerollSummary(items=orb_data, lifeforce=lifeforce, total_weight=total_orb_weight)
    return summary
