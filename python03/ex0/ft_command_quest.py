import sys

if __name__ == "__main__":
    print("=== Command Quest ===")

    clean_argv = [arg for arg in sys.argv[1:] if arg]
    if not len(clean_argv):
        print("No arguments provided!")

    print("Program name:", sys.argv[0])

    if len(clean_argv):
        print("Arguments received:", len(clean_argv))
        i: int = 0
        while i < len(clean_argv):
            print(F"Argument{i + 1}:", clean_argv[i])
            i += 1
    print("Total arguments:", len(sys.argv))
