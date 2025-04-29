def is_palindrome(s):
    return s == s[::-1]

def min_steps_to_empty(s):
    if not s:
        return 0
    if is_palindrome(s):
        return 1
    else:
        return 2

def run_tests():
    test_cases = [
        ("ababa", 1),
        ("abb", 2),
        ("baabb", 2),
        ("a", 1),
        ("b", 1),
        ("aba", 1),
        ("bab", 1),
        ("aabb", 2),
        ("abab", 2),
        ("abba", 1),
        ("bbba", 2),
        ("aaab", 2),
        ("aaaa", 1),
        ("bbbb", 1),
        ("ab", 2),
        ("ba", 2),
        ("bbab", 2),
        ("baba", 2),
        ("abbb", 2),
        ("baaa", 2),
    ]
    correct_count = 0
    for input_s, expected_output in test_cases:
        actual_output = min_steps_to_empty(input_s)
        if actual_output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")
    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()