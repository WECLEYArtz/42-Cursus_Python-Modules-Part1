class GardenError(Exception):
    def __init__(self, message: str):
        self.message: str = message

    def __str__(self) -> str:
        return (self.message)


class PlantError(GardenError):
    def __init__(self, message: str):
        self.message: str = message


class WaterError(GardenError):
    def __init__(self, message: str):
        self.message: str = message


def harvest_plants():
    raise PlantError("The tomato plant is wilting!")


def water_plants():
    raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    for title, operation in {
            "WaterError": harvest_plants,
            "PlantError": water_plants
            }.items():
        print(F"Testing {title}...")
        try:
            operation()
        except WaterError as error:
            print("Caught WaterError:", error)
            pass
        except PlantError as error:
            print("Caught PlantError:", error)
            pass
        print()

    print("Testing catching all garden errors...")
    for operation in [water_plants, harvest_plants]:
        try:
            operation()
        except GardenError as error:
            print("Caught a garden error:", error)
    print()
    print("All custom error types work correctly!")


# === Custom Garden Errors Demo ===
#
# Testing PlantError...
# Caught PlantError: The tomato plant is wilting!
#
# Testing WaterError...
# Caught WaterError: Not enough water in the tank!
#
# Testing catching all garden errors...
# Caught a garden error: The tomato plant is wilting!
# Caught a garden error: Not enough water in the tank!
#
# All custom error types work correctly!
