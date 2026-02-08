class InvalidValueError(Exception):
    def __init__(self, message) -> None:
        self.message: str = message

    def __str__(self) -> str:
        return ("Error: "+self.message)


class EmptyNameError(InvalidValueError):
    pass


class WaterLevelError(InvalidValueError):
    pass


class SunlightError(InvalidValueError):
    pass


def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    if not plant_name:
        raise EmptyNameError("Plant name cannot be empty!")

    if water_level > 10:
        raise WaterLevelError(
                F"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise WaterLevelError(
                F"Water level {water_level} is too low (min 0)")

    if sunlight_hours < 2:
        raise SunlightError(
                F"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise SunlightError(
                F"Sunlight hours {sunlight_hours} is too high (max 12)")
    print("Plant", plant_name, "is healthy!")


def test_plant_checks():
    tests = {
            "good values": ["tomato", 5, 5],
            "empty plant name": ["", 5, 5],
            "bad water level": ["tomato", 99, 5],
            "bad sunlight hours": ["tomato", 5, 0],
            }
    for title in tests:
        test = tests[title]
        print(F"Testing {title}...")
        try:
            check_plant_health(test[0], test[1], test[2])
        except (EmptyNameError, WaterLevelError, SunlightError) as error:
            print(error)
        print()
    print("All error raising tests completed!")


test_plant_checks()
