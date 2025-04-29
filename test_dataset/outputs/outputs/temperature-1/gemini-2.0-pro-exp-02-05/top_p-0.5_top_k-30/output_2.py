def lengthOfLongestSubstring(s):
    char_index_map = {}
    max_length = 0
    start = 0

    for end, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length

def run_tests(s, expected):
    result = lengthOfLongestSubstring(s)
    return result == expected

def main():
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
        test_result = run_tests(s, expected)
        print(test_result)
        if test_result:
            correct_count += 1

    print(f"{correct_count}/{total_tests}")

if __name__ == "__main__":
    main()