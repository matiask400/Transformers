def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    max_len = 1
    start = 0
    end = 1
    seen = set(s[start])
    while end < n:
        if s[end] not in seen:
            seen.add(s[end])
            end += 1
            max_len = max(max_len, end - start)
        else:
            seen.remove(s[start])
            start += 1
    return max_len

# Example 1
s = "abcabcbb"
output_1 = lengthOfLongestSubstring(s)
print(output_1 == 3)  # True

# Example 2
s = "bbbbb"
output_2 = lengthOfLongestSubstring(s)
print(output_2 == 1)  # True

# Example 3
s = "pwwkew"
output_3 = lengthOfLongestSubstring(s)
print(output_3 == 3)  # True