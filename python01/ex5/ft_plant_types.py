class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name:      str = name
        self.height:    int = height
        self.age:       int = age

    def get_info(self) -> None:
        print(F"{self.name} ({self.__class__.__name__})", end=': ')
        print(F"{self.height}cm, {self.age} days", end=", ")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, clr: str) -> None:
        super().__init__(name, height, age)
        self.color: str = clr

    def get_info(self) -> None:
        Plant.get_info(self)
        print(self.color, "color")
        self.bloom()

    def bloom(self) -> None:
        print(F"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, td: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = td

    def get_info(self) -> None:
        Plant.get_info(self)
        print(F"{self.trunk_diameter}cm diameter")
        self.produce_shade()

    def produce_shade(self) -> None:
        height = self.height
        print(F"{self.name} provides {(3.14 * ((height/100) **2)):.0f} square meters of shade")


class Vegetable(Plant):
    def __init__(self,
                 name: str, height: int, age: int, hs: str, nv: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = hs
        self.nutritional_value: str = nv

    def get_info(self) -> None:
        Plant.get_info(self)
        print(F"{self.harvest_season} harvest")
        print(self.name, "is rich in", self.nutritional_value)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    plant_list: list[Plant] = [
        (Flower("Rose", 25, 30, "red")),
        (Flower("Sakura", 25, 30, "pink")),
        (Tree("Oak", 500, 1825, 50)),
        (Tree("Boardleaf", 500, 1825, 50)),
        (Vegetable("Tomato", 80, 90, "summer", "vitamin C")),
        (Vegetable("Carrot", 80, 90, "spring", "vitamin C")),
    ]

    for plant in plant_list:
        plant.get_info()
        print()
