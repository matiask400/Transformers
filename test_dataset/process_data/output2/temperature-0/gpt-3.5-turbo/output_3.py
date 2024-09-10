def lengthOfLongestSubstring(s):
    start = 0
    max_length = 0
    char_index = {}

    for i in range(len(s)):
        if s[i] in char_index and char_index[s[i]] >= start:
            start = char_index[s[i]] + 1
        char_index[s[i]] = i
        max_length = max(max_length, i - start + 1)

    return max_length

# Test the solution with example inputs
print(lengthOfLongestSubstring('abcabcbb') == 3)
print(lengthOfLongestSubstring('bbbbb') == 1)
print(lengthOfLongestSubstring('pwwkew') == 3)