class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.score: int = 0
        self.set_height(height)
        if height < 0:
            self.set_height(0)

    def set_height(self, new_height: int):
        if (GardenManager.GardenStats.height_validation and new_height < 0):
            print(F"[Warning]: Invalid height given: {new_height}cm.")
            print("           Using 0cm instead")
            new_height = 0
            print()
        self._height: int = new_height

    def get_height(self):
        return self._height

    def get_info(self) -> str:
        return (F"{self.name}: {str(self._height)}cm")

    def show_info(self) -> None:
        print(self.get_info())

    def grow(self):
        self._height += 1
        print(F"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        self._color: str = color
        super().__init__(name, height)

    def get_info(self) -> str:
        return (Plant.get_info(self) + F", {self._color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        self.prize: int = prize
        super().__init__(name, height, color)

    def get_info(self) -> str:
        return (FloweringPlant.get_info(self) +
                F", Prize flowers: {self.prize}")


class GardenManager:
    class Garden():
        def __init__(self, owner: str):
            self.owner: str = owner
            self._plants: list[Plant | FloweringPlant | PrizeFlower] = []
            self._count: dict[str, int] = {
                "Plant": 0,
                "PrizeFlower": 0,
                "FloweringPlant": 0,
            }
            self._total_added: int = 0
            self._total_growth: int = 0
      
        def get_plants(self):
            return self._plants

        def append_plant(self,
                         plant: Plant | FloweringPlant | PrizeFlower):
            self._plants += [plant]
            self._count[plant.__class__.__name__] += 1
            self._total_added += 1
            GardenManager.GardenStats.score[self.owner] += plant.get_height()
            if (plant.__class__.__name__ == 'PrizeFlower'):
                GardenManager.GardenStats.score[self.owner] += plant.prize
            print(F"Added {plant.name} to {self.owner}'s garden")

        def grow_all(self) -> None:
            print(F"{self.owner} is helping all plants grow...")
            for plant in self._plants:
                plant.grow()
                self._total_growth += 1
                GardenManager.GardenStats.score[self.owner] += 1

        def report(self):
            print(F"=== {self.owner} Garden Report ===")
            for plant in self._plants:
                print(F"- {plant.get_info()}")
            print()
            print(F"Plants added: {self._total_added}", end=', ')
            print(F"Total growth: {self._total_growth}cm")
            print("Plant types:", end=' ')
            print(F"{self._count['Plant']} regular", end=', ')
            print(F"{self._count['PrizeFlower']} flowering", end=', ')
            print(F"{self._count['FloweringPlant']} prize flowers")

    @classmethod
    def create_garden_network(cls, owner: str) -> None:
        if owner not in cls.gardens:
            cls.gardens[owner] = cls.Garden(owner)
            cls.GardenStats.gardens_count += 1
            cls.GardenStats.score[owner] = 0
        else:
            print("Error: attempted to add already existing owner:", owner)

    @classmethod
    def add_plant(cls, owner: str,
                  plant: Plant | FloweringPlant | PrizeFlower):
        if owner not in cls.gardens:
            print("Error: no garden asigned for", owner)
            return
        plants = cls.gardens[owner].get_plants()
        if plant in plants:
            print("Error: can't add same existing plant")
            return
        cls.gardens[owner].append_plant(plant)

    @classmethod
    def get_garden(cls, owner: str) -> Garden | None:
        if owner in cls.gardens:
            return cls.gardens[owner]
        else:
            return None

    gardens: dict[str, Garden] = {}

    class GardenStats():
        height_validation: bool = True
        score: dict[str, int] = {}
        gardens_count: int = 0

        @classmethod
        def toggle_height_validation(cls):
            cls.height_validation = False if cls.height_validation else True

        @classmethod
        def show(cls):
            print("Height validation test: ", cls.height_validation)
            print(F"Garden scores: - {cls.format_scores(cls.score)}")
            print(F"Total gardens managed: {cls.gardens_count}")

        @staticmethod
        def format_scores(score: dict[str, int]) -> str:
            result: str = ""
            for key in score:
                result += F"{key}: {score[key]}, "
            return result[:-2]


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    GardenManager.create_garden_network("Alice")
    GardenManager.create_garden_network("Bob")
    print()
    GardenManager.add_plant("Alice", Plant("Oak Tree", 101))
    GardenManager.add_plant("Alice", FloweringPlant("Rose", 10, "red"))
    GardenManager.add_plant("Alice",
                            PrizeFlower("Sunflower", 100, "yellow", 10))
    GardenManager.add_plant("Bob", Plant("Oak Tree", 92))
    print()
    alice_garden = GardenManager.get_garden('Alice')
    if (alice_garden):
        alice_garden.grow_all()
        print()
        alice_garden.report()
    print()
    GardenManager.GardenStats.show()
    GardenManager.GardenStats.toggle_height_validation()
    GardenManager.GardenStats.show()
