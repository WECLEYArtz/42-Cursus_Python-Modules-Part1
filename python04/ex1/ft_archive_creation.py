def archive(vault: str, entries: list[str]) -> None:
    print("Initializing new storage unit:", vault)

    with open(vault, 'w') as f:
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        for entry in entries:
            print(entry)
            _ = f.write(entry+"\n")
        f.close()

    print()
    print("Data inscription complete. Storage unit sealed.")
    print(F"Archive '{vault}' ready for long-term preservation.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    vault: str = "new_discovery.txt"
    entries: list[str] = [
            "[ENTRY 001] New quantum algorithm discovered",
            "[ENTRY 002] Efficiency increased by 347%",
            "[ENTRY 003] Archived by Data Archivist trainee"
            ]

    try:
        archive(vault, entries)
    except Exception as e:
        print("\nUnexpected error:", e.__class__.__name__, e)
