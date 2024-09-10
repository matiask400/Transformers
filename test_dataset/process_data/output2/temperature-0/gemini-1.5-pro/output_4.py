def find_median_sorted_arrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m
    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and nums2[j - 1] > nums1[i]:
            imin = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            imax = i - 1
        else:
            if i == 0:
                max_left = nums2[j - 1]
            elif j == 0:
                max_left = nums1[i - 1]
            else:
                max_left = max(nums1[i - 1], nums2[j - 1])
            if (m + n) % 2 == 1:
                return max_left
            if i == m:
                min_right = nums2[j]
            elif j == n:
                min_right = nums1[i]
            else:
                min_right = min(nums1[i], nums2[j])
            return (max_left + min_right) / 2.0


# Test cases
inputs = [
    ([1, 3], [2]),
    ([1, 2], [3, 4]),
    ([0, 0], [0, 0]),
    ([], [1]),
    ([2], []),
]
outputs = [
    2.00000,
    2.50000,
    0.00000,
    1.00000,
    2.00000,
]

for i in range(len(inputs)):
    output = find_median_sorted_arrays(inputs[i][0], inputs[i][1])
    print(output == outputs[i])