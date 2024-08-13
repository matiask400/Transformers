def length_of_longest_substring(s):
    used = {}
    max_length = start = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_length = max(max_length, i - start + 1)
        used[c] = i
    return max_length


input_1 = "abcabcbb"
output_1 = 3
input_2 = "bbbbb"
output_2 = 1
input_3 = "pwwkew"
output_3 = 3

print(length_of_longest_substring(input_1) == output_1)
print(length_of_longest_substring(input_2) == output_2)
print(length_of_longest_substring(input_3) == output_3)