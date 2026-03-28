from alchemy.grimoire import validate_ingredients, spellbook, record_spell


def print_validation(ingredient: str):
    result: str = validate_ingredients(ingredient)
    print(F'validate_ingredients({ingredient}):', result)


def print_record(spell_name: str, ingredient: str):
    result: str = spellbook(spell_name, ingredient)
    print(F'validate_ingredients({ingredient}):', result)


print("=== Circular Curse Breaking ===")

print("\nTesting ingredient validation:")

print_validation("fire air")
print_validation("dragon scales")

print("\nTesting spell recording with validation:")

print('record_spell("Fireball", "fire air"):',
      record_spell("Fireball", "fire air"))
print('record_spell("Dark Magic", "shadow"):',
      record_spell("Dark Magic", "shadow"))


print("\nTesting late import technique:")
print('record_spell("Lightning", "air"):', record_spell("Lightning", "air"))

print("\nCircular dependency curse avoided using late imports!")
print("All spells processed safely!")
