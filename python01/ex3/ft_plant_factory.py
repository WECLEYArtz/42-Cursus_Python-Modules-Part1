class Plant():
    call_count = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name:      str = name
        self.height:    int = height
        self.age:       int = age
        print(F"Created: {self.name} ({self.height}cm, {self.age} days old)")
        Plant.call_count += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant_list: list[Plant] = []

    plant_list += [(Plant("Rose", 25, 30))]
    plant_list += [(Plant("Sunflower", 80, 45))]
    plant_list += [(Plant("Cactus", 15, 120))]
    plant_list += [(Plant("Tree", 100, 120))]
    plant_list += [(Plant("Weed", 15, 10))]
    print("Total plants created: ", Plant.call_count)
