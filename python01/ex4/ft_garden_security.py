class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        print(F"Plant created:: {self.name}")
        self.set_height(height)
        if height < 0:
            self.set_height(0)
        self.set_age(age)
        if age < 0:
            self.set_age(0)

    def set_height(self, new_height: int):
        if new_height < 0:
            print(F"Invalid operation attempted: height, {new_height}cm [REJECTED]")
            print(F"Security: Negative height rejected")
            self.get_info()
            return
        self._height: int = new_height
        print(F"Height updated: {self._height}cm [OK]")


    def set_age(self, new_age: int):
        if new_age < 0:
            print(F"Invalid operation attempted: age, {new_age} days [REJECTED]")
            print(F"Security: Negative age rejected")
            self.get_info()
            return
        self._age: int = new_age
        print(F"Age updated: {self._age} days [OK]")
        print(F"Security: Negative age rejected")

    def get_height(self):
        print(self._height)

    def get_age(self):
        print(self._age)

    def get_info(self):
        print()
        print(F"Current: {self.name} ({self._height}cm, {self._age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    a = SecurePlant("Rose", 25, 30)
    print()
    a.set_height(-5)
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
