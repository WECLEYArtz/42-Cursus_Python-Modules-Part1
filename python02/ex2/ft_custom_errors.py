class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def harvest_plants() -> None:
    raise PlantError("The tomato plant is wilting!")


def water_plants() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    tests = {
        "PlantError": harvest_plants,
        "WaterError": water_plants
    }
    print("=== Custom Garden Errors Demo ===\n")
    for title in tests:
        print(F"Testing {title}...")
        try:
            tests[title]()
        except WaterError as error:
            print("Caught WaterError:", error)
        except PlantError as error:
            print("Caught PlantError:", error)
        print()

    print("Testing catching all garden errors...")
    for title in tests:
        try:
            tests[title]()
        except GardenError as error:
            print("Caught a garden error:", error)
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    try:
        test_custom_errors()
    except Exception as e:
        print("Unexcpecetd error", e)
