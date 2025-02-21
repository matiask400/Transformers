def length_of_longest_substring(s: str) -> int:
    char_map = {}
    left = max_length = 0
    for right in range(len(s)):
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)
    return max_length

# Example 1
test_input_1 = "abcabcbb"
expected_output_1 = 3
print(length_of_longest_substring(test_input_1) == expected_output_1)  # True

# Example 2
test_input_2 = "bbbbb"
expected_output_2 = 1
print(length_of_longest_substring(test_input_2) == expected_output_2)  # True

# Example 3
test_input_3 = "pwwkew"
expected_output_3 = 3
print(length_of_longest_substring(test_input_3) == expected_output_3)  # True

# Example 4
test_input_4 = ""
expected_output_4 = 0
print(length_of_longest_substring(test_input_4) == expected_output_4)  # True