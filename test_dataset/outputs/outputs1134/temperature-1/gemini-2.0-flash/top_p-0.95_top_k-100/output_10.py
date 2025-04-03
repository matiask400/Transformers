def count_substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            if 'a' in sub and 'b' in sub and 'c' in sub:
                count += 1
    return count

def test_count_substrings():
    test_cases = [
        ("abcabc", 10),
        ("aaacb", 3),
        ("abc", 1),
        ("abca", 3),
        ("abcbaaabcabc", 55)
    ]
    
    num_correct = 0
    total_tests = len(test_cases)
    
    for input_str, expected_output in test_cases:
        actual_output = count_substrings(input_str)
        if actual_output == expected_output:
            print("True")
            num_correct += 1
        else:
            print("False")
    
    print(f"{num_correct}/{total_tests}")

if __name__ == "__main__":
    test_count_substrings()