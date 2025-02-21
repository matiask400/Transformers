def lengthOfLongestSubstring(s):
    start = 0
    max_length = 0
    used_chars = {}

    for i in range(len(s)):
        if s[i] in used_chars and start <= used_chars[s[i]]:
            start = used_chars[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used_chars[s[i]] = i

    return max_length

# Test cases
print(lengthOfLongestSubstring('abcabcbb') == 3)
print(lengthOfLongestSubstring('bbbbb') == 1)
print(lengthOfLongestSubstring('pwwkew') == 3)