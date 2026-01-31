class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name:      str = name
        self.height:    int = height
        self.age:       int = age

    def get_info(self):
        print(F"{self.name} ({self.__class__.__name__})", end=': ')
        print(F"{self.height}cm, {self.age} days", end=", ")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int,
                 clr: str) -> None:
        super().__init__(name, height, age)
        self.color = clr

    def bloom(self):
        print(F"{self.name} is blooming beautifully!")
        pass

    def get_info(self):
        Plant.get_info(self)
        print(self.color, "color")
        self.bloom()


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 td: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = td

    def produce_shade(self):
        print(F"{self.name} provides N square meters of shade")

    def get_info(self):
        Plant.get_info(self)
        print(F"{self.trunk_diameter}cm diameter")
        self.produce_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 hs: str, nv: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = hs
        self.nutritional_value: str = nv

    def get_info(self):
        Plant.get_info(self)
        print(F"{self.harvest_season} harvest")
        print(self.name, "is rich in", self.nutritional_value)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    plant_list: list[Plant] = []

    plant_list += [(Flower("Rose", 25, 30, "red"))]
    plant_list += [(Flower("Sakura", 25, 30, "pink"))]
    plant_list += [(Tree("Oak", 500, 1825, 50))]
    plant_list += [(Vegetable("Tomato", 80, 90, "summer", "vitamin C"))]

    for plant in plant_list:
        plant.get_info()
        print()

# $> python3 ft_plant_types.py
# === Garden Plant Types ===
# Rose (Flower): 25cm, 30 days, red color
# Rose is blooming beautifully!

# Oak (Tree): 500cm, 1825 days, 50cm diameter
# Oak provides 78 square meters of shade

# Tomato (Vegetable): 80cm, 90 days, summer harvest
# Tomato is rich in vitamin C
