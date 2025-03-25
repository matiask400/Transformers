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
    char_index_map = {}  # Stores the index of each character

    for end, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            # Repeating character found within the current window
            start = char_index_map[char] + 1
        char_index_map[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length


def run_tests():
    """Runs the test cases and prints the results."""
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
        ("anviaj", 6),
        ("tmmzuxt", 5)
    ]
    correct_count = 0
    total_tests = len(test_cases)

    for i, (s, expected_length) in enumerate(test_cases):
        result = lengthOfLongestSubstring(s)
        if result == expected_length:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")

    print(f"Correct tests: {correct_count}/{total_tests}")

run_tests()