from abc import ABC, abstractmethod
from ex0.creatures import Creature, CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        '''heal self, or others'''


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        '''transform'''

    @abstractmethod
    def revert(self) -> str:
        '''revert'''

# == Healer family ============================================================


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Grass")

    def attack(self) -> str:
        return (f"{self.name} uses Vine Whip!")

    def heal(self) -> str:
        return (f"{self.name} heals itself for a small amount")


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Grass/Fairy")

    def attack(self) -> str:
        return (f"{self.name} uses Petal Dance!")

    def heal(self) -> str:
        return (f"{self.name} heals itself and others for a large amount")

# == Transform family =========================================================


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Normal")
        self.attacks: list[str] = [
                "attacks normally.",
                "performs a boosted strike!",
                ]

    def attack(self) -> str:
        attack = f"{self.name} {self.attacks[0]}"
        self.attacks = self.attacks[1:] + self.attacks[:1]
        return (attack)

    def transform(self) -> str:
        return (f"{self.name} shifts into a sharper form!")

    def revert(self) -> str:
        return (f"{self.name} returns to normal.")


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Normal/Dragon")
        self.attacks: list[str] = [
                "attacks normally.",
                "unleashes a devastating morph strike!",
                ]

    def attack(self) -> str:
        attack = f"{self.name} {self.attacks[0]}"
        self.attacks = self.attacks[1:] + self.attacks[:1]
        return (attack)

    def transform(self) -> str:
        return (f"{self.name} morphs into a dragonic battle form!")

    def revert(self) -> str:
        return (f"{self.name} stabilizes its form.")


# == Factories ================================================================

class HealingCreatureFactory(CreatureFactory):
    @staticmethod
    def create_base() -> Sproutling:
        return Sproutling()

    @staticmethod
    def create_evolved() -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    @staticmethod
    def create_base() -> Shiftling:
        return Shiftling()

    @staticmethod
    def create_evolved() -> Morphagon:
        return Morphagon()
