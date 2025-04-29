def next_greater_element(nums1, nums2):
    """
    Finds the next greater numbers for nums1's elements in nums2.

    Args:
        nums1: An integer array of unique elements, a subset of nums2.
        nums2: An integer array of unique elements.

    Returns:
        A list of next greater numbers for each element in nums1.
    """
    result = []
    for n1 in nums1:
        n1_index_in_nums2 = -1
        for i in range(len(nums2)):
            if nums2[i] == n1:
                n1_index_in_nums2 = i
                break

        next_greater = -1
        for i in range(n1_index_in_nums2 + 1, len(nums2)):
            if nums2[i] > n1:
                next_greater = nums2[i]
                break
        result.append(next_greater)
    return result

def run_tests():
    test_cases = [
        {
            "nums1": [4, 1, 2],
            "nums2": [1, 3, 4, 2],
            "expected_output": [-1, 3, -1]
        },
        {
            "nums1": [2, 4],
            "nums2": [1, 2, 3, 4],
            "expected_output": [3, -1]
        },
        {
            "nums1": [1],
            "nums2": [1, 2, 3],
            "expected_output": [2]
        },
        {
            "nums1": [3],
            "nums2": [1, 2, 3],
            "expected_output": [-1]
        },
        {
            "nums1": [1, 3, 5, 2, 4],
            "nums2": [6, 5, 4, 3, 2, 1, 7],
            "expected_output": [7, 7, 7, 7, 7]
        },
        {
            "nums1": [5, 4, 3, 2, 1],
            "nums2": [6, 5, 4, 3, 2, 1, 7],
            "expected_output": [7, 7, 7, 7, 7]
        },
        {
            "nums1": [6, 7],
            "nums2": [6, 5, 4, 3, 2, 1, 7],
            "expected_output": [7, -1]
        },
        {
            "nums1": [1, 3, 5, 2, 4],
            "nums2": [2, 4, 6, 8, 1, 3, 5, 7],
            "expected_output": [3, 5, 7, 4, 5]
        }
    ]

    correct_count = 0
    for i, test_case in enumerate(test_cases):
        nums1 = test_case["nums1"]
        nums2 = test_case["nums2"]
        expected_output = test_case["expected_output"]
        actual_output = next_greater_element(nums1, nums2)
        if actual_output == expected_output:
            print(f'Test {i+1}: True')
            correct_count += 1
        else:
            print(f'Test {i+1}: False')
    print(f'{correct_count}/{len(test_cases)}')

if __name__ == '__main__':
    run_tests()