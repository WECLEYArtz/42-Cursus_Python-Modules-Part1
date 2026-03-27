import alchemy

print("=== Sacred Scroll Mastery ===\n")

print("Testing direct module access:")
print("alchemy.elements.create_water():", alchemy.elements.create_water())
print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
print("alchemy.elements.create_air():", alchemy.elements.create_air())

print("\nTesting package-level access (controlled by __init__.py):")

print("alchemy.create_fire():",     alchemy.create_fire())
print("alchemy.create_water():",    alchemy.create_water())

print("alchemy.create_air():", end=' ')
try:
    alchemy.create_earth()
except AttributeError:
    print("AttributeError - not exposed")

print("alchemy.create_earth():", end=' ')
try:
    alchemy.create_air()
except AttributeError:
    print("AttributeError - not exposed")

print("\nPackage metadata:")
print("Version:", alchemy.__version__)
print("Author:", alchemy.__author__)
