def length_of_longest_substring(s: str) -> int:
    char_set = set()
    l = 0
    max_len = 0
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        max_len = max(max_len, r - l + 1)
    return max_len


# Test cases
input1 = "abcabcbb"
output1 = 3
input2 = "bbbbb"
output2 = 1
input3 = "pwwkew"
output3 = 3

print(length_of_longest_substring(input1) == output1)
print(length_of_longest_substring(input2) == output2)
print(length_of_longest_substring(input3) == output3)