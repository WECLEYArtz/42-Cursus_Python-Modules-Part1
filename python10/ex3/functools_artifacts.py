from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    match operation:
        case "add":
            return (reduce(add, spells))
        case "multiply":
            return (reduce(mul, spells))
        case "max":
            return (max(spells))
        case "min":
            return (min(spells))
        case _:
            raise ValueError(f"'{operation}' is not a valid operation")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    enchantments: dict[str, Callable] = {
            'fire': partial(base_enchantment, power=50, element='fire'),
            'wind': partial(base_enchantment, power=50, element='wind'),
            'earth': partial(base_enchantment, power=50, element='earth')
            }
    return enchantments


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Preferably None negative values for fibunacci")
    if (n < 2):
        return n
    return (memoized_fibonacci(n-1) + memoized_fibonacci(n-2))


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def func(value: Any) -> str:
        return "Unknown spell type"

    @func.register(int)
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @func.register(str)
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @func.register(list)
    def _(value: list[Any]) -> str:
        return f"Multi-cast: {len(value)} spells"
    return func


def main():
    # == Test 0 ===============================================================
    print("Testing spell reducer...")

    spell_powers = [25, 25, 25, 25]
    print("Sum:", spell_reducer(spell_powers, 'add'))

    spell_powers = [24, 10, 10, 10, 10]
    print("Product:", spell_reducer(spell_powers, 'multiply'))

    spell_powers = [24, 1, 12, 40, 10]
    print("Max:", spell_reducer(spell_powers, 'max'))

    # print(memoized_fibonacci.cache_info())
    print(memoized_fibonacci(100))

    # == Test 1 ===============================================================
    print("\nTesting memoized fibonacci...")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}):", memoized_fibonacci(n))

    print("\nTesting spell dispatcher...")

    # == Test 2 ===============================================================
    spell_dp = spell_dispatcher()
    print(spell_dp(42))
    print(spell_dp("fireball"))
    print(spell_dp(['fire', 'earth', 'semen']))
    print(spell_dp(0.1))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
