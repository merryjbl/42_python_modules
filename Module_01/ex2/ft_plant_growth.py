class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 0.8

    def age_day(self) -> None:
        self.age += 1

    def show(self) -> None:
        word = "day" if self.age == 1 else "days"
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} {word} old")


if __name__ == "__main__":
    def ft_plant_growth() -> None:
        print("=== Garden Plant Growth ===")
        rose = Plant("Rose", 25.0, 30)
        rose.show()
        initial_height = rose.height
        for day in range(1, 8):
            print(f"=== Day {day} ===")
            rose.grow()
            rose.age_day()
            rose.show()

        final_growth = round((rose.height - initial_height), 1)
        print(f"Growth this week: {final_growth}cm")
    ft_plant_growth()
