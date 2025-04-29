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

def run_tests(tests):
    correct_count = 0
    total_tests = len(tests)

    for i, (input_s, expected_output) in enumerate(tests):
        result = lengthOfLongestSubstring(input_s)
        if result == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")

    print(f"{correct_count}/{total_tests} tests correct")

if __name__ == "__main__":
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("dvdf", 3),
        ("au", 2)
    ]
    run_tests(tests)