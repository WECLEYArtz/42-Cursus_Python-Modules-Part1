class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    plant_list = []
    plant_list += [(Plant("Rose", 25, 30))]
    plant_list += [(Plant("Sunflower", 80, 45))]
    plant_list += [(Plant("Cactus", 15, 120))]
    for plant in plant_list:
        print(F"{plant.name}: {plant.height} cm {plant.age} days old")


# $> python3 ft_garden_data.py
# === Garden Plant Registry ===
# Rose: 25cm, 30 days old
# Sunflower: 80cm, 45 days old
# Cactus: 15cm, 120 days old
