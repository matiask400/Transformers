def solve():
    def get_prefix_end(s):
        if not s:
            return -1
        char = s[0]
        for i in range(len(s)):
            if s[i] != char:
                return i - 1
        return len(s) - 1

    def get_suffix_start(s):
        if not s:
            return 0
        char = s[-1]
        for i in range(len(s) - 1, -1, -1):
            if s[i] != char:
                return i + 1
        return 0

    def get_min_length(s):
        current_s = s
        while True:
            if len(current_s) < 2:
                break
            prefix_end = get_prefix_end(current_s)
            suffix_start = get_suffix_start(current_s)
            if prefix_end < suffix_start and current_s[0] == current_s[-1]:
                current_s = current_s[prefix_end+1:suffix_start]
            else:
                break
        return len(current_s)

    def run_test(s, expected_output):
        output = get_min_length(s)
        if output == expected_output:
            print('True')
        else:
            print('False')

    # Example 1
    run_test("ca", 2)

    # Example 2
    run_test("cabaabac", 0)

    # Example 3
    run_test("aabccabba", 3)

    # Additional tests
    run_test("aaaaa", 0)
    run_test("abc", 3)
    run_test("aba", 1)
    run_test("aabbbaa", 0)
    run_test("aabbaa", 0)
    run_test("aabbcbaa", 2)
    run_test("aabbccaa", 0)
    run_test("bab", 1)
    run_test("bbbab", 1)
    run_test("bbbb", 0)
    run_test("b", 1)
    run_test("", 0)
    run_test("aaa", 1)
    run_test("abca", 2)
    run_test("abcba", 1)
    run_test("abccba", 0)
    run_test("aabbccddeeffgg", 16)
    run_test("aabbccddeeffgga", 15)
    run_test("aaabbbaaa", 1)

    test_cases = [
        ("ca", 2),
        ("cabaabac", 0),
        ("aabccabba", 3),
        ("aaaaa", 0),
        ("abc", 3),
        ("aba", 1),
        ("aabbbaa", 0),
        ("aabbaa", 0),
        ("aabbcbaa", 2),
        ("aabbccaa", 0),
        ("bab", 1),
        ("bbbab", 1),
        ("bbbb", 0),
        ("b", 1),
        ("", 0),
        ("aaa", 1),
        ("abca", 2),
        ("abcba", 1),
        ("abccba", 0),
        ("aabbccddeeffgg", 16),
        ("aabbccddeeffgga", 15),
        ("aaabbbaaa", 1)
    ]

    correct_count = 0
    for s, expected in test_cases:
        output = get_min_length(s)
        if output == expected:
            print('True')
            correct_count += 1
        else:
            print('False')

    print(f"{correct_count}/{len(test_cases)}")

solve()