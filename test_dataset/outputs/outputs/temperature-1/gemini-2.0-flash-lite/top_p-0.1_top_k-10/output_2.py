def lengthOfLongestSubstring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.

    Args:
        s: The input string.

    Returns:
        The length of the longest substring without repeating characters.
    """
    if not s:
        return 0

    max_length = 0
    start = 0
    char_index_map = {}  # Store the index of each character

    for end, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            # Repeating character found within the current window
            start = char_index_map[char] + 1
        char_index_map[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length

def test_length_of_longest_substring():
    """Tests the lengthOfLongestSubstring function."""
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
        ("anviaj", 6)
    ]
    correct_tests = 0
    for s, expected_length in tests:
        result = lengthOfLongestSubstring(s)
        if result == expected_length:
            print(True)
            correct_tests += 1
        else:
            print(False)
    print(f"{correct_tests}/{len(tests)}")

if __name__ == '__main__':
    test_length_of_longest_substring()