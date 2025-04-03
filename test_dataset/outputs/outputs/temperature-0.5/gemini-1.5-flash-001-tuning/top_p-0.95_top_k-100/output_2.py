def lengthOfLongestSubstring(s):
    """
    Finds the length of the longest substring without repeating characters.

    Args:
        s: The input string.

    Returns:
        The length of the longest substring without repeating characters.
    """
    longest = 0
    start = 0
    seen = {}  # Use a dictionary to track seen characters

    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = i
        longest = max(longest, i - start + 1)

    return longest

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
        ("jbpnbwwd", 4),
    ]
    passed = 0
    for s, expected in test_cases:
        result = lengthOfLongestSubstring(s)
        print(f"Test case: s = {s}, expected = {expected}, actual = {result} - {result == expected}")
        if result == expected:
            passed += 1
    print(f"Passed {passed} out of {len(test_cases)} tests")

test_lengthOfLongestSubstring()