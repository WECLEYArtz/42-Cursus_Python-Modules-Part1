def recover(vault: str) -> None:
    print("Accessing Storage Vault:", vault)
    with open(vault) as f:
        print("Connection established...\n")
        print("RECOVERED DATA:")

        print(f.read(), "\n")
        f.close()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    vault: str = "ancient_fragment.txt"
    try:
        recover(vault)
    except PermissionError:
        print("\nError - No permission to access", vault)
    except FileNotFoundError:
        print("\nError - No file with the name:", vault)
    except IsADirectoryError:
        print("\nError - The vault", vault, "must be file. It's a directory")
    except Exception as e:
        print("\nUnexpected error:", e.__class__.__name__, e)
