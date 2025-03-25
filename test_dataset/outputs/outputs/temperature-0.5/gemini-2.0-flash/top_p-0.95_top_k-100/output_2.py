def length_of_longest_substring(s):
    """
    Finds the length of the longest substring without repeating characters.

    Args:
        s: The input string.

    Returns:
        The length of the longest substring without repeating characters.
    """
    char_index_map = {}
    start = 0
    max_length = 0

    for end, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length


def test_length_of_longest_substring():
    """
    Tests the length_of_longest_substring function.
    """
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3)
    ]

    num_passed = 0
    total_tests = len(test_cases)

    for s, expected in test_cases:
        result = length_of_longest_substring(s)
        if result == expected:
            print("True")
            num_passed += 1
        else:
            print("False")

    print(f"{num_passed}/{total_tests}")


if __name__ == '__main__':
    test_length_of_longest_substring()