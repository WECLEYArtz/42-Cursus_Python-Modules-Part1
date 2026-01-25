def ft_count_harvest_iterative():
    day_max = int(input("Days until harvest: "))
    day = 1
    while day <= day_max:
        print(F"Day {day}")
        day += 1
    print("Harvest time!")
