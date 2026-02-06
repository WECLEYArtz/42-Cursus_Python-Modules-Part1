class PlantError(Exception):
    def __init__(self, message: str):
        self.message: str = message


def water_plants(plant_list: list[str]):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise PlantError("invalid plant!")
            print("Watering", plant)
    except PlantError as error:
        print("Error: Cannot water None -", error.message)
        return
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")


def test_watering_system():
    print("=== Garden Watering System ===")
    print("Testing normal watering...")
    try:
        water_plants(["tomato", "lettuce", "carrots"])
    except PlantError:
        pass
    print()
    print("Testing normal error...")
    try:
        water_plants(["tomato", None])
    except PlantError:
        pass
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()

# === Garden Watering System ===
#
# Testing normal watering...
# Opening watering system
# Watering tomato
# Watering lettuce
# Watering carrots
# Closing watering system (cleanup)
# Watering completed successfully!
#
# Testing with error...
# Opening watering system
# Watering tomato
# Error: Cannot water None - invalid plant!
# Closing watering system (cleanup)
#
# Cleanup always happens, even with errors!
