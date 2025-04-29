def lengthOfLongestSubstring(s: str) -> int:
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

# Test cases
input_1 = "abcabcbb"
output_1 = lengthOfLongestSubstring(input_1)

input_2 = "bbbbb"
output_2 = lengthOfLongestSubstring(input_2)

input_3 = "pwwkew"
output_3 = lengthOfLongestSubstring(input_3)

print(f"Input 1: {input_1}")
print(f"Output 1: {output_1}")
print(f"Input 2: {input_2}")
print(f"Output 2: {output_2}")
print(f"Input 3: {input_3}")
print(f"Output 3: {output_3}")

# Check if the outputs are correct
print(f"Output 1 is correct: {output_1 == 3}")
print(f"Output 2 is correct: {output_2 == 1}")
print(f"Output 3 is correct: {output_3 == 3}")