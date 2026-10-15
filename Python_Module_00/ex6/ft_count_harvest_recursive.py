def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))

    def count_days(i: int) -> None:
        if i > days:
            print("Harvest time!")
            return
        print(f"Day {i}")
        count_days(i + 1)
    count_days(1)
