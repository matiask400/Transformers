def findMedianSortedArrays(nums1, nums2):
    """
    Finds the median of two sorted arrays.
    """
    m, n = len(nums1), len(nums2)
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m  # Ensure nums1 is shorter

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
            if (m + n) % 2 == 0:  # Even total elements
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:  # Odd total elements
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1

    return -1  # Should never reach here

def test_findMedianSortedArrays():
    test_cases = [
        ([1,3], [2], 2.00000),
        ([1,2], [3,4], 2.50000),
        ([0,0], [0,0], 0.00000),
        ([], [1], 1.00000),
        ([2], [], 2.00000),
        ([1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], 5.00000)
    ]

    passed_tests = 0

    for case in test_cases:
        result = findMedianSortedArrays(case[0], case[1])
        print(f"True: {result == case[2]}")
        if result == case[2]:
            passed_tests += 1

    print(f"Passed {passed_tests}/{len(test_cases)} tests")

test_findMedianSortedArrays()