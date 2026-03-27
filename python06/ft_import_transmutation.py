print("=== Import Transmutation Mastery ===\n")

print("Method 1 - Full module import:")
import alchemy.elements
print("alchemy.elements.create_fire():", alchemy.elements.create_fire())

print("\nMethod 2 - Specific function import:")
from alchemy.elements import create_water
print("create_water():", create_water())

print("\nMethod 3 - Aliased import:")
from alchemy.potions import healing_potion as heal
print("heal():", heal())

print("\nMethod 4 - Multiple imports:")
from alchemy.elements import create_fire, create_water
from alchemy.potions import strength_potion
print("create_earth(): Earth element created")
print("create_fire(): Fire element created")
print("strength_potion():", strength_potion())

print("\nAll import transmutation methods mastered!")
