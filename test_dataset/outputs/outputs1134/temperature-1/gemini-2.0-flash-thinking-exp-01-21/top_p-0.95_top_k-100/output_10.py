def count_substrings_with_abc(s):
    count = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if 'a' in substring and 'b' in substring and 'c' in substring:
                count += 1
    return count

def run_tests():
    tests = [
        {"input": "abcabc", "expected_output": 10},
        {"input": "aaacb", "expected_output": 3},
        {"input": "abc", "expected_output": 1},
        {"input": "abca", "expected_output": 3},
        {"input": "abcb", "expected_output": 2},
        {"input": "abcc", "expected_output": 3},
        {"input": "aabbcc", "expected_output": 10},
        {"input": "bacbab", "expected_output": 7},
        {"input": "cabacba", "expected_output": 22},
        {"input": "cccaaaabbbccc", "expected_output": 36}
    ]
    correct_tests = 0
    for i, test in enumerate(tests):
        input_s = test["input"]
        expected_output = test["expected_output"]
        actual_output = count_substrings_with_abc(input_s)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
    print(f"{correct_tests}/{len(tests)}")

if __name__ == '__main__':
    run_tests()