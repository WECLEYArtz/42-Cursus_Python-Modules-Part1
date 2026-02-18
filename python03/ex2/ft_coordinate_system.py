import sys
import math


def show_distance(x: int, y: int, z: int) -> None:
    dist = (math.sqrt((x)**2 + (y)**2 + (z)**2))
    print(F"Distance between (0, 0, 0) and {cords}: {dist}")


def unpack(cords: tuple[int, int, int]) -> None:
    (x, y, z) = cords
    print("Unpacking demonstration:")
    print("Player at x=0, y=0, z=0")
    print(F"Coordinates: X={x}, Y={y}, Z={z}")


def parse_cords(arg: str) -> tuple[int, int, int]:

    tmp: list[int] = []
    cords: tuple[int, int, int]
    for value in values:
        try:
            tmp += [int(value)]
        except ValueError:
            raise ValueError(value)
    cords = (tmp[0], tmp[1], tmp[2])
    print("Parsing coordinates:", arg)
    print("Parsed position:", cords)
    return cords


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    cords = (10, 20, 5)
    print("Position created:", cords)
    show_distance(*cords)
    print()

    for arg in sys.argv[1:]:
        values = arg.split(",")

        if values.__len__() != 3:
            print("Error parsing coordinates:", end=' ')
            print("Must pass exactly 3 values, unmatched requirement in:",
                  arg)
            continue
        try:
            cords = parse_cords(arg)
            show_distance(*cords)
        except ValueError as val:
            error = F"invalid literal for int() with base 10: '{val}'"
            print("Parsing invalid coordinates:", error)
            print("Error parsing coordinates:", )
            print(f"Error details - Type: ValueError, Args: ({error})")
        print()

    unpack(cords)
