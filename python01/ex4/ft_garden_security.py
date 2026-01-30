class SecurePlant:
    _height: int = 0
    _age: int = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.set_age(age)
        self.set_height(height)
        print(F"Created: {self.name} ({self._height}cm, {self._age} days old)")

    def set_height(self, new_height: int):
        if new_height < 0:
            print(F"Invalid operation attempted: height, {new_height}cm [REJECTED]")
            return
        self._height:    int = new_height

    def set_age(self, new_age: int):
        if new_age < 0:
            print(F"Invalid operation attempted: age, {new_age} days [REJECTED]")
            return
        self._age:       int = new_age

    def get_height(self):
        print(self._height)

    def get_age(self):
        print(self._age)


if __name__ == "__main__":
    print("=== Garden Security System ===")
    a = SecurePlant("rose", -1, 1)
    print(a.name)
    a.get_height()
    a.get_age()
    # print(a.get_age())

    # print("plant attribute", plant.__dict__)
    # print(plant.get_age(), plant.get_height())


# Example:
# $> python3 ft_garden_security.py
# === Garden Security System ===
# Plant created: Rose
# Height updated: 25cm [OK]
# Age updated: 30 days [OK]
#
# Invalid operation attempted: height -5cm [REJECTED]
# Security: Negative height rejected
#
# Current plant: Rose (25cm, 30 days)
