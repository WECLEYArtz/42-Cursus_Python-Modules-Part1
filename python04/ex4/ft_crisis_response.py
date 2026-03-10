def test1() -> None:
    file_name: str = "lost_archive.txt"

    print(F"CRISIS ALERT: Attempting access to '{file_name}'...")
    with open(file_name) as file:
        file.close()
        print(file, "exists")


def test2() -> None:
    file_name: str = "classified_vault.txt"

    print(F"CRISIS ALERT: Attempting access to '{file_name}'...")
    with open(file_name) as file:
        _ = file.read()
        print(file, "is readable")


def test3() -> None:
    file_name: str = "standard_archive.txt"

    print(F"ROUTINE ACCESS: Attempting access to '{file_name}'...")
    with open(file_name) as file:
        data: str = file.read()
        print(F"SUCCESS: Archive recovered - ``{data}''")


def main() -> None:
    tests = [test1, test2, test3]
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    for test in tests:
        try:
            test()
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix" +
                  "\nSTATUS: Crisis handled, system stable")
        except PermissionError:
            print("RESPONSE: Security protocols deny access" +
                  "\nSTATUS: Crisis handled, security maintained")
        except IsADirectoryError:
            print("RESPONSE: Archive is a directory, not a file" +
                  "\nSTATUS: Crisis handled, server monitored")
        else:
            print("STATUS: Normal operations resumed")
        finally:
            print()
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("RESPONSE: Unexpected error -", e.__class__.__name__ +
              "\nSTATUS: Crisis handled, blackhole arrived")


# === CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===

# CRISIS ALERT: Attempting access to 'lost_archive.txt'...
# RESPONSE: Archive not found in storage matrix
# STATUS: Crisis handled, system stable

# CRISIS ALERT: Attempting access to 'classified_vault.txt'...
# RESPONSE: Security protocols deny access
# STATUS: Crisis handled, security maintained

# ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...
# SUCCESS: Archive recovered - ``Knowledge preserved for humanity''
# STATUS: Normal operations resumed

# All crisis scenarios handled successfully. Archives secure.
