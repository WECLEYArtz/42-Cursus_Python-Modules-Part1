from abc import ABC, abstractmethod
from typing import Any
from ex0.creatures import Creature
from ex1.capabilities import (
        HealCapability, TransformCapability,
        HealerProtocol, TransformerProtocol
        )


class BattleStrategy(ABC):
    @staticmethod
    @abstractmethod
    def is_valid(pokemon: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, pokemon: Creature) -> None:
        pass

class NormalStrategy(BattleStrategy):
    '''
    suitable for any Creature, that will simply use the attack method
    during the tournament'''
    @staticmethod
    def is_valid(pokemon: Any):
        return isinstance(pokemon, Creature)

    def act(self, pokemon: Creature) -> None:
        if self.is_valid(pokemon):
            print(pokemon.attack())
        else:
            raise ValueError(F"{pokemon} is not suitable for any strategy")


class DefensiveStrategy(BattleStrategy):
    '''
    suitable for Creature with healing capabilities,
    that will attack and then heal during the tournament
    '''
    @staticmethod
    def is_valid(pokemon: HealerProtocol):
        return isinstance(pokemon, (Creature, HealCapability))

    def act(self, pokemon: HealerProtocol) -> None:
        if self.is_valid(pokemon):
            print(pokemon.attack())
            print(pokemon.heal())
        else:
            raise ValueError(F"{pokemon} is not suitable for any defensive strategy")


class AggressiveStrategy(BattleStrategy):
    '''
    suitable for Creature with transform capabilities,
    that will transform, attack, and revert during the tournament
    '''
    @staticmethod
    def is_valid(pokemon: TransformerProtocol):
        return isinstance(pokemon, (Creature, TransformCapability))

    def act(self, pokemon: TransformerProtocol) -> None:
        if self.is_valid(pokemon):
            print(pokemon.transform())
            print(pokemon.attack())
            print(pokemon.revert())
        else:
            raise ValueError(F"{pokemon} is not suitable for any aggressive strategy")
