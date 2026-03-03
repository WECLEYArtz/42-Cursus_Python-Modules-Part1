def garden_operations(test_num: str):
    match test_num:
        case "ValueError":
            _ = int("abc")
        case "ZeroDivisionError":
            _ = 1/0
        case "FileNotFoundError":
            _ = open("missing.txt", "r")
        case "KeyError":
            dictionary: dict[str, str] = {}
            _ = dictionary["missing_plant"]
        case _:
            print("Why did we even reach here?...")


def test_error_types():
    tests: list[str] = [
            "ValueError",
            "ZeroDivisionError",
            "FileNotFoundError",
            "KeyError",
            ]
    print("=== Garden Error Types Demo ===")
    print()
    for name in tests:
        try:
            print("Testing", name+"...")
            garden_operations(name)
        except ValueError:
            print("Caught ValueError: invalid literal for int()")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
        except FileNotFoundError as e:
            print(F"Caught FileNotFoundError: No such file '{e.filename}'")
        except KeyError as e:
            print("Caught KeyError:", e )
        except Exception as e:
            print("Something went wrong:", e)
        print()

    try:
        print("Testing multiple errors together...")
        garden_operations("ValueError")
        garden_operations("ZeroDivisionError")
        garden_operations("FileNotFoundError")
        garden_operations("KeyError")
    except (ValueError, FileNotFoundError, KeyError, ZeroDivisionError, Exception):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
