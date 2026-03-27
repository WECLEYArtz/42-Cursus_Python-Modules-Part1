def record_spell(spell_name: str, ingredients: str) -> str:
    from . import validator

    result: str = validator.validate_ingredients(ingredients)
    if "VALID" in result:
        return F"Spell recorded: {spell_name} ({result})"
    else:
        return F"Spell rejected: {spell_name} ({result})"
