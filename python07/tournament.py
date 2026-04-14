from itertools import combinations

# Simple Import
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (NormalStrategy, DefensiveStrategy, AggressiveStrategy)

# Lint Direct Import
from ex0.creatures import CreatureFactory
from ex2.strategies import BattleStrategy


def battle(oponents: list[tuple[CreatureFactory, BattleStrategy]]):
    print("*** Tournament ***")
    print(len(oponents), "opponents involved")

    rounds = list(combinations(range(len(oponents)), 2))

    for round in rounds:
        oponent1 = oponents[round[0]]
        oponent2 = oponents[round[1]]

        pok1_card, pok1_strat = oponent1[0].create_base(), oponent1[1]
        pok2_card, pok2_strat = oponent2[0].create_base(), oponent2[1]

        print("\n* Battle *")
        print(pok1_card.name, pok1_card.describe())
        print(" vs")
        print(pok2_card.name, pok2_card.describe())
        print(" now fight!")

        pok1_strat.act(pok1_card)
        pok2_strat.act(pok2_card)


if __name__ == "__main__":
    # == Tournament 0 (basic) ================================================
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    fighters = [(FlameFactory, NormalStrategy()),
                (HealingCreatureFactory, DefensiveStrategy())]
    try:
        battle(fighters)
    except ValueError as e:
        print("Battle error, aborting tournament: ", e)
    print()

    # == Tournament 1 (error) ================================================
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    fighters = [(FlameFactory, AggressiveStrategy()),
                (HealingCreatureFactory, DefensiveStrategy())]
    try:
        battle(fighters)
    except ValueError as e:
        print("Battle error, aborting tournament: ", e)
    print()

    # == Tournament 2 (multiple) =============================================
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    fighters = [(AquaFactory, NormalStrategy()),
                (HealingCreatureFactory, DefensiveStrategy()),
                (TransformCreatureFactory, AggressiveStrategy())]
    try:
        battle(fighters)
    except ValueError as e:
        print("Battle error, aborting tournament: ", e)
    print()
