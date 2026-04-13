from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, type: str):
        self.name: str = self.__class__.__name__
        self.type: str = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


# === Creatures ===============================================================


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Fire")

    def attack(self) -> str:
        return (f"{self.name} uses Ember!")


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Fire/Flying")

    def attack(self) -> str:
        return (f"{self.name} uses Flamethrower!")


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Water")

    def attack(self) -> str:
        return (f"{self.name} uses Water Gun!")


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Water")

    def attack(self) -> str:
        return (f"{self.name} uses Hydro Pump!")


# === Factories ===============================================================


class CreatureFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_base() -> Creature:
        '''create a base creature'''

    @staticmethod
    @abstractmethod
    def create_evolved() -> Creature:
        '''create an evolved creature'''


class FlameFactory(CreatureFactory):
    @staticmethod
    def create_base() -> Flameling:
        return Flameling()

    @staticmethod
    def create_evolved() -> Pyrodon:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    @staticmethod
    def create_base() -> Aquabub:
        return Aquabub()

    @staticmethod
    def create_evolved() -> Torragon:
        return Torragon()
