from typing import Any, Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combine(*args: Any, **kwargs: Any) -> tuple[str, str]:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combine


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplify(target: str, power: int) -> str:
        return (base_spell(target, power * multiplier))
    return amplify


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast(*args, **kwags):
        if condition(*args, **kwags):
            return spell(*args, **kwags)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def seq(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]
    return seq


def main():
    # == Testing Spells =======================================================
    def fire_spell(target: str, power: int):
        return f"Fireball hits {target} for {power} HP"

    def heal_spell(target: str, power: int):
        return f"Heals {target} for {power} HP"

    # == Tests ================================================================
    print("Testing spell combiner...")

    combiner = spell_combiner(fire_spell, heal_spell)
    print(f"Combined spell result: {', '.join(combiner('dragon', 10))}")

    normal_spell = fire_spell
    amplified_spell = power_amplifier(fire_spell, 3)

    print()
    print(f"Original: {normal_spell('dragon',10)}\n" +
          f"Amplified: {amplified_spell('dragon',10)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
