def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    print(F"{seed_type.capitalize()} seeds: ", end="")
    if (unit == "packets"):
        print(F"{quantity} packets available")
    elif (unit == "grams"):
        print(F"{quantity} grams total")
    elif (unit == "area"):
        print(F"covers {quantity} square meters")
    else:
        print(F"{quantity} Unknown unit type")
