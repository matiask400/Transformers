def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

# Test cases
inputs = ["abcabcbb", "bbbbb", "pwwkew"]
outputs = [3, 1, 3]
for i in range(len(inputs)):
    result = length_of_longest_substring(inputs[i])
    print(result == outputs[i])