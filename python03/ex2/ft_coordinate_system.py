import sys
import math


def distance(x: int, y: int, z: int) -> float:
    return (math.sqrt((x)**2 + (y)**2 + (z)**2))


def unpack(cords: tuple[int, int, int]) -> None:
    (x, y, z) = cords
    print("Unpacking demonstration:")
    print("Player at x=0, y=0, z=0")
    print(F"Coordinates: X={x}, Y={y}, Z={z}")


def parse_cords(arg: str) -> tuple[int, int, int]:
    values = arg.split(",")

    if values.__len__() != 3:
        print("Error parsing coordinates:", end=' ')
        print("Must pass exactly 3 values")
        return

    tmp: list[int] = []
    for value in values:
        try:
            tmp += [int(value)]
        except ValueError:
            message = "invalid literal for int() with base 10: "+value
            print("Parsing invalid coordinates:", arg)
            print("Error parsing coordinates:", message)
            raise ValueError(message)

    cords: tuple[int, int, int] = (tmp[0], tmp[1], tmp[2])
    print("Parsing coordinates:", arg)
    print("Parsed position:", cords)
    return cords


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    cords = (10, 20, 5)
    print("Position created:", cords)
    print(F"Distance between (0, 0, 0) and {cords}: {distance(*cords):.2f}")
    print()

    for arg in sys.argv:
        try:
            cords = parse_cords(arg)
        except ValueError as e:
            print(F"Error details - Type: ValueError, Args: ({e})")
        except Exception:
            print('huh')

    unpack(cords)

# $> python3 ft_coordinate_system.py
# === Game Coordinate System ===
#
# Position created: (10, 20, 5)
# Distance between (0, 0, 0) and (10, 20, 5): 22.91
#
# Parsing coordinates: "3,4,0"
# Parsed position: (3, 4, 0)
# Distance between (0, 0, 0) and (3, 4, 0): 5.0
#
# Parsing invalid coordinates: "abc,def,ghi"
# Error parsing coordinates: invalid literal for int() with base 10: 'abc'
# Error details - Type: ValueError, Args: ("invalid literal for int() with base 10: 'abc'",)
#
# Unpacking demonstration:
# Player at x=3, y=4, z=0
# Coordinates: X=3, Y=4, Z=0
