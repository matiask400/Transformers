def large_group_positions(s):
    """
    Finds the intervals of large groups in a string.

    Args:
        s: The input string.

    Returns:
        A list of intervals representing the large groups, sorted by start index.
    """
    result = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[i] == s[j]:
            j += 1
        if j - i >= 3:
            result.append([i, j - 1])
        i = j
    return result

def test_large_group_positions():
    """
    Tests the large_group_positions function.
    """
    test_cases = [
        ("abbxxxxzzy", [[3, 6]]),
        ("abc", []),
        ("abcdddeeeeaabbbcd", [[3, 5], [6, 9], [12, 14]]),
        ("aba", []),
        ("aaa", [[0,2]]),
        ("aabbbaa", [])
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, (input_str, expected_output) in enumerate(test_cases):
        actual_output = large_group_positions(input_str)
        if actual_output == expected_output:
            print("True")
            correct_tests += 1
        else:
            print("False")
            print(f"Test case {i+1} failed:")
            print(f"Input: {input_str}")
            print(f"Expected output: {expected_output}")
            print(f"Actual output: {actual_output}")

    print(f"{correct_tests}/{total_tests}")

if __name__ == "__main__":
    test_large_group_positions()