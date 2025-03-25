def findMedianSortedArrays(nums1, nums2):
    """
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

    Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

    Example 3:
    Input: nums1 = [0,0], nums2 = [0,0]
    Output: 0.00000

    Example 4:
    Input: nums1 = [], nums2 = [1]
    Output: 1.00000

    Example 5:
    Input: nums1 = [2], nums2 = []
    Output: 2.00000

    Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106
    Follow up: The overall run time complexity should be O(log (m+n)).
    """
    merged_array = sorted(nums1 + nums2)
    total_length = len(merged_array)
    if total_length % 2 == 0:
        mid1 = merged_array[total_length // 2 - 1]
        mid2 = merged_array[total_length // 2]
        return (mid1 + mid2) / 2.0
    else:
        return float(merged_array[total_length // 2])

def test_findMedianSortedArrays():
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0)
    ]
    
    correct_count = 0
    total_tests = len(test_cases)
    
    for nums1, nums2, expected_output in test_cases:
        result = findMedianSortedArrays(nums1, nums2)
        if abs(result - expected_output) < 1e-5:  # Account for potential floating-point inaccuracies
            print(True)
            correct_count += 1
        else:
            print(False)

    print(f"{correct_count}/{total_tests}")

if __name__ == '__main__':
    test_findMedianSortedArrays()