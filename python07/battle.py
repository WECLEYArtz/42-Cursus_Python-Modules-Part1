# Simple Import
from ex0 import FlameFactory, AquaFactory

# Lint Direct Import
from ex0.creatures import CreatureFactory


def testfactory(factory: CreatureFactory) -> None:
    base_pok = factory.create_base()
    print(base_pok.describe())
    print(base_pok.attack())

    eval_pok = factory.create_evolved()
    print(eval_pok.describe())
    print(eval_pok.attack())


def testbattle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")

    pok1 = factory1.create_base()
    pok2 = factory2.create_base()
    print(pok1.describe())
    print(" vs")
    print(pok2.describe())
    print(" fight!")

    print(pok1.attack())
    print(pok2.attack())


def main() -> None:
    flamefactory = FlameFactory()
    aquafactory = AquaFactory()

    print("Testing factory")
    testfactory(flamefactory)
    print()
    testfactory(aquafactory)
    print()
    testbattle(flamefactory, aquafactory)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
