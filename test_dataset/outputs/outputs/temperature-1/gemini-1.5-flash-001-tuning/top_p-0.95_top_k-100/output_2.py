def lengthOfLongestSubstring(s):
    """
    Finds the length of the longest substring without repeating characters in a given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest substring without repeating characters.
    """
    n = len(s)
    if n == 0:
        return 0

    max_len = 0
    start = 0
    char_index = {}

    for i in range(n):
        if s[i] in char_index and char_index[s[i]] >= start:
            start = char_index[s[i]] + 1
        char_index[s[i]] = i
        max_len = max(max_len, i - start + 1)

    return max_len


def test_lengthOfLongestSubstring():
    """
    Tests the lengthOfLongestSubstring function with various inputs.
    """
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("dvdf", 3),
        (" ", 1),
        ("au", 2),
        ("abcdefghijklmnopqrstuvwxyz", 26),
    ]
    passed = 0
    for s, expected_output in test_cases:
        output = lengthOfLongestSubstring(s)
        print(f'Test: "{s}" - {output} == {expected_output} - {output == expected_output}')
        if output == expected_output:
            passed += 1
    print(f'Passed {passed} out of {len(test_cases)} tests.')


test_lengthOfLongestSubstring()