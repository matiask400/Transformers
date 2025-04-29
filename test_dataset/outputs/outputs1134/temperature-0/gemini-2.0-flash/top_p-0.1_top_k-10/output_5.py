def largeGroupPositions(s):
    """
    Finds the intervals of every large group in a string.

    Args:
        s: The input string.

    Returns:
        A list of lists, where each inner list represents the interval [start, end] of a large group.
    """
    result = []
    start = 0
    for i in range(len(s)):
        if i == len(s) - 1 or s[i] != s[i + 1]:
            if i - start + 1 >= 3:
                result.append([start, i])
            start = i + 1
    return result

def test_largeGroupPositions():
    """
    Tests the largeGroupPositions function with several test cases.
    """
    test_cases = [
        ("abbxxxxzzy", [[3, 6]]),
        ("abc", []),
        ("abcdddeeeeaabbbcd", [[3, 5], [6, 9], [12, 14]]),
        ("aba", []),
        ("aaa", [[0, 2]]),
        ("aabbccddd", [[6, 8]]),
        ("abbxxxxzyy", [[3, 6]]),
        ("abbxxxxzzyyy", [[3, 6], [7, 8]]),
        ("abbxxxxzzyyyy", [[3, 6], [7, 10]]),
        ("abbxxxxzzyyyyy", [[3, 6], [7, 11]])
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (input_str, expected_output) in enumerate(test_cases):
        actual_output = largeGroupPositions(input_str)
        if actual_output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Test case {i+1} failed:")
            print(f"  Input: {input_str}")
            print(f"  Expected output: {expected_output}")
            print(f"  Actual output: {actual_output}")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_largeGroupPositions()