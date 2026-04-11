from ex0 import FlameFactory, AquaFactory
from ex0.creatures import Creature


def testfactory(p1: Creature, p2: Creature) -> None:
    print("Testing factory")
    print(p1.describe())
    print(p1.attack())

    print(p2.describe())
    print(p2.attack())


def testbattle(p1: Creature, p2: Creature) -> None:
    print("Testing battle")
    print(p1.describe())
    print(" vs")
    print(p2.describe())
    print(" fight!")

    print(p1.attack())
    print(p2.attack())


if __name__ == "__main__":
    flamefactory = FlameFactory()
    aquafactory = AquaFactory()

    pokemon1 = FlameFactory.create_base("Flameling")
    pokemon2 = FlameFactory.create_evolved("Pyrodon")
    testfactory(pokemon1, pokemon2)

    print()

    pokemon3 = AquaFactory.create_base("Aquabub")
    pokemon4 = AquaFactory.create_evolved("Torragon")
    testfactory(pokemon3, pokemon4)

    print()

    testbattle(pokemon1, pokemon3)
