from elements import create_fire, create_water
from .elements import create_air, create_earth

def healing_potion() -> str:
    return ("Healing potion brewed with "
          f"’{create_earth()}’ and "
          f"’{create_air()}'")


def strength_potion() -> str:
    return ("Strength potion brewed with "
          f"’{create_fire()}’ and "
          f"’{create_water()}")
