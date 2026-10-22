class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name

        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height: float = 0
        else:
            self._height = height

        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            self._age: int = 0
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(new_height)
            print(f"Height updated: {new_height}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

    def show(self) -> None:
        word = "day" if self._age == 1 else "days"
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._age} {word} old")


if __name__ == "__main__":
    def ft_garden_security() -> None:
        print("=== Garden Security System ===")
        rose = Plant("Rose", 15.0, 10)
        print("Plant created:", end=" ")
        rose.show()

        rose.set_height(25)
        rose.set_age(30)

        rose.set_height(-5)
        rose.set_age(-20)
        print("Current state:", end=" ")
        rose.show()
    ft_garden_security()
