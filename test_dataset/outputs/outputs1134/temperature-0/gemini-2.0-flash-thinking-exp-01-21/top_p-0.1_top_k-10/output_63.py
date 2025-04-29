def find_peak_element_linear(nums):
    n = len(nums)
    if n == 1:
        return 0
    for i in range(n):
        if i == 0:
            if nums[i] > nums[i+1]:
                return i
        elif i == n - 1:
            if nums[i] > nums[i-1]:
                return i
        else:
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
    return -1 # Should not reach here as per problem description

def find_peak_element_binary_search(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

def test_find_peak_element():
    test_cases = [
        ([1, 2, 3, 1], [2]),
        ([1, 2, 1, 3, 5, 6, 4], [1, 5]),
        ([1], [0]),
        ([1, 2], [1]),
        ([2, 1], [0]),
        ([1,2,3,4,5], [4]),
        ([5,4,3,2,1], [0]),
        ([3,2,1,5,6], [0, 4]),
        ([1,2,3,2,1], [2]),
    ]

    linear_correct_count = 0
    binary_correct_count = 0
    total_tests = len(test_cases)

    print("Linear Scan Tests:")
    for nums, expected_indices in test_cases:
        output_index = find_peak_element_linear(nums)
        if output_index in expected_indices:
            print("True")
            linear_correct_count += 1
        else:
            print("False")

    print(f"Linear Scan: {linear_correct_count}/{total_tests} correct")

    print("\nBinary Search Tests:")
    for nums, expected_indices in test_cases:
        output_index = find_peak_element_binary_search(nums)
        if output_index in expected_indices:
            print("True")
            binary_correct_count += 1
        else:
            print("False")

    print(f"Binary Search: {binary_correct_count}/{total_tests} correct")

if __name__ == '__main__':
    test_find_peak_element()