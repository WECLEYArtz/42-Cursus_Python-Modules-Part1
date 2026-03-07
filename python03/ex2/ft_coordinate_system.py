import sys
import math


def show_distance(cords: tuple[int, int, int]) -> None:
    x, y, z = cords
    dist = (math.sqrt((x)**2 + (y)**2 + (z)**2))
    print(F"Distance between (0, 0, 0) and {cords}: {dist:.2f}")


def unpack(cords: tuple[int, int, int]) -> None:
    (x, y, z) = cords
    print("Unpacking demonstration:")
    print("Player at x=0, y=0, z=0")
    print(F"Coordinates: X={x}, Y={y}, Z={z}")


def parse_cords(values: list[str]) -> tuple[int, int, int]:
    cords = (int(values[0]), int(values[1]), int(values[2]))
    print("Parsed position:", cords)
    return cords


def main() -> None:
    print("=== Game Coordinate System ===\n")

    cords = (10, 20, 5)
    print("Position created:", cords)
    show_distance(cords)
    print()

    for arg in sys.argv[1:]:
        values = arg.split(",")

        if values.__len__() != 3:
            print("Error parsing coordinates:", end=' ')
            print("Must pass exactly 3 values, unmatched requirement in:", arg)
            continue
        try:
            print("Parsing coordinates:", arg)
            cords = parse_cords(values)
            show_distance(cords)
        except ValueError as e:
            print("Error parsing coordinates:", e)
            print(f'Error details - Type: ValueError, Args: ("{e}")')
        print()
    unpack(cords)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Unexcpecetd error", e)
