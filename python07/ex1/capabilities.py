from abc import ABC, abstractmethod
from typing import Protocol
from ex0.creatures import Creature, CreatureFactory


class HealerProtocol(Protocol):
    @staticmethod
    def describe() -> str:
        ...

    @staticmethod
    def attack() -> str:
        ...

    @staticmethod
    def heal() -> str:
        ...


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        '''heal self, or others'''


class TransformerProtocol(Protocol):
    @staticmethod
    def describe() -> str:
        ...

    @staticmethod
    def attack() -> str:
        ...

    @staticmethod
    def transform() -> str:
        ...

    @staticmethod
    def revert() -> str:
        ...


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        '''transform'''

    @abstractmethod
    def revert(self) -> str:
        '''revert'''

# == Healer family ============================================================


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Grass")

    def attack(self) -> str:
        return (f"{self.name} uses Vine Whip!")

    def heal(self) -> str:
        return (f"{self.name} heals itself for a small amount")


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Grass/Fairy")

    def attack(self) -> str:
        return (f"{self.name} uses Petal Dance!")

    def heal(self) -> str:
        return (f"{self.name} heals itself and others for a large amount")

# == Transform family =========================================================


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Normal")
        self.attacks: list[str] = [
                "attacks normally.",
                "performs a boosted strike!",
                ]

    def attack(self) -> str:
        attack = f"{self.name} {self.attacks[0]}"
        self.attacks = self.attacks[1:] + self.attacks[:1]
        return (attack)


    def transform(self):
        return (f"{self.name} shifts into a sharper form!")

    def revert(self):
        return (f"{self.name} returns to normal.")


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Normal/Dragon")
        self.attacks: list[str] = [
                "attacks normally.",
                "unleashes a devastating morph strike!",
                ]

    def attack(self) -> str:
        attack = f"{self.name} {self.attacks[0]}"
        self.attacks = self.attacks[1:] + self.attacks[:1]
        return (attack)

    def transform(self):
        return (f"{self.name} morphs into a dragonic battle form!")

    def revert(self):
        return (f"{self.name} stabilizes its form.")


# == Factories ================================================================

class HealingCreatureFactory(CreatureFactory):
    @staticmethod
    def create_base(name: str) -> Sproutling:
        return Sproutling(name)

    @staticmethod
    def create_evolved(name: str) -> Bloomelle:
        return Bloomelle(name)


class TransformCreatureFactory(CreatureFactory):
    @staticmethod
    def create_base(name: str) -> Shiftling:
        return Shiftling(name)

    @staticmethod
    def create_evolved(name: str) -> Morphagon:
        return Morphagon(name)
