from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleStrategy():
    @abstractmethod
    def is_valid() -> bool:
        pass

    def act():
        pass

class NormalStrategy(BattleStrategy):
    '''
    suitable for any Creature, that will simply use the attack method
    during the tournament'''
    def is_valid(pokemon1: Any, pokemon2: Any):
        if not(  isinstance() and isinstance())

class AggressiveStrategy(BattleStrategy):
    '''
    suitable for Creature with transform capabilities,
    that will transform, attack, and revert during the tournament
    '''

class DefensiveStrategy(BattleStrategy)
    '''
    suitable for Creature with healing capabilities,
    that will attack and then heal during the tournament
    '''
