from poe_profit_calc.items import PoeNinjaSource


BASE_NINJA_URL = "https://poe.ninja/api/data/"
LEAGUE = "Settlers"

ENDPOINT_MAPPING = {
    PoeNinjaSource.CURRENCY: f"{BASE_NINJA_URL}currencyoverview?league={LEAGUE}&type=Currency",
    PoeNinjaSource.UNIQUE_ARMOUR: f"{BASE_NINJA_URL}itemoverview?league={LEAGUE}&type=UniqueArmour",
    PoeNinjaSource.UNIQUE_JEWEL: f"{BASE_NINJA_URL}itemoverview?league={LEAGUE}&type=UniqueJewel",
    PoeNinjaSource.INVITATION: f"{BASE_NINJA_URL}itemoverview?league={LEAGUE}&type=Invitation",
    PoeNinjaSource.FRAGMENT: f"{BASE_NINJA_URL}currencyoverview?league={LEAGUE}&type=Fragment",
    PoeNinjaSource.UNIQUE_ACCESSORY: f"{BASE_NINJA_URL}itemoverview?league={LEAGUE}&type=UniqueAccessory",
    PoeNinjaSource.UNIQUE_FLASK: f"{BASE_NINJA_URL}itemoverview?league={LEAGUE}&type=UniqueFlask",
    PoeNinjaSource.UNIQUE_WEAPON: f"{BASE_NINJA_URL}itemoverview?league={LEAGUE}&type=UniqueWeapon",
    PoeNinjaSource.DIVINATION_CARD: f"{BASE_NINJA_URL}itemoverview?league={LEAGUE}&type=DivinationCard",
    PoeNinjaSource.SKILL_GEM: f"{BASE_NINJA_URL}itemoverview?league={LEAGUE}&type=SkillGem",
}

FILE_PATH_MAPPING = {
    PoeNinjaSource.CURRENCY: "static/currencyoverview_currency.json",
    PoeNinjaSource.UNIQUE_ARMOUR: "static/itemoverview_uniquearmour.json",
    PoeNinjaSource.UNIQUE_JEWEL: "static/itemoverview_uniquejewel.json",
    PoeNinjaSource.INVITATION: "static/itemoverview_invitation.json",
    PoeNinjaSource.FRAGMENT: "static/currencyoverview_fragment.json",
    PoeNinjaSource.UNIQUE_ACCESSORY: "static/itemoverview_uniqueaccessory.json",
    PoeNinjaSource.UNIQUE_FLASK: "static/itemoverview_uniqueflask.json",
    PoeNinjaSource.UNIQUE_WEAPON: "static/itemoverview_uniqueweapon.json",
    PoeNinjaSource.DIVINATION_CARD: "static/itemoverview_divinationcard.json",
    PoeNinjaSource.SKILL_GEM: "static/itemoverview_skillgem.json",
}
