from python07.ex0.creatures import CreatureFactory
from python07.ex2.battle import BattleStrategy


def battle(oponents: list[tuple[CreatureFactory, BattleStrategy]]):


    rounds: int = len(oponents)

    print("*** Tournament ***")
    print(len(oponents), "opponents involved")

    while (rounds):
        pok1_factory, pok1_strat = oponents[rounds % 2]
        pok2_factory, pok2_strat = oponents[rounds % 2]

        pok1_card = pok1_factory.create_base()
        pok2_card = pok2_factory.create_base()

        pok1_strat.act(pok1_card)
        pok2_strat.act(pok2_card)
        rounds =- 1

if __name__ = "__main__":
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle



    
# Tournament 0 (basic)
# [ (Flameling+Normal), (Healing+Defensive) ]
# *** Tournament ***
# 2 opponents involved
# * Battle *
# Flameling is a Fire type Creature
# vs.
# Sproutling is a Grass type Creature
# now fight!
# Flameling uses Ember!
# Sproutling uses Vine Whip!
# Sproutling heals itself for a small amount


# Tournament 1 (error)
# [ (Flameling+Aggressive), (Healing+Defensive) ]
# *** Tournament ***
# 2 opponents involved
# * Battle *
# Flameling is a Fire type Creature
# vs.
# Sproutling is a Grass type Creature
# now fight!
# Battle error, aborting tournament: Invalid Creature 'Flameling' for this aggressive strategy
# Tournament 2 (multiple)
# [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]
# *** Tournament ***
# 3 opponents involved
# * Battle *
# Aquabub is a Water type Creature
# vs.
# Sproutling is a Grass type Creature
# now fight!
# Aquabub uses Water Gun!
# Sproutling uses Vine Whip!
# Sproutling heals itself for a small amount
# * Battle *
# Aquabub is a Water type Creature
# vs.
# Shiftling is a Normal type Creature
# now fight!
# Aquabub uses Water Gun!
# Shiftling shifts into a sharper form!
# Shiftling performs a boosted strike!
# Shiftling returns to normal.
# * Battle *
# Sproutling is a Grass type Creature
# vs.
# Shiftling is a Normal type Creature
# now fight!
# Sproutling uses Vine Whip!
# Sproutling heals itself for a small amount
# Shiftling shifts into a sharper form!
# Shiftling performs a boosted strike!
# Shiftling returns to normal.
