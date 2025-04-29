def solve():
    s = input()

    def is_palindrome(text):
        return text == text[::-1]

    if is_palindrome(s):
        print(1)
    else:
        print(2)

def test_solve():
    test_cases = [
        ("ababa", 1),
        ("abb", 2),
        ("baabb", 2),
        ("a", 1),
        ("b", 1),
        ("aba", 1),
        ("bab", 1),
        ("aa", 1),
        ("bb", 1),
        ("ab", 2),
        ("ba", 2),
        ("aabb", 2),
        ("abab", 2),
        ("baba", 2),
        ("bbba", 2),
        ("abbb", 2),
        ("aaaa", 1),
        ("bbbb", 1),
        ("aabbbbaa", 1),
        ("aabbbaa", 2),
        ("aabbaa", 1),
        ("aabbbab", 2)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for input_s, expected_output in test_cases:
        def is_palindrome_test(text):
            return text == text[::-1]

        if is_palindrome_test(input_s):
            actual_output = 1
        else:
            actual_output = 2

        if actual_output == expected_output:
            print('True')
            correct_count += 1
        else:
            print('False')

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_solve()