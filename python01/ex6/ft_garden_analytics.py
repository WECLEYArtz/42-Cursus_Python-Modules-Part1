from typing import override


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.score: int = 0
        self.set_height(height)
        if height < 0:
            self.set_height(0)

    def set_height(self, new_height: int):
        if new_height < 0:
            print("Invalid operation attempted:", end=' ')
            print(F"height, {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
            self.show_info()
            return
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

    @override
    def get_info(self) -> str:
        return (Plant.get_info(self) + F" {self._color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str) -> None:
        self.prize: int = 0
        super().__init__(name, height, color)

    @override
    def get_info(self) -> str:
        return (FloweringPlant.get_info(self) + F" {self.prize} prize flowers")


class GardenManager:

    def append_plant(self,
                     plant: Plant | FloweringPlant | PrizeFlower):
        self._plants += [plant]
        self._count[plant.__class__.__name__] += 1
        self._total_added += 1
        GardenManager.GardenStats.score[self.owner] += plant.get_height()
        print(F"Added {plant.name} to {self.owner}'s garden")

    @classmethod
    def grow_all(cls, owner: str) -> None:
        print(F"{owner} is helping all plants grow...")
        for plant in cls.gardens[owner]:
            plant.grow()
            cls._total_growth += 1


    @classmethod
    def report(cls, ownr: str):
        print(F"=== {ownr} Garden Report ===")
        for plant in cls.gardens:
            print(F"- {plant.get_info()}")
        print()
        print(F"Plants added: {self._total_added}", end=', ')
        print(F"Total growth: {self._total_growth}cm")
        print("Plant types:", end=' ')
        print(F"{self._count["Plant"]} regular", end=', ')
        print(F"{self._count["PrizeFlower"]} flowering", end=', ')
        print(F"{self._count["FloweringPlant"]} prize flowers")

    @classmethod
    def get_garden(cls,
                   ownr: str) -> list[Plant | FloweringPlant | PrizeFlower]:
        return cls.gardens[ownr]

    @classmethod
    def create_garden_network(cls, owner: str) -> None:
        if owner not in cls.gardens:
            cls.gardens[owner] = []
            cls.gardens_count += 1
        else:
            print("Error: attempted to add already existing owner:", owner)

    @classmethod
    def add_plant(cls, ownr: str, plant: Plant | FloweringPlant | PrizeFlower):
        if ownr not in cls.gardens:
            print("Error: no garden asigned for", ownr)
            return
        cls.gardens[ownr] += [plant]

    class GardenStats():
        @classmethod
        def show(cls):
            print("Height validation test: ", GardenManager.height_validation)
            print("Garden scores: ", end='')
            # if(cls.height_validation):
            #     cls.calculate_score()   
            # else:
            print(F"Total gardens managed: {GardenManager.gardens_count}")

        @classmethod
        def calculate_score(cls) -> int:
            cls.gardens

        @classmethod
        def calculate_score_valid(garden: Garden) -> int:
            pass

    gardens: dict[str, list[Plant | FloweringPlant | PrizeFlower]] = {}
    gardens_count: int = 0
    height_validation: bool = True

    @classmethod
    def toggle(cls) -> None:
        cls.height_validation = False if cls.height_validation else True


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    GardenManager.create_garden_network("Alice")
    GardenManager.create_garden_network("Bob")
    print()
    GardenManager.add_plant("Alice", Plant("Oak Tree", 101))
    GardenManager.add_plant("Alice", FloweringPlant("Rose", 10, "red"))
    GardenManager.add_plant("Alice", PrizeFlower("Sunflower", 9999, "yellow"))
    print()
    GardenManager.GardenStats.show()
