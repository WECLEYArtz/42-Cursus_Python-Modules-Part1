def rec(day_max: int, day):
    if (day <= day_max):
        print("Day", day)
        rec(day_max, day+1)
    return


def ft_count_harvest_recursive() -> None:
    day_max = int(input("Days until harvest: "))
    rec(day_max, 1)
    print("Harvest time!")
