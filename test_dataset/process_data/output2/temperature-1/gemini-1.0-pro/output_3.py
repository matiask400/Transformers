def lengthOfLongestSubstring(s: str) -> int:
    start = 0
    end = 0
    max_len = 0
    char_index_map = {}

    while end < len(s):
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            start = char_index_map[s[end]] + 1
        char_index_map[s[end]] = end
        max_len = max(max_len, end - start + 1)
        end += 1

    return max_len


# Test the function
input1 = "abcabcbb"
output1 = lengthOfLongestSubstring(input1)
print(output1 == 3)

input2 = "bbbbb"
output2 = lengthOfLongestSubstring(input2)
print(output2 == 1)

input3 = "pwwkew"
output3 = lengthOfLongestSubstring(input3)
print(output3 == 3)