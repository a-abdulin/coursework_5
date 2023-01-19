from dataclasses import dataclass

from skills import Skill, FuryPunch, HardShot


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name='Воин',
    max_health=60.0,
    max_stamina=30.0,
    attack=1.3,
    stamina=0.7,
    armor=1.2,
    skill=FuryPunch(),
)

ThiefClass = UnitClass(
    name='Лучник',
    max_health=50.0,
    max_stamina=25.0,
    attack=1.6,
    stamina=0.9,
    armor=0.9,
    skill=HardShot(),
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}