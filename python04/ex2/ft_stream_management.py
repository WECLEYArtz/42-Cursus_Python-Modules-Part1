import sys


def alert(message: str) -> None:
    print("[ALERT]", message, file=sys.stderr)


def standard(message: str) -> None:
    print("[STANDARD]", message, file=sys.stdout)


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    id: str = input("Input Stream active. Enter archivist ID: ")
    report: str = input("Input Stream active. Enter status report: ")

    print()

    standard(F"Archive status from {id}: {report}")
    alert("System diagnostic: Communication channels verified")
    standard("Data transmission complete")

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\nUnexpected error:", e.__class__.__name__, e)


# Input Stream active. Enter archivist ID: ARCH_7742
# Input Stream active. Enter status report: All systems nominal
