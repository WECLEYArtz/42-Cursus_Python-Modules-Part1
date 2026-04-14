# Simple Import
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_heal_factory(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    p1 = factory.create_base()
    p2 = factory.create_evolved()

    print(" base:")
    print(p1.describe())
    print(p1.attack())
    print(p1.heal())

    print(" evolved:")
    print(p2.describe())
    print(p2.attack())
    print(p2.heal())


def test_transform_factory(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    p1 = factory.create_base()
    p2 = factory.create_evolved()

    print(" base:")
    print(p1.describe())
    print(p1.attack())
    print(p1.transform())
    print(p1.attack())
    print(p1.revert())

    print(" evolved:")
    print(p2.describe())
    print(p2.attack())
    print(p2.transform())
    print(p2.attack())
    print(p2.revert())


def main() -> None:
    healingfactory = HealingCreatureFactory()
    test_heal_factory(healingfactory)
    print()

    transformfactory = TransformCreatureFactory()
    test_transform_factory(transformfactory)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
