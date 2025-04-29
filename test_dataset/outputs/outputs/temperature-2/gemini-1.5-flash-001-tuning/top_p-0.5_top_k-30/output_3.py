def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
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
        
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == m else nums1[partitionX]
        
        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == n else nums2[partitionY]
        
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (m + n) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1
    return 0.0

def test_findMedianSortedArrays():
    test_cases = [
        ([1,3], [2], 2.0),
        ([1,2], [3,4], 2.5),
        ([0,0], [0,0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([1,2,3,4,5], [6,7,8,9,10], 5.5),
        ([1,2,3,4,5], [6,7,8,9,10,11], 6.0),
    ]
    passed = 0
    for nums1, nums2, expected in test_cases:
        result = findMedianSortedArrays(nums1, nums2)
        print(f"Test: {nums1} + {nums2} -> {expected} == {result} -> {result == expected}")
        if result == expected:
            passed += 1
    print(f"Passed {passed} out of {len(test_cases)} tests.")

test_findMedianSortedArrays()