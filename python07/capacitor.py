from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0.creatures import Creature
from ex1.capabilities import (HealCapability, HealerProtocol,
                              TransformCapability, TransformerProtocol)


def test_heal_factory(p1: HealerProtocol,
                      p2: HealerProtocol) -> None:
    print("Testing Creature with healing capability")

    print(" base:")
    print(p1.describe())
    print(p1.attack())
    print(p1.heal())

    print(" evolved:")
    print(p2.describe())
    print(p2.attack())
    print(p2.heal())


def test_transform_factory(p1: TransformerProtocol,
                           p2: TransformerProtocol) -> None:
    print("Testing Creature with transform capability")

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


if __name__ == "__main__":
    healingcreaturefactory = HealingCreatureFactory()
    transformcreaturefactory = TransformCreatureFactory()

    pokemon1 = healingcreaturefactory.create_base("Sproutling")
    pokemon2 = healingcreaturefactory.create_evolved("Bloomelle")
    test_heal_factory(pokemon1, pokemon2)
    print()

    pokemon3 = transformcreaturefactory.create_base("Shiftling")
    pokemon4 = transformcreaturefactory.create_evolved("Morphagon")
    test_transform_factory(pokemon3, pokemon4)
