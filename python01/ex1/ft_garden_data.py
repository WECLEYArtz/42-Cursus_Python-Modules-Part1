class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name_:      str = name
        self.height_:    int = height
        self.age_:       int = age


if __name__ == "__main__":
    plant_list: list[Plant] = []

    plant_list += [Plant("Rose", 25, 30)]
    plant_list += [Plant("Sunflower", 80, 45)]
    plant_list += [Plant("Cactus", 15, 120)]

    print("=== Garden Plant Registry ===")
    for plant in plant_list:
        print(F"{plant.name_}: {plant.height_}cm, {plant.age_} days old")
