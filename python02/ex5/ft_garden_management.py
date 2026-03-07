class GardenError(Exception):
    pass


class WaterError(GardenError):
    pass


class HealthError(GardenError):
    pass


class Plant():
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name:      str = name
        self.water_level:    int = water
        self.sun_level:       int = sun

    def water(self) -> None:
        self.water_level += 1

    def sun(self) -> None:
        self.sun_level += 1


class GardenManager:
    def __init__(self) -> None:
        self.garden: list[Plant] = []
        self.water_tank: int = 2

    def add_plants(self, plants: list[Plant]) -> None:
        for plant in plants:
            try:
                if not plant.name:
                    raise ValueError(
                            "Error adding plant: Plant name cannot be empty!")
                self.garden.append(plant)
            except (ValueError) as e:
                print(e)
            else:
                print("Added", plant.name, "successfully")

    def water_plants(self) -> None:
        print("Watering plants...")
        self.open_water_system()
        try:
            for plant in self.garden:
                print(F"Watering {plant.name}", end=' - ')
                if not self.water_tank:
                    raise WaterError(
                            "Error watering plants: Not enough water in tank")
                self.water_tank -= 1
                plant.water()
                print("success")
        except WaterError as e:
            print("failed")
            print(e)
        finally:
            self.close_water_system()

    def open_water_system(self) -> None:
        print("Opening watering system")

    def close_water_system(self) -> None:
        print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        print("Checking plant health...")
        for plant in self.garden:
            if plant.water_level > 10:
                raise HealthError(
                    F"Error checking {plant.name}: " +
                    F"Water level {plant.water_level} is too high (max 10)")
            if plant.water_level < 1:
                raise HealthError(
                    F"Error checking {plant.name}: " +
                    F"Water level {plant.water_level} is too low (min 1)")
            if plant.sun_level > 12:
                raise HealthError(
                    F"Error checking {plant.name}: " +
                    F"Water level {plant.sun_level} is too high (max 12)")
            if plant.sun_level < 2:
                raise HealthError(
                    F"Error checking {plant.name}: " +
                    F"Water level {plant.sun_level} is too low (min 2)")
            print(F"{plant.name}: healthy", end=' ')
            print(F"(water: {plant.water_level}, sun: {plant.sun_level})")

    def recovery_test(self) -> None:
        print("Testing error recovery...")
        try:
            if self.water_tank == 0:
                raise WaterError(
                        "Caught GardenError: Not enough water in tank")
        except GardenError as e:
            print(e)
            print("System recovered and continuing...")


def test_garden_management() -> None:
    try:
        print("=== Garden Management System ===\n")
        garden = GardenManager()

        print("Adding plants to garden...")
        garden.add_plants([
            Plant("tomato", 4, 8),
            Plant("lettuce", 14, 8),
            Plant("", 4, 8),
        ])
        print()

        garden.water_plants()
        print()

        try:
            garden.check_plant_health()
        except HealthError as e:
            print(e)
        finally:
            print()

        garden.recovery_test()
        print()

        print("Garden management system test complete!")
    except Exception as e:
        print("Caught Error:", e)


if __name__ == "__main__":
    test_garden_management()
