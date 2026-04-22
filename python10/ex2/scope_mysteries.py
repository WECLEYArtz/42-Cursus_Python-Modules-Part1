from typing import Any, Callable


def mage_counter() -> Callable:
    count: int = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total: int = initial_power

    def accumulator(amount: int):
        nonlocal total
        total += amount
        return total
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchanted(item: str):
        return (f"{enchantment_type} {item}")
    return enchanted


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: Any, value: Any) -> None:
        memory[key] = value

    def recall(key: Any) -> Any | None:
        return (memory.get(key, "Memory not found"))
    return {'store': store, 'recall': recall}


def main():
    # == Test 0 ===============================================================
    print("Testing mage counter...")

    counter = mage_counter()
    for n in range(1, 3):
        print(f"counter_a call {n}:", counter())
    print("counter_b call 1:", mage_counter()())
    print()

    # == Test 1 ===============================================================
    print("Testing spell accumulator...")
    base = 100
    accumulator = spell_accumulator(base)
    print(F"Base {base}, add 20: {accumulator(20)}")
    print(F"Base {base}, add 30: {accumulator(30)}")
    print()

    # == Test 2 ===============================================================
    print("Testing enchantment factory...")
    print(enchantment_factory('Flaming')("Sword"))
    print(enchantment_factory('Frozen')("Shield"))
    print()

    # == Test 3 ===============================================================
    print("Testing memory vault...")

    mem_vault = memory_vault()

    print("Store 'secret' = 42")
    mem_vault['store']('secret', 42)

    print("Recall 'secret' =", mem_vault['recall']('secret'))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
