def lengthOfLongestSubstring(s):
    char_index_map = {}
    start = 0
    max_length = 0

    for end, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length

def run_tests(lengthOfLongestSubstring):
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3)
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for s, expected in test_cases:
        result = lengthOfLongestSubstring(s)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"  Input: s = \"{s}\"")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")

    print(f"{correct_count}/{total_tests}")

run_tests(lengthOfLongestSubstring)