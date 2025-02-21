def length_of_longest_substring(s: str) -> int:
    char_map = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_map:
            left = max(left, char_map[s[right]] + 1)
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

# Test cases
inputs = ["abcabcbb", "bbbbb", "pwwkew", ""]
expected_outputs = [3, 1, 3, 0]

for i, input_str in enumerate(inputs):
    result = length_of_longest_substring(input_str)
    print(result == expected_outputs[i])