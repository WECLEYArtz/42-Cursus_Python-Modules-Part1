def check_temperature(temp_str: str) -> int:
    try:
        temp_number = int(temp_str)
    except ValueError:
        raise ValueError(F"Error: '{temp_str}' is not a valid number")

    if (temp_number > 40):
        raise ValueError(
                F"Error: {temp_number} °C is too hot for plants (max 40°C)")
    elif (temp_number < 0):
        raise ValueError(
                F"Error: {temp_number} °C is too cold for plants (min 0°C)")
    return temp_number


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    tests: list[str] = ["25", "abc", "100", "-50"]
    for test in tests:
        print("Testing temperature:", test)
        try:
            temp = check_temperature(test)
        except ValueError as e:
            print(e)
        except Exception as e:
            print("Something went wrong:", e)
        else:
            print("Temperature", temp, "°C is perfect for plants!")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
