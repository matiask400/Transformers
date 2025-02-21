s = "abcabcbb"
print(lengthOfLongestSubstring(s) == 3)
s = "bbbbb"
print(lengthOfLongestSubstring(s) == 1)
s = "pwwkew"
print(lengthOfLongestSubstring(s) == 3)
s = ""
print(lengthOfLongestSubstring(s) == 0)

def lengthOfLongestSubstring(s: str) -> int:
    char_index_map = {}
    max_length = 0
    start = 0
    for end in range(len(s)):
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            start = char_index_map[s[end]] + 1
        char_index_map[s[end]] = end
        max_length = max(max_length, end - start + 1)
    return max_length