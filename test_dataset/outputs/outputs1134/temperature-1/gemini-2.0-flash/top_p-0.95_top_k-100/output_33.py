def xorGame(nums):
    """
    Determines if Alice wins the XOR game, assuming both players play optimally.

    Args:
        nums: A list of non-negative integers written on a chalkboard.

    Returns:
        True if and only if Alice wins the game, assuming both players play optimally.
    """
    if len(nums) % 2 == 0:
        return True

    xor_sum = 0
    for num in nums:
        xor_sum ^= num

    return xor_sum == 0

def run_tests():
    """
    Runs several test cases for the xorGame function and prints the results.
    """
    test_cases = [
        ([1, 1, 2], False),
        ([0, 1, 2, 3], True),
        ([1, 2, 3], True),
        ([3,4,5,6,7], True),
        ([1,2], False),
        ([0], True),
        ([1], False),
        ([], True),
        ([1,1], True),
        ([1, 1, 2, 2], True)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for nums, expected in test_cases:
        actual = xorGame(nums)
        if actual == expected:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    run_tests()