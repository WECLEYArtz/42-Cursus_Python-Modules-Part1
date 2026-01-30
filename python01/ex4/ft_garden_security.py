class SecurePlant:
    def __new__(cls, height: int, age: int) -> None:
        if height < 0:
            return None
        if age < 0:
            return None
        return SecurePlant.__new__(cls, height, age)

    def __init__(self, height: int, age: int) -> None:
        if self is None:
            return
        self._height:    int = height
        self._age:       int = age

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
    a = SecurePlant(1, 1)
    if a:
        print(a.get_height())
        print(a.get_age())
    else:
        print(a)

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
