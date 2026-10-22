class Plant:

    class Statistics:

        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = round(height, 1) if height >= 0 else 0.0
        self._age = age if age >= 0 else 0
        self._stats = Plant.Statistics()

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = float(new_height)

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = new_age

    def grow(self, amount: float) -> None:
        self._height += amount
        self._stats._grow_calls += 1

    def age_day(self, days: int) -> None:
        self._age += days
        self._stats._age_calls += 1

    def show(self) -> None:
        self._stats._show_calls += 1
        word = "day" if self._age == 1 else "days"

        print(
            f"{self.get_name()}: "
            f"{round(self.get_height(), 1)}cm, "
            f"{self.get_age()} {word} old"
        )

    def get_stats(self):
        return self._stats

    @staticmethod
    def is_year_old(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False
        self._stats = Plant.Statistics()

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

    class TreeStats(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def extra_display(self):
            print(f"{self._shade_calls} shade")

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._stats = Tree.TreeStats()

    def produce_shade(self) -> None:
        self._stats._shade_calls += 1
        print(
            f"Tree {self.get_name()} now produces a shade of "
            f"{self.get_height()}cm long and "
            f"{self._trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.get_stats().display()
    

def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_year_old(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_year_old(400)}")

    print("\n=== Flower")

    rose = Plant("Rose", 15.0, 10, "red")

    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_statistics(rose)

if __name__ == "__main__":
    ft_garden_analytics()
