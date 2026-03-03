class GardenError(Exception):
    def __init__(self, message: str):
        self.message: str = message


def water_plants(plant_list: list[str]):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise GardenError("Cannot water None - invalid plant!")
            print("Watering", plant)
    except GardenError as error:
        print("Error:", error.message)
        return
    except TypeError as e:
        print("Error: Cannot water - Recieved wrong Type -", e)
        return
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")


def test_watering_system():
    print("=== Garden Watering System ===")
    print()

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print()

    print("Testing normal error...")
    water_plants(["tomato", None])
    print()

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
