def findMedianSortedArrays(nums1, nums2):
    """
    Finds the median of two sorted arrays.

    Args:
        nums1: The first sorted array.
        nums2: The second sorted array.

    Returns:
        The median of the two sorted arrays.
    """
    m, n = len(nums1), len(nums2)
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m

    low = 0
    high = m
    while low <= high:
        partitionX = (low + high) // 2
        partitionY = ((m + n + 1) // 2) - partitionX

        maxLeftX = nums1[partitionX - 1] if partitionX > 0 else float('-inf')
        minRightX = nums1[partitionX] if partitionX < m else float('inf')
        maxLeftY = nums2[partitionY - 1] if partitionY > 0 else float('-inf')
        minRightY = nums2[partitionY] if partitionY < n else float('inf')

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (m + n) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1
    return -1

def test_findMedianSortedArrays():
    """
    Tests the findMedianSortedArrays function with various inputs.
    """
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([1, 2], [1, 2], 1.5),
        ([1, 3], [2, 7], 2.5),
        ([1, 2, 3, 4], [5, 6, 7, 8], 4.0),
    ]
    passed = 0
    for nums1, nums2, expected_output in test_cases:
        output = findMedianSortedArrays(nums1, nums2)
        print(f'Test: {nums1} + {nums2} - {output} == {expected_output} - {output == expected_output}')
        if output == expected_output:
            passed += 1
    print(f'Passed {passed} out of {len(test_cases)} tests.')


test_findMedianSortedArrays()