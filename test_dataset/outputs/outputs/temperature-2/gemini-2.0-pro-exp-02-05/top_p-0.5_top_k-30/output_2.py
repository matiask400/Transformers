def longest_substring_without_repeating_characters(s: str) -> int:
    """
    Given a string s, find the length of the longest substring without repeating characters.
    """
    char_index_map = {}
    max_length = 0
    start = 0
    for end, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = end
        max_length = max(max_length, end - start + 1)
    return max_length


def test_longest_substring_without_repeating_characters():
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
    ]
    passed_tests = 0
    total_tests = len(test_cases)

    for s, expected_output in test_cases:
        actual_output = longest_substring_without_repeating_characters(s)
        if actual_output == expected_output:
            print("True")
            passed_tests += 1
        else:
            print("False")

    print(f"{passed_tests}/{total_tests}")


if __name__ == "__main__":
    test_longest_substring_without_repeating_characters()