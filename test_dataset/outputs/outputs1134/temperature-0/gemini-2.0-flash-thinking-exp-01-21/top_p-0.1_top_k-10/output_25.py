def find_median_sorted_arrays(nums1, nums2):
    m = len(nums1)
    n = len(nums2)

    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m

    low = 0
    high = m
    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (m + n + 1) // 2 - partitionX

        maxLeftX = nums1[partitionX - 1] if partitionX > 0 else -float('inf')
        minRightX = nums1[partitionX] if partitionX < m else float('inf')

        maxLeftY = nums2[partitionY - 1] if partitionY > 0 else -float('inf')
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

def test_find_median_sorted_arrays():
    test_cases = [
        (([1, 3], [2]), 2.0),
        (([1, 2], [3, 4]), 2.5),
        (([0, 0], [0, 0]), 0.0),
        (([], [1]), 1.0),
        (([2], []), 2.0),
        (([1, 2, 5], [3, 4]), 3.0),
        (([1, 2], [3, 4, 5, 6]), 3.5),
        (([100, 200], [1, 2, 3, 4]), 3.0),
        (([1, 2, 3, 4], [100, 200]), 3.0),
        (([1, 1, 1], [1, 1, 1]), 1.0),
    ]
    correct_count = 0
    for i, (input_arrays, expected_output) in enumerate(test_cases):
        nums1, nums2 = input_arrays
        output = find_median_sorted_arrays(nums1, nums2)
        if abs(output - expected_output) < 1e-5:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    test_find_median_sorted_arrays()