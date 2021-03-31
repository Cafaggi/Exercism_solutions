from dataclasses import dataclass, fields
from numpy.random import randint


@dataclass
class Character:

    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    def __init__(self):
        for field in fields(self):
            setattr(self, field.name, self.ability())
        self.hitpoints =  10 + modifier(self.constitution)

    def ability(self) -> int:
        return sum(sorted(randint(1,6,size=6))[:3])
    
def modifier(constitution: int) -> int:
    return (constitution-10)//2

ch = Character()
ch.strength