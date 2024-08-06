def length_of_longest_substring(s):
    n = len(s)
    longest = 0
    for i in range(n):
        seen = set()
        j = i
        while j < n and s[j] not in seen:
            seen.add(s[j])
            j += 1
        longest = max(longest, j - i)
    return longest


# Test Cases
input1 = "abcabcbb"
output1 = 3
input2 = "bbbbb"
output2 = 1
input3 = "pwwkew"
output3 = 3

print(length_of_longest_substring(input1) == output1)
print(length_of_longest_substring(input2) == output2)
print(length_of_longest_substring(input3) == output3)