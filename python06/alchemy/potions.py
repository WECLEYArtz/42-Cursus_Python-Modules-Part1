def healing_potion() -> str:
    from .elements import create_fire, create_water
    return F"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    from .elements import create_fire, create_earth
    return F"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    from .elements import create_water, create_air
    return \
        F"Invisibility potion brewed with {create_air()} and {create_water()}"


def wisdom_potion() -> str:
    from .elements import create_fire, create_water, create_earth, create_air
    return ("Wisdom potion brewed with all elements:" +
            F"{create_air()} {create_earth()} {create_fire()} {create_water()}"
            )
