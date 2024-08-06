import unittest

def length_of_longest_substring(s: str) -> int:
    """
    Given a string s, find the length of the longest substring without repeating characters.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the longest substring without repeating characters.
    """
    n = len(s)
    if n == 0:
        return 0
    max_len = 1
    start = 0
    end = 1
    seen = set()
    seen.add(s[0])
    while end < n:
        if s[end] not in seen:
            seen.add(s[end])
            end += 1
            max_len = max(max_len, end - start)
        else:
            seen.remove(s[start])
            start += 1
    return max_len

class TestLongestSubstring(unittest.TestCase):
    def test_example_1(self):
        s = "abcabcbb"
        expected_output = 3
        self.assertEqual(length_of_longest_substring(s), expected_output)
        print(f"Example 1: {length_of_longest_substring(s) == expected_output}")

    def test_example_2(self):
        s = "bbbbb"
        expected_output = 1
        self.assertEqual(length_of_longest_substring(s), expected_output)
        print(f"Example 2: {length_of_longest_substring(s) == expected_output}")

    def test_example_3(self):
        s = "pwwkew"
        expected_output = 3
        self.assertEqual(length_of_longest_substring(s), expected_output)
        print(f"Example 3: {length_of_longest_substring(s) == expected_output}")

    def test_example_4(self):
        s = ""
        expected_output = 0
        self.assertEqual(length_of_longest_substring(s), expected_output)
        print(f"Example 4: {length_of_longest_substring(s) == expected_output}")

if __name__ == '__main__':
    unittest.main()