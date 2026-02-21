def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    message: str
    if (unit == "packets"):
        message = F"{quantity} packets available"
    elif (unit == "grams"):
        message = F"{quantity} grams total"
    elif (unit == "area"):
        message = F"covers {quantity} square meters"
    else:
        print("Unknown unit type")
        return
    print(F"{seed_type.capitalize()} seeds:", message)
