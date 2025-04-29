def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    if m == 0:
        if n %2 ==1:
            return float(nums2[n//2])
        else:
            return (nums2[n//2 -1] + nums2[n//2])/2.0
    imin, imax, half_len = 0, m, (m + n +1)//2
    while imin <= imax:
        i = (imin + imax)//2
        j = half_len - i
        if i < m and nums2[j-1] > nums1[i]:
            imin = i +1
        elif i >0 and nums1[i-1] > nums2[j]:
            imax = i -1
        else:
            if i ==0:
                max_of_left = nums2[j-1]
            elif j ==0:
                max_of_left = nums1[i-1]
            else:
                max_of_left = max(nums1[i-1], nums2[j-1])
            if (m + n) %2 ==1:
                return float(max_of_left)
            if i ==m:
                min_of_right = nums2[j]
            elif j ==n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])
            return (max_of_left + min_of_right)/2.0

if __name__ == "__main__":
    test_cases = [
        # Example 1
        {
            "nums1": [1,3],
            "nums2": [2],
            "expected": 2.00000
        },
        # Example 2
        {
            "nums1": [1,2],
            "nums2": [3,4],
            "expected": 2.50000
        },
        # Example 3
        {
            "nums1": [0,0],
            "nums2": [0,0],
            "expected": 0.00000
        },
        # Example 4
        {
            "nums1": [],
            "nums2": [1],
            "expected": 1.00000
        },
        # Example 5
        {
            "nums1": [2],
            "nums2": [],
            "expected": 2.00000
        },
        # Additional Test Cases
        {
            "nums1": [1, 3, 8, 9, 15],
            "nums2": [7, 11, 18, 19, 21, 25],
            "expected": 11.0
        },
        {
            "nums1": [1],
            "nums2": [2,3,4,5,6],
            "expected": 3.5
        },
        {
            "nums1": [1,2,3],
            "nums2": [4,5,6},
            "expected": 3.5
        },
    ]
    correct = 0
    total = len(test_cases)
    for case in test_cases:
        nums1 = case["nums1"]
        nums2 = case["nums2"]
        expected = case["expected"]
        result = findMedianSortedArrays(nums1, nums2)
        if abs(result - expected) < 1e-5:
            print(True)
            correct +=1
        else:
            print(False)
    print(f"{correct}/{total}")