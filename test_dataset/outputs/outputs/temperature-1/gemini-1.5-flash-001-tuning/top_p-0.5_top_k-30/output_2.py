def lengthOfLongestSubstring(s):
    """
    Finds the length of the longest substring without repeating characters.

    Args:
        s: The input string.

    Returns:
        The length of the longest substring without repeating characters.
    """
    n = len(s)
    if n == 0:
        return 0
    
    max_len = 1
    start = 0
    char_index = {}
    for i in range(n):
        if s[i] in char_index and char_index[s[i]] >= start:
            start = char_index[s[i]] + 1
        char_index[s[i]] = i
        max_len = max(max_len, i - start + 1)
    return max_len

def test_lengthOfLongestSubstring():
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("dvdf", 3),
        (" ", 1),
        ("au", 2),
        ("aab", 2),
        ("tmmzuxt", 5),
    ]
    passed = 0
    for s, expected in test_cases:
        result = lengthOfLongestSubstring(s)
        print(result == expected, end=" ")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")

test_lengthOfLongestSubstring()