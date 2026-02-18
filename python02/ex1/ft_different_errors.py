
def garden_operations(test_num: int):
    match test_num:
        case 0:
            _ = int("abc")
        case 1:
            _ = 1/0
        case 2:
            _ = open("missing.txt", "r")
        case 3:
            dictionary: dict[str, str] = {}
            _ = dictionary["plant"]
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
    for i in range(tests.__len__()):
        try:
            print("Testing", tests[i])
            garden_operations(i)
        except ValueError:
            print("Caught ValueError: invalid literal for int()\n")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero\n")
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'\n")
        except KeyError:
            print("Caught KeyError: 'nothing\n")

    try:
        print("Testing multiple errors together...")
        garden_operations(0)
        garden_operations(1)
        garden_operations(2)
        garden_operations(3)
    except (ValueError, KeyError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
