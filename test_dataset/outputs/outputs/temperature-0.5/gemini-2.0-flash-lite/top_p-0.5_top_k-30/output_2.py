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

def run_tests():
    """Runs the tests and prints the results."""
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
        ("tmmzuxt", 5)
    ]
    correct_tests = 0
    for i, (s, expected_output) in enumerate(test_cases):
        result = lengthOfLongestSubstring(s)
        if result == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
    print(f"Correct tests: {correct_tests}/{len(test_cases)}")

run_tests()