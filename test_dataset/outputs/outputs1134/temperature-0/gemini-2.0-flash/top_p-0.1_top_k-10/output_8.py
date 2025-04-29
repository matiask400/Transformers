def move_zeroes(nums):
    """
    Moves all 0's to the end of the array while maintaining the relative order of the non-zero elements.

    Args:
        nums: An integer array.
    """
    n = len(nums)
    j = 0  # Index for non-zero elements

    for i in range(n):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

    # Fill the remaining elements with 0
    for i in range(j, n):
        nums[i] = 0


def test_move_zeroes():
    """
    Tests the move_zeroes function with several test cases.
    """
    test_cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
        ([1, 0, 0, 0, 0], [1, 0, 0, 0, 0]),
        ([0, 0, 0, 0, 1], [1, 0, 0, 0, 0]),
        ([4,2,4,0,0,3,0,5,1,0], [4,2,4,3,5,1,0,0,0,0])
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (input_nums, expected_output) in enumerate(test_cases):
        nums = input_nums[:]  # Create a copy to avoid modifying the original test case
        move_zeroes(nums)
        if nums == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: {input_nums}")
            print(f"  Expected: {expected_output}")
            print(f"  Actual: {nums}")

    print(f"\nCorrect: {correct_count}/{total_count}")


if __name__ == "__main__":
    test_move_zeroes()