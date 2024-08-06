import unittest


def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    max_len = 0
    start = 0
    char_index = {}
    for end in range(n):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        char_index[s[end]] = end
        max_len = max(max_len, end - start + 1)
    return max_len


class TestLongestSubstring(unittest.TestCase):
    def test_example_1(self):
        s = "abcabcbb"
        expected_output = 3
        self.assertEqual(lengthOfLongestSubstring(s), expected_output)
        print(f"Example 1: {lengthOfLongestSubstring(s) == expected_output}")

    def test_example_2(self):
        s = "bbbbb"
        expected_output = 1
        self.assertEqual(lengthOfLongestSubstring(s), expected_output)
        print(f"Example 2: {lengthOfLongestSubstring(s) == expected_output}")

    def test_example_3(self):
        s = "pwwkew"
        expected_output = 3
        self.assertEqual(lengthOfLongestSubstring(s), expected_output)
        print(f"Example 3: {lengthOfLongestSubstring(s) == expected_output}")

    def test_example_4(self):
        s = ""
        expected_output = 0
        self.assertEqual(lengthOfLongestSubstring(s), expected_output)
        print(f"Example 4: {lengthOfLongestSubstring(s) == expected_output}")


if __name__ == '__main__':
    unittest.main()