def check_temperature(temp_str: str) -> int | None:
    temp_number = 0
    print("temp_str:", temp_str)
    try:
        temp_number = int(temp_str)
        if (temp_number > 40):
            print("Error:", temp_number, "°C is too hot for plants (max 40°C)")
        elif (temp_number < 0):
            print("Error:", temp_number, "°C is too cold for plants (min 0°C)")
        else:
            print("Temperature", temp_number, "°C is perfect for plants!")
    except ValueError:
        print("Error: "+temp_str+" is not a valid number")


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    tests: list[str] = ["25", "abc", "100", "-50"]
    for test in tests:
        print("Testing temperature:", test)
        _ = check_temperature(test)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()

# === Garden Temperature Checker ===

# Testing temperature: 25
# Temperature 25°C is perfect for plants!

# Testing temperature: abc
# Error: 'abc' is not a valid number

# Testing temperature: 100
# Error: 100°C is too hot for plants (max 40°C)

# Testing temperature: -50
# Error: -50°C is too cold for plants (min 0°C)

# All tests completed - program didn't crash!
