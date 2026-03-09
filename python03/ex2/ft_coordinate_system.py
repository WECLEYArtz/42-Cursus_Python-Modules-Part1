import sys
import math


def show_distance(cords_a: tuple[int, int, int],
                  cords_b: tuple[int, int, int]) -> None:
    x1, y1, z1 = cords_a
    x2, y2, z2 = cords_b
    dist = (math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
    print(F"Distance between {cords_a} and {cords_b}: {dist:.2f}")


def unpack(cords_b: tuple[int, int, int]) -> None:
    x, y, z = cords_b
    print("Unpacking demonstration:")
    print(F"Player at x={x}, y={y}, z={z}")
    print(F"Coordinates: X={x}, Y={y}, Z={z}")


def parse_cords(values: list[str]) -> tuple[int, int, int]:
    cords = (int(values[0]), int(values[1]), int(values[2]))
    print("Parsed position:", cords)
    return cords


def verify_cords(cords: tuple[int, int, int]) -> None:
    if len(cords) != 3:
        raise ValueError("Error creating cords, must be 3 points, got:",
                         cords)
    for point in cords:
        if point.__class__.__name__ != "int":
            raise ValueError("Error creating cords," +
                             F"Incorrect type of point:{point}", cords)


def main() -> None:
    print("=== Game Coordinate System ===\n")

    cords_a = (0, 0, 0)
    cords_b = (10, 20, 5)

    try:
        verify_cords(cords_a)
        verify_cords(cords_b)
    except ValueError as e:
        return (print(*e.args))

    print("Position created:", cords_b)
    show_distance(cords_a, cords_b)
    print()

    for arg in sys.argv[1:]:
        values = arg.split(",")

        if values.__len__() != 3:
            print("Error parsing coordinates:", end=' ')
            print("Must pass exactly 3 values, unmatched requirement in:", arg)
            continue
        try:
            print(F'Parsing coordinates: "{arg}"')
            cords_b = parse_cords(values)
            show_distance(cords_a, cords_b)
        except ValueError as e:
            print("Error parsing coordinates:", *e.args)
            print(f'Error details - Type: ValueError, Args: {e.args}')
        print()

    # Late Demonstration
    unpack(cords_b)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Unexcpecetd error", e)
