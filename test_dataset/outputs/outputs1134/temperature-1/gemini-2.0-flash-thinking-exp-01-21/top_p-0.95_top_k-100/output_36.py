def format_number(n):
    s = str(n)
    if len(s) <= 3:
        return s
    result = ""
    count = 0
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
        count += 1
        if count % 3 == 0 and i != 0:
            result += "."
    return result[::-1]

def run_tests():
    test_cases = [
        (987, "987"),
        (1234, "1.234"),
        (123456789, "123.456.789"),
        (0, "0"),
        (1000, "1.000"),
        (1000000, "1.000.000"),
        (999, "999"),
        (1001, "1.001"),
        (12345, "12.345"),
        (123456, "123.456"),
        (1, "1")
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for input_n, expected_output in test_cases:
        actual_output = format_number(input_n)
        if actual_output == expected_output:
            print("True")
            correct_tests += 1
        else:
            print("False")

    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()