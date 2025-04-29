def min_steps(s):
    if s == s[::-1]:
        return 1
    else:
        return 2

def run_tests():
    tests = [
        ("ababa", 1),
        ("abb", 2),
        ("baabb", 2),
        ("a", 1),
        ("b", 1),
        ("aaabbb", 2),
        ("aabccbaa", 1),
        ("abc", 2),
        ("abba", 1),
        ("abcba",1),
        ("abacaba",1),
        ("abab",2),
        ("aabb",2),
        ("ababab",2),
        ("", 0), # Edge case: empty string
    ]
    correct = 0
    total = len(tests)
    for s, expected in tests:
        result = min_steps(s)
        is_correct = result == expected
        print(is_correct)
        if is_correct:
            correct +=1
    print(f"{correct}/{total}")

run_tests()