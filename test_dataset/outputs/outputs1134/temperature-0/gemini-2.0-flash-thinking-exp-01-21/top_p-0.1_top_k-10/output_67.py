def isPalindrome(x):
    """
    Given an integer x, return true if x is palindrome integer.

    An integer is a palindrome when it reads the same backward as forward.
    For example, 121 is palindrome while 123 is not.

    Args:
        x (int): An integer.

    Returns:
        bool: True if x is a palindrome, False otherwise.
    """
    if x < 0:
        return False
    if x == 0:
        return True

    original_x = x
    reversed_x = 0
    while x > 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x = x // 10

    return original_x == reversed_x

def run_tests():
    test_cases = [
        {"input": 121, "expected": True},
        {"input": -121, "expected": False},
        {"input": 10, "expected": False},
        {"input": -101, "expected": False},
        {"input": 0, "expected": True},
        {"input": 1, "expected": True},
        {"input": 12321, "expected": True},
        {"input": 12345, "expected": False},
        {"input": 1001, "expected": True},
        {"input": -1, "expected": False},
        {"input": 5, "expected": True},
        {"input": 11, "expected": True},
        {"input": 222, "expected": True},
        {"input": 1221, "expected": True},
        {"input": 123321, "expected": True},
        {"input": 1234321, "expected": True},
        {"input": 123456, "expected": False},
    ]

    correct_count = 0
    for i, test_case in enumerate(test_cases):
        input_x = test_case["input"]
        expected_output = test_case["expected"]
        actual_output = isPalindrome(input_x)
        if actual_output == expected_output:
            print(True)
            correct_count += 1
        else:
            print(False)
    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()