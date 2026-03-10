def process(vault_pres: str, vault_extr: str, entry: str) -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    with open(vault_extr, 'r') as file_1:
        print("Vault connection established with failsafe protocols\n")

        print("SECURE EXTRACTION:")
        print(file_1.read(), '\n')

    with open(vault_pres, "w") as file_2:
        print("SECURE PRESERVATION:")
        print(entry)
        _ = file_2.write(entry)
        print("Vault automatically sealed upon completion\n")

    print("All vault operations completed with maximum security.")


def main() -> None:
    vault_extr: str = "classified_data.txt"
    vault_pres: str = "new_information.txt"
    entry: str = "[CLASSIFIED] New security protocols archived"

    try:
        process(vault_pres, vault_extr, entry)
    except PermissionError as e:
        print("\nError - No permission to access", e.filename)
    except FileNotFoundError as e:
        print("\nError - No file with the name:", e.filename)
    except IsADirectoryError as e:
        print("\nError -", e.filename, "must be file. It's a directory")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\nUnexpected error:", e.__class__.__name__, e)
