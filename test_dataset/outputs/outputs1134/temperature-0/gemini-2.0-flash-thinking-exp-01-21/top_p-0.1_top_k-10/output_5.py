def largeGroupPositions(s):
    """
    Finds the intervals of every large group in a string.

    Args:
        s: A string of lowercase letters.

    Returns:
        A list of intervals of large groups, sorted in increasing order by start index.
    """
    large_groups = []
    start_index = 0
    i = 0
    while i < len(s):
        char = s[i]
        j = i
        while j < len(s) and s[j] == char:
            j += 1
        if j - i >= 3:
            large_groups.append([i, j - 1])
        i = j
    return large_groups

def run_tests():
    test_cases = [
        {"input": "abbxxxxzzy", "expected_output": [[3, 6]]},
        {"input": "abc", "expected_output": []},
        {"input": "abcdddeeeeaabbbcd", "expected_output": [[3, 5], [6, 9], [12, 14]]},
        {"input": "aba", "expected_output": []},
        {"input": "nnn", "expected_output": [[0, 2]]},
        {"input": "nnnaaa", "expected_output": [[0, 2], [3, 5]]},
        {"input": "aaaabbbcdddeee", "expected_output": [[0, 3], [7, 9], [10, 12]]},
        {"input": "aaaa", "expected_output": [[0, 3]]},
        {"input": "aabbcc", "expected_output": []},
        {"input": "aabbccc", "expected_output": [[4, 6]]},
        {"input": "aaabbbccc", "expected_output": [[0, 2], [3, 5], [6, 8]]},
        {"input": "a", "expected_output": []},
        {"input": "aa", "expected_output": []},
        {"input": "aaa", "expected_output": [[0, 2]]},
        {"input": "", "expected_output": []},
    ]

    correct_tests = 0
    for i, test_case in enumerate(test_cases):
        input_s = test_case["input"]
        expected_output = test_case["expected_output"]
        actual_output = largeGroupPositions(input_s)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
    print(f"{correct_tests}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()