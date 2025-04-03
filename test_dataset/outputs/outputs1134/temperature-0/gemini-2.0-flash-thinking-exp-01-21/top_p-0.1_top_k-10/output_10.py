def count_substrings(s):
    count = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if 'a' in substring and 'b' in substring and 'c' in substring:
                count += 1
    return count

def run_tests():
    test_cases = [
        {"input": "abcabc", "expected_output": 10},
        {"input": "aaacb", "expected_output": 3},
        {"input": "abc", "expected_output": 1},
        {"input": "abca", "expected_output": 3},
        {"input": "abcb", "expected_output": 2},
        {"input": "abcc", "expected_output": 2},
        {"input": "aabbcc", "expected_output": 10},
        {"input": "bacbab", "expected_output": 7},
        {"input": "cababc", "expected_output": 10},
        {"input": "cbaabc", "expected_output": 10},
        {"input": "acbacb", "expected_output": 10},
        {"input": "bcabca", "expected_output": 10},
        {"input": "aaaaabbbbcccc", "expected_output": 66}
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        input_s = test_case["input"]
        expected_output = test_case["expected_output"]
        actual_output = count_substrings(input_s)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")

    print(f"\nCorrect tests: {correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()