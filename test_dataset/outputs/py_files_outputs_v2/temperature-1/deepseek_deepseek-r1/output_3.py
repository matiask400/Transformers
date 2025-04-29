def lengthOfLongestSubstring(s):
    char_map = {}
    start = 0
    max_length = 0
    for end in range(len(s)):
        current_char = s[end]
        if current_char in char_map and char_map[current_char] >= start:
            start = char_map[current_char] + 1
        char_map[current_char] = end
        current_length = end - start + 1
        if current_length > max_length:
            max_length = current_length
    return max_length