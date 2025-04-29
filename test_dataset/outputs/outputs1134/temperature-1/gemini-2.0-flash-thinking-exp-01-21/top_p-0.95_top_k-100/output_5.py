def large_group_positions(s):
    """
    Finds the intervals of every large group in a string.

    Args:
        s: A string of lowercase letters.

    Returns:
        A list of intervals of large groups, sorted in increasing order by start index.
    """
    large_groups = []
    i = 0
    while i < len(s):
        start = i
        char = s[i]
        while i < len(s) and s[i] == char:
            i += 1
        end = i - 1
        if end - start + 1 >= 3:
            large_groups.append([start, end])
    return large_groups

def run_tests():
    """
    Runs test cases for the large_group_positions function.
    """
    test_cases = [
        {"input": "abbxxxxzzy", "expected_output": [[3, 6]]},
        {"input": "abc", "expected_output": []},
        {"input": "abcdddeeeeaabbbcd", "expected_output": [[3, 5], [6, 9], [12, 14]]},
        {"input": "aba", "expected_output": []},
        {"input": "nnnoraaaaa", "expected_output": [[0,2],[6,10]]},
        {"input": "aaaaabbbbbcccccc", "expected_output": [[0, 4], [5, 9], [10, 15]]},
        {"input": "abcde", "expected_output": []},
        {"input": "aaabbbaaa", "expected_output": [[0, 2], [3, 5], [6, 8]]},
        {"input": "aaa", "expected_output": [[0, 2]]},
        {"input": "aaaa", "expected_output": [[0, 3]]},
        {"input": "aabbcc", "expected_output": []},
        {"input": "zzzzz", "expected_output": [[0, 4]]},
        {"input": "aabbbaaa", "expected_output": [[2, 4], [5, 7]]},
        {"input": "bbbbaa", "expected_output": [[0, 2]]}
    ]

    correct_count = 0
    for i, test_case in enumerate(test_cases):
        input_s = test_case["input"]
        expected_output = test_case["expected_output"]
        actual_output = large_group_positions(input_s)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()