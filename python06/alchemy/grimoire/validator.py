def validate_ingredients(ingredients: str) -> str:
    ingredients_list = ingredients.split()
    valid_list = ["fire", "water", "earth", "air"]

    for ing in ingredients_list:
        if ing not in valid_list:
            return F"{ingredients} - INVALID"
    return F"{ingredients} - VALID"
