from dataclasses import dataclass
from random import uniform
import marshmallow_dataclass
import marshmallow
import json


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self):
        return round(uniform(self.min_damage, self.max_damage),1)


@dataclass
class EquipmentData:
    weapons: list[Weapon]
    armors: list[Armor]


class Equipment:

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Weapon | None:
        for item in self.equipment.weapons:
            if item.name == weapon_name:
                return item
        return None


    def get_armor(self, armor_name) -> Armor | None:
        for item in self.equipment.armors:
            if item.name == armor_name:
                return item
        return None

    def get_weapons_names(self) -> list:
        return [weapon.name for weapon in self.equipment.weapons]

    def get_armors_names(self) -> list:
        return [armor.name for armor in self.equipment.armors]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        with open("./data/equipment.json", mode='r', encoding='utf-8') as file:
            data = json.load(file)
            equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
            try:
                return equipment_schema().load(data)
            except marshmallow.exceptions.ValidationError:
                raise ValueError
