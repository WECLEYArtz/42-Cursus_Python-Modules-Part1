# Simple Import
from ex1 import HealingCreatureFactory, TransformCreatureFactory

# Lint Direct Import
from ex1.capabilities import (HealerProtocol, TransformerProtocol)


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


def main() -> None:
    pokemon1 = HealingCreatureFactory().create_base()
    pokemon2 = HealingCreatureFactory().create_evolved()
    test_heal_factory(pokemon1, pokemon2)
    print()

    pokemon3 = TransformCreatureFactory().create_base()
    pokemon4 = TransformCreatureFactory().create_evolved()
    test_transform_factory(pokemon3, pokemon4)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
