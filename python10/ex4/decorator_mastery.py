from typing import Callable, Any
from functools import wraps
from time import sleep, perf_counter
from random import choice


def spell_timer(f: Callable) -> Callable:
    @wraps(f)
    def wrapper():
        print(f"Casting {wrapper.__name__}...")
        start = perf_counter()
        result: str = f()
        print(f"Spell completed in {perf_counter() - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def power_validation_decorator(f: Callable[[int],Any]):
        @wraps(f)
        def wrapper(*args: int, **kwargs: int):
            power: int = kwargs.get('power')
            if not args and not kwargs:
                raise TypeError("no argument was recieved")
            if not power:
                power = args[0]
            if power >= min_power:
                return f(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return power_validation_decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(f: Callable):
        @wraps(f)
        def retry():
            for n in range(max_attempts):
                try:
                    result: Any = f()
                except ValueError:
                    print("Spell failed, " +
                          f"retrying... (attempt {n+1}/{max_attempts})")
                else:
                    return result
            return (f"Spell casting failed after {max_attempts} attempts" +
                    "\nWaaaaaaagh spelled !")
        return retry
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        name: str = name.strip()
        if not isinstance(name, str) or len(name) < 3\
                or not all(c == ' ' or c.isalpha() for c in name):
            return False
        return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


def main() -> None:
    @spell_timer
    def fireball() -> str:
        sleep(0.101)
        return "Fireball cast!"

    @retry_spell(max_attempts=3)
    def gambleball():
        var = [0, 3, 5, 7, 9, 10]
        if choice(var) % 2:
            raise ValueError()
        return "Spell casted!"

    print("Testing spell timer...")
    print("Result:", fireball())

    print("Testing retrying spell...")
    result = gambleball()
    print(result if result else "")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Dragon born"))
    print(guild.validate_mage_name("  "))
    print(guild.cast_spell("Lightning", power=15))
    print(guild.cast_spell("EpicFart", power=5))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error", e)

# Testing MageGuild...
# True
# False
# Successfully cast Lightning with 15 power
# Insufficient power for this spell
