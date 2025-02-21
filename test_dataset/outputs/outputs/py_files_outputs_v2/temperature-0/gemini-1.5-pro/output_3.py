def length_of_longest_substring(s):
    char_set = set()
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length


# Test cases
input_1 = "abcabcbb"
output_1 = 3
input_2 = "bbbbb"
output_2 = 1
input_3 = "pwwkew"
output_3 = 3

print(length_of_longest_substring(input_1) == output_1)
print(length_of_longest_substring(input_2) == output_2)
print(length_of_longest_substring(input_3) == output_3)