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

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print("Invalid operation attempted:", end=' ')
            print(F"height, {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height: int = new_height
        print(F"Height updated: {self._height}cm [OK]")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print("Invalid operation attempted:", end=' ')
            print(F"age, {new_age}cm [REJECTED]")
            print("Security: Negative age rejected")
            return
        self._age: int = new_age
        print(F"Age updated: {self._age} days [OK]")

    def get_height(self) -> None:
        print(self._height)

    def get_age(self) -> None:
        print(self._age)

    def get_info(self) -> None:
        print(F"Current: {self.name} ({self._height}cm, {self._age} days)")


def main():
    print("=== Garden Security System ===")
    a = SecurePlant("Rose", 25, 30)
    print()
    a.set_height(-5)
    print()
    a.get_info()


if __name__ == "__main__":
    main()
