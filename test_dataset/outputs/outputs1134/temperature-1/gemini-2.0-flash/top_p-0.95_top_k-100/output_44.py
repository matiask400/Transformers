def remove_palindromic_subsequences(s):
    """
    Given a string s consisting only of letters 'a' and 'b'. In a single step you can remove one palindromic subsequence from s.
    Return the minimum number of steps to make the given string empty.

    Args:
        s (str): The input string consisting of 'a' and 'b'.

    Returns:
        int: The minimum number of steps to make the given string empty.
    """
    if not s:
        return 0
    if s == s[::-1]:
        return 1
    else:
        return 2

def test_remove_palindromic_subsequences():
    test_cases = [
        ("ababa", 1),
        ("abb", 2),
        ("baabb", 2),
        ("abba", 1),
        ("a", 1),
        ("b", 1),
        ("abab", 2),
        ("", 0)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for s, expected in test_cases:
        result = remove_palindromic_subsequences(s)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_remove_palindromic_subsequences()