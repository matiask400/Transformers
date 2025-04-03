def reorder_logs(logs):
    """
    Reorders logs based on the problem description.

    Args:
        logs: A list of strings representing the logs.

    Returns:
        A list of strings representing the reordered logs.
    """

    letter_logs = []
    digit_logs = []

    for log in logs:
        identifier, content = log.split(" ", 1)
        if content[0].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(log)

    letter_logs.sort(key=lambda log: (log.split(" ", 1)[1], log.split(" ", 1)[0]))

    return letter_logs + digit_logs


def test_reorder_logs():
    """
    Tests the reorder_logs function with the provided examples.
    """

    test_cases = [
        {
            "input": ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"],
            "expected": ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"],
        },
        {
            "input": ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"],
            "expected": ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"],
        },
        {
            "input": ["j mo", "5 m w", "g 07", "o 2 0"],
            "expected": ["j mo", "5 m w", "g 07", "o 2 0"],
        },
        {
            "input": ["mi2 jog mid pet", "wz3 34 54 398", "a1 alps cow bar", "x4 45 21 7"],
            "expected": ["a1 alps cow bar", "mi2 jog mid pet", "wz3 34 54 398", "x4 45 21 7"],
        },
        {
            "input": ["t k", "r h", "i l", "p q"],
            "expected": ["i l", "p q", "r h", "t k"],
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        input_logs = test_case["input"]
        expected_output = test_case["expected"]
        actual_output = reorder_logs(input_logs)

        if actual_output == expected_output:
            print(f"Test {i + 1}: True")
            correct_tests += 1
        else:
            print(f"Test {i + 1}: False")
            print(f"  Input: {input_logs}")
            print(f"  Expected: {expected_output}")
            print(f"  Actual: {actual_output}")

    print(f"\nCorrect tests: {correct_tests}/{total_tests}")


if __name__ == "__main__":
    test_reorder_logs()