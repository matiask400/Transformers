def is_palindrome(x):
    """
    Checks if an integer is a palindrome.

    Args:
        x: An integer.

    Returns:
        True if x is a palindrome, False otherwise.
    """
    if x < 0:
        return False
    
    original_x = x
    reversed_x = 0
    
    while x > 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x //= 10
    
    return original_x == reversed_x

def test_is_palindrome():
    """
    Tests the is_palindrome function with several test cases.
    """
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (-101, False),
        (0, True),
        (1, True),
        (12321, True),
        (12345, False),
        (11111, True),
        (1221, True)
    ]
    
    num_correct = 0
    total_tests = len(test_cases)
    
    for x, expected in test_cases:
        actual = is_palindrome(x)
        if actual == expected:
            print("True")
            num_correct += 1
        else:
            print("False")
    
    print(f"{num_correct}/{total_tests}")

if __name__ == "__main__":
    test_is_palindrome()