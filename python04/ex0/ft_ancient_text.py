def recover(vault: str):
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("Accessing Storage Vault:", vault)
    with open(vault) as f:
        print("Connection established...\n")
        print("RECOVERED DATA:")

        print(f.read(), "\n")
        f.close()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    vault: str = "ancient_fragment.txt"
    try:
        recover(vault)
    except PermissionError:
        print("\nError - No permission to access", vault)
    except IsADirectoryError:
        print("\nError - The vault", vault, "must be a file, found directory")
    except Exception as e:
        print("\nUnexpected error:", e.__class__.__name__, e)
