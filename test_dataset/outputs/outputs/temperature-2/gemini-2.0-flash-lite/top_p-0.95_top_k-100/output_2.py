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

    start = 0
    end = 0
    max_length = 0
    char_index_map = {}  # Store the index of each character

    while end < len(s):
        char = s[end]
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = end
        max_length = max(max_length, end - start + 1)
        end += 1
    return max_length


def test_length_of_longest_substring():
    """
    Tests the length_of_longest_substring function.
    """
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
        ("tmmzuxt",5)

    ]

    correct_count = 0
    for i, (s, expected_output) in enumerate(tests):
        result = length_of_longest_substring(s)
        if result == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Test {i+1} Failed. Expected: {expected_output}, Got: {result}")

    print(f"{correct_count}/{len(tests)}")


test_length_of_longest_substring()