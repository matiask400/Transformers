def length_of_longest_substring(s: str) -> int:
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
    char_index_map = {}  # Store the last seen index of each character

    for end, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            # If the character is repeated within the current window,
            # move the start pointer to the next position after the previous occurrence.
            start = char_index_map[char] + 1
        
        char_index_map[char] = end  # Update the last seen index of the character
        max_length = max(max_length, end - start + 1)

    return max_length

def test_length_of_longest_substring():
    """Tests the length_of_longest_substring function."""
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("aab", 2),
        ("dvdf", 3),
        ("abba", 2)
    ]
    correct_tests = 0
    for i, (s, expected) in enumerate(tests):
        result = length_of_longest_substring(s)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
    print(f"Correct tests: {correct_tests}/{len(tests)}")


if __name__ == '__main__':
    test_length_of_longest_substring()