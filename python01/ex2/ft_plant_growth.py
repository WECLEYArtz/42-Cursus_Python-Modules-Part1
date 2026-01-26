class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name_:      str = name
        self.height_:    int = height
        self.age_:       int = age

    def grow(self):
        self.height_ += 1

    def age(self):
        self.age_ += 1

    def get_info(self):
        print(F"{self.name_}: {self.height_}cm, {self.age_} days old")


def simulate_days(plant_list: list[Plant], days: int):
    for plant in plant_list:
        print("=== Day 1 ===")
        plant.get_info()

        height_old = plant.height_
        for _ in range(days):
            plant.grow()
            plant.age()
        print(F"=== Day {days+1} ===")
        plant.get_info()
        print(F"Growth this week: +{plant.height_ - height_old}cm")
        print()


if __name__ == "__main__":
    days = 6
    plant_list: list[Plant] = []

    plant_list += [Plant("Rose", 25, 30)]
    plant_list += [Plant("Sunflower", 80, 45)]
    plant_list += [Plant("Cactus", 15, 120)]

    simulate_days(plant_list, days)
