def nextGreaterElement(nums1, nums2):
    """
    Finds the next greater numbers for nums1's elements in nums2.

    Args:
        nums1: An integer array of unique elements, a subset of nums2.
        nums2: An integer array of unique elements.

    Returns:
        A list of the next greater numbers for each element in nums1.
    """
    result = []
    for num1 in nums1:
        found = False
        for i in range(nums2.index(num1) + 1, len(nums2)):
            if nums2[i] > num1:
                result.append(nums2[i])
                found = True
                break
        if not found:
            result.append(-1)
    return result

def test_nextGreaterElement():
    """
    Tests the nextGreaterElement function with several test cases.
    """
    test_cases = [
        (([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1]),
        (([2, 4], [1, 2, 3, 4]), [3, -1]),
        (([1,3,5,2,4], [6,5,4,3,2,1,7]), [7,7,7,7,7]),
        (([1,3,5,2,4], [5,4,3,2,1]), [-1,-1,-1,-1,-1]),
        (([1,3,5,2,4], [1,2,3,4,5]), [2,4,-1,-1,5]),
        (([1], [1,2,3,4,5]), [-1]),
        (([5], [1,2,3,4,5]), [-1]),
        (([5], [5]), [-1]),
        (([1,2,3], [1,2,3]), [-1,-1,-1]),
        (([3,2,1], [1,2,3]), [ -1, -1, -1])
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (input_data, expected_output) in enumerate(test_cases):
        nums1, nums2 = input_data
        actual_output = nextGreaterElement(nums1, nums2)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Input: {input_data}, Expected: {expected_output}, Actual: {actual_output})")

    print(f"\nCorrect: {correct_count}/{total_count}")

if __name__ == "__main__":
    test_nextGreaterElement()