from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients2(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    ingredient_list = ingredients.replace(" and ", " ").replace(", ", " ")
    for ingredient in ingredient_list.split():
        if ingredient not in allowed:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
