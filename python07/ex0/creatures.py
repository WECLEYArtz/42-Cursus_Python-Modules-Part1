from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str):
        self.name: str = name
        self.type: str = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Fire")

    def attack(self) -> str:
        return (f"{self.name} uses Ember!")


# === Creatures ===============================================================


class Pyrodon(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Fire/Flying")

    def attack(self) -> str:
        return (f"{self.name} uses Flamethrower!")


class Aquabub(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Water")

    def attack(self) -> str:
        return (f"{self.name} uses Water Gun!")


class Torragon(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Water")

    def attack(self) -> str:
        return (f"{self.name} uses Hydro Pump!")


# === Factories ===============================================================


class CreatureFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_base(name: str) -> Creature:
        '''create a base creature'''

    @staticmethod
    @abstractmethod
    def create_evolved(name: str) -> Creature:
        '''create an evolved creature'''


class FlameFactory(CreatureFactory):
    @staticmethod
    def create_base(name: str) -> Flameling:
        return Flameling(name)

    @staticmethod
    def create_evolved(name: str) -> Pyrodon:
        return Pyrodon(name)


class AquaFactory(CreatureFactory):
    @staticmethod
    def create_base(name: str) -> Aquabub:
        return Aquabub(name)

    @staticmethod
    def create_evolved(name: str) -> Torragon:
        return Torragon(name)
