def findMedianSortedArrays(nums1, nums2):
    merged = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1
    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    total_length = len(merged)
    if total_length % 2 == 0:
        return (merged[total_length // 2 - 1] + merged[total_length // 2]) / 2.0
    else:
        return float(merged[total_length // 2])

def run_tests(findMedianSortedArrays):
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([1,2,3], [4,5,6], 3.5)
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for nums1, nums2, expected in test_cases:
        result = findMedianSortedArrays(nums1, nums2)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"  Input: nums1 = {nums1}, nums2 = {nums2}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")

    print(f"{correct_count}/{total_tests}")

run_tests(findMedianSortedArrays)