def check_plant_health(
        plant_name: str, water_level: int, sunlight_hours: int) -> None:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level > 10:
        raise ValueError(
                F"Error: Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(
                F"Error: Water level {water_level} is too low (min 1)")

    if sunlight_hours > 12:
        raise ValueError(
                F"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
    if sunlight_hours < 2:
        raise ValueError(
                F"Error: Sunlight hours {sunlight_hours} is too low (min 2)")

    print("Plant", plant_name, "is healthy!")


def test_plant_checks() -> None:
    tests: dict[str, tuple[str, int, int]] = {
            "good values": ("tomato", 5, 5),
            "empty plant name": ("", 5, 5),
            "bad water level": ("tomato", 99, 5),
            "bad sunlight hours": ("tomato", 5, 0),
    }
    for title in tests:
        test = tests[title]
        print(F"Testing {title}...")
        try:
            check_plant_health(*test)
        except ValueError as error:
            print(error)
        except TypeError as error:
            print("Error: TypeError -", error)
        print()
    print("All error raising tests completed!")


test_plant_checks()
