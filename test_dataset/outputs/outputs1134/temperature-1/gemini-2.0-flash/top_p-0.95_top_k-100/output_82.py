def nextGreaterElement(nums1, nums2):
    """
    Finds the next greater numbers for nums1's elements in the corresponding places of nums2.

    Args:
        nums1: An integer array of unique elements, which is a subset of nums2.
        nums2: An integer array of unique elements.

    Returns:
        A list of the next greater numbers for nums1's elements in nums2.
    """
    result = []
    for num1 in nums1:
        found = False
        greater = -1
        for i in range(len(nums2)):
            if nums2[i] == num1:
                found = True
            if found and nums2[i] > num1:
                greater = nums2[i]
                break
        result.append(greater)
    return result

def test_nextGreaterElement():
    """
    Tests the nextGreaterElement function with several test cases.
    """
    test_cases = [
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
        ([2, 4], [1, 2, 3, 4], [3, -1]),
        ([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7], [7, 7, 7, 7, 7]),
        ([1, 3, 5, 2, 4], [5, 4, 3, 2, 1], [-1, -1, -1, -1, -1]),
        ([1,2,3,4], [4,3,2,1], [-1, -1, -1, -1]),
        ([1], [1,2,3,4], [-1]),
        ([4], [1,2,3,4], [-1]),
        ([4], [4,3,2,1], [-1]),
    ]

    correct_count = 0
    for i, (nums1, nums2, expected) in enumerate(test_cases):
        actual = nextGreaterElement(nums1, nums2)
        if actual == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Actual: {actual})")
    
    print(f"\nCorrect tests: {correct_count}/{len(test_cases)}")

if __name__ == "__main__":
    test_nextGreaterElement()