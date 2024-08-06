def length_of_longest_substring(s: str) -> int:
    char_set = set()
    l = 0
    max_length = 0
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        max_length = max(max_length, r - l + 1)
    return max_length


input_1 = "abcabcbb"
output_1 = 3
input_2 = "bbbbb"
output_2 = 1
input_3 = "pwwkew"
output_3 = 3
input_4 = ""
output_4 = 0

print(length_of_longest_substring(input_1) == output_1)
print(length_of_longest_substring(input_2) == output_2)
print(length_of_longest_substring(input_3) == output_3)
print(length_of_longest_substring(input_4) == output_4)