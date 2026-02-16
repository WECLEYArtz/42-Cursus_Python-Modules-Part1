import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])
    clean_argv = [arg for arg in sys.argv[1:] if arg]

    if not len(clean_argv):
        exit("No arguments provided!")

    print("Arguments received:", len(clean_argv))
    i: int = 0
    while i < len(clean_argv):
        print(F"Argument{i + 1}:", clean_argv[i])
        i += 1
    print("Total arguments:", len(sys.argv))


# $> python3 ft_command_quest.py
# === Command Quest ===
# No arguments provided!
# Program name: ft_command_quest.py
# Total arguments: 1
# $> python3 ft_command_quest.py hello world 42
# === Command Quest ===
# Program name: ft\_command\_quest.py
# Arguments received: 3
# Argument 1: hello
# Argument 2: world
# Argument 3: 42
# Total arguments: 4
# $> python3 ft_command_quest.py "Data Quest"
# === Command Quest ===
# Program name: ft_command_quest.py
# Arguments received: 1
# Argument 1: Data Ques
