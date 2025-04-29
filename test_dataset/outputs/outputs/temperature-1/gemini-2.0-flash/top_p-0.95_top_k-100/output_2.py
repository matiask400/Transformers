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

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length

def test_length_of_longest_substring():
    """
    Tests the length_of_longest_substring function with various test cases.
    """
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3)
    ]

    correct_count = 0
    total_count = len(tests)

    for input_string, expected_output in tests:
        result = length_of_longest_substring(input_string)
        if result == expected_output:
            print(True)
            correct_count += 1
        else:
            print(False)

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_length_of_longest_substring()