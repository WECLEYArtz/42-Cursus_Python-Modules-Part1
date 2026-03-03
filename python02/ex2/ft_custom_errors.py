class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def harvest_plants():
    raise PlantError("The tomato plant is wilting!")


def water_plants():
    raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    tests = {
        "WaterError": harvest_plants,
        "PlantError": water_plants
    }
    print("=== Custom Garden Errors Demo ===")
    for title in tests:
        print(F"Testing {title}...")
        try:
            tests[title]()
        except WaterError as error:
            print("Caught WaterError:", error)
            pass
        except PlantError as error:
            print("Caught PlantError:", error)
            pass
        print()

    print("Testing catching all garden errors...")
    for title in tests:
        try:
            tests[title]()
        except GardenError as error:
            print("Caught a garden error:", error)
    print()
    print("All custom error types work correctly!")
