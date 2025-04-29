def format_number_with_dots(n):
    s = str(n)
    if len(s) <= 3:
        return s
    parts = []
    for i in range(len(s), 0, -3):
        start_index = max(0, i - 3)
        parts.append(s[start_index:i])
    return ".".join(reversed(parts))

def run_tests():
    test_cases = [
        (987, "987"),
        (1234, "1.234"),
        (123456789, "123.456.789"),
        (0, "0"),
        (1000, "1.000"),
        (1000000, "1.000.000"),
        (999, "999"),
        (1, "1"),
        (12, "12"),
        (123, "123"),
        (12345, "12.345"),
        (123456, "123.456"),
        (1234567, "1.234.567"),
        (12345678, "12.345.678"),
        (1234567890, "1.234.567.890")
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for input_n, expected_output in test_cases:
        actual_output = format_number_with_dots(input_n)
        if actual_output == expected_output:
            print('True')
            correct_tests += 1
        else:
            print('False')

    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()