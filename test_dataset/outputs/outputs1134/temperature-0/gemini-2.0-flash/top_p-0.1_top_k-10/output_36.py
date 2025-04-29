def format_number_with_dots(n):
    """
    Adds a dot (".") as the thousands separator to an integer and returns it in string format.

    Args:
        n: An integer.

    Returns:
        A string representing the integer with dots as thousands separators.
    """
    s = str(n)
    result = ""
    count = 0
    for i in range(len(s) - 1, -1, -1):
        result = s[i] + result
        count += 1
        if count % 3 == 0 and i != 0:
            result = "." + result
    return result

def test_format_number_with_dots():
    """
    Tests the format_number_with_dots function with several test cases.
    """
    test_cases = [
        (987, "987"),
        (1234, "1.234"),
        (123456789, "123.456.789"),
        (0, "0"),
        (1000, "1.000"),
        (1000000, "1.000.000"),
        (1, "1"),
        (12, "12"),
        (123, "123")
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for n, expected in test_cases:
        actual = format_number_with_dots(n)
        if actual == expected:
            print("True")
            correct_tests += 1
        else:
            print("False")
            print(f"Input: {n}, Expected: {expected}, Actual: {actual}")

    print(f"{correct_tests}/{total_tests}")

if __name__ == "__main__":
    test_format_number_with_dots()