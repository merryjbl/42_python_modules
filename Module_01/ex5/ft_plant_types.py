class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height: float = 0
        else:
            self._height = height

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._age: int = 0
        else:
            self._age = age

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(new_height)
            print(f"Height updated: {new_height}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

    def grow(self) -> None:
        self._height += 2.1

    def age_day(self, days: int) -> None:
        self._age += days

    def show(self) -> None:
        word = "day" if self._age == 1 else "days"
        print(
            f"{self.get_name()}: "
            f"{round(self.get_height(), 1)}cm, "
            f"{self.get_age()} {word} old"
        )


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")

        if self._bloomed:
            print(f"{self.get_name()} is blooming beautifully!")
        else:
            print(f"{self.get_name()} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.get_name()} now produces a shade of "
            f"{self.get_height()}cm long and "
            f"{self._trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self) -> None:
        super().grow()
        self._nutritional_value = 1

    def age_day(self, days: int) -> None:
        super().age_day(days)
        self._nutritional_value += days - 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season. {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


def ft_plant_types() -> None:
    flower = Flower("Rose", 15.0, 10, "red")
    tree = Tree("Oak", 200.0, 365, 5.0)
    vegetable = Vegetable("Tomato", 5.0, 10, "April")

    print("=== Garden Plant Types ===")

    print("=== Flower")
    flower.show()
    print("[asking the rose to bloom]")
    flower.bloom()
    flower.show()

    print("\n=== Tree")
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()

    print("\n=== Vegetable")
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        vegetable.grow()
    vegetable.age_day(20)
    vegetable.show()


if __name__ == "__main__":
    ft_plant_types()
