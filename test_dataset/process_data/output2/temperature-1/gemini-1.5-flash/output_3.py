def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    max_length = 0
    start = 0
    seen = set()
    for end in range(n):
        while s[end] in seen:
            seen.remove(s[start])
            start += 1
        seen.add(s[end])
        max_length = max(max_length, end - start + 1)
    return max_length

# Example 1
s = "abcabcbb"
output_1 = lengthOfLongestSubstring(s)
print(f"Example 1: {output_1 == 3}")

# Example 2
s = "bbbbb"
output_2 = lengthOfLongestSubstring(s)
print(f"Example 2: {output_2 == 1}")

# Example 3
s = "pwwkew"
output_3 = lengthOfLongestSubstring(s)
print(f"Example 3: {output_3 == 3}")

# Example 4
s = ""
output_4 = lengthOfLongestSubstring(s)
print(f"Example 4: {output_4 == 0}")