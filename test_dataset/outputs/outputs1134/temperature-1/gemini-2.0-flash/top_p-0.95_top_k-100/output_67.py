def is_palindrome(x):
    """
    Given an integer x, return true if x is palindrome integer.

    An integer is a palindrome when it reads the same backward as forward.
    For example, 121 is palindrome while 123 is not.
    """
    if x < 0:
        return False
    
    original_number = x
    reversed_number = 0
    
    while x > 0:
        last_digit = x % 10
        reversed_number = (reversed_number * 10) + last_digit
        x = x // 10
        
    return original_number == reversed_number

def test_is_palindrome():
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (-101, False),
        (0, True),
        (5, True),
        (12321, True),
        (12345, False),
        (1000021, False)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for input_val, expected_output in test_cases:
        actual_output = is_palindrome(input_val)
        if actual_output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")
    
    print(f"{correct_count}/{total_count}")

test_is_palindrome()