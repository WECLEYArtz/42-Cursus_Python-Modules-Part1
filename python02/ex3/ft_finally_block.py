class GardenError(Exception):
    pass


def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise GardenError(F"Cannot water {plant} - invalid plant!")
            print("Watering", plant)
    except GardenError as error:
        return (print("Error:", error))
    except TypeError as e:
        return (print("Error: Cannot water - Recieved wrong Type -", e))
    except Exception as e:
        return (print("Unexcpecetd error", e))
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print()

    print("Testing normal error...")
    water_plants(["tomato", None])
    print()

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
