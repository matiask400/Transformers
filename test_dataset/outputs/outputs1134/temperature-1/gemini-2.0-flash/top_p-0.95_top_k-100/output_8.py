def move_zeroes(nums):
    """
    Moves all 0's to the end of an array while maintaining the relative order of the non-zero elements.

    Args:
      nums: A list of integers.
    """
    n = len(nums)
    j = 0  # Index for non-zero elements
    for i in range(n):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

    # Fill the remaining elements with 0's
    for i in range(j, n):
        nums[i] = 0


def test_move_zeroes():
    """Tests the move_zeroes function."""
    tests = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
        ([1, 0, 1, 0, 1], [1, 1, 1, 0, 0]),
        ([1, 0], [1, 0]),
        ([0,1],[1,0])
    ]

    correct_tests = 0
    total_tests = len(tests)

    for i, (input_nums, expected_output) in enumerate(tests):
        nums = input_nums[:]  # Create a copy to avoid modifying the original test case
        move_zeroes(nums)
        if nums == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False (Input: {input_nums}, Output: {nums}, Expected: {expected_output})")

    print(f"\n{correct_tests}/{total_tests} correct")


if __name__ == "__main__":
    test_move_zeroes()