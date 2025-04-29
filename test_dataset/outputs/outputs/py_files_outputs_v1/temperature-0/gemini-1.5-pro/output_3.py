def length_of_longest_substring(s):
    n = len(s)
    longest = 0
    start = 0
    char_index = {}

    for i in range(n):
        if s[i] in char_index and start <= char_index[s[i]]:
            start = char_index[s[i]] + 1
        else:
            longest = max(longest, i - start + 1)
        char_index[s[i]] = i

    return longest


input1 = "abcabcbb"
output1 = 3
input2 = "bbbbb"
output2 = 1
input3 = "pwwkew"
output3 = 3

print(length_of_longest_substring(input1) == output1)
print(length_of_longest_substring(input2) == output2)
print(length_of_longest_substring(input3) == output3)