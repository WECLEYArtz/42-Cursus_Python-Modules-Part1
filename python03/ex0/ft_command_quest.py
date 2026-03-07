import sys


def main() -> None:
    argv_clean = [arg for arg in sys.argv[1:] if arg]

    print("=== Command Quest ===")

    if not len(argv_clean):
        print("No arguments provided!")

    print("Program name:", sys.argv[0])

    if len(argv_clean):
        print("Arguments received:", len(argv_clean))
        i: int = 0
        while i < len(argv_clean):
            print(F"Argument{i + 1}:", argv_clean[i])
            i += 1
    print("Total arguments:", len(sys.argv))


if __name__ == "__main__":
    main()
