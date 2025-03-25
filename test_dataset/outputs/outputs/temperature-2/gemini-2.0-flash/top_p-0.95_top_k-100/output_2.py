def lengthOfLongestSubstring(s):
    """
    Given a string s, find the length of the longest substring without repeating characters.

    Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.

    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    Example 4:
    Input: s = ""
    Output: 0

    Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
    """
    n = len(s)
    max_length = 0
    char_index_map = {}
    start = 0
    for end in range(n):
        if s[end] in char_index_map:
            start = max(start, char_index_map[s[end]] + 1)
        char_index_map[s[end]] = end
        max_length = max(max_length, end - start + 1)
    return max_length

def test_lengthOfLongestSubstring():
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0)
    ]
    
    correct_count = 0
    total_tests = len(test_cases)
    
    for input_string, expected_output in test_cases:
        result = lengthOfLongestSubstring(input_string)
        if result == expected_output:
            print(True)
            correct_count += 1
        else:
            print(False)

    print(f"{correct_count}/{total_tests}")

if __name__ == '__main__':
    test_lengthOfLongestSubstring()