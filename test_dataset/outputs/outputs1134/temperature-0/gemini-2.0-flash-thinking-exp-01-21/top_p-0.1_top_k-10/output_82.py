def nextGreaterElement(nums1, nums2):
    """
    Finds the next greater number for each element in nums1 in nums2.

    Args:
        nums1: An integer array of unique elements, a subset of nums2.
        nums2: An integer array of unique elements.

    Returns:
        A list of next greater numbers for each element in nums1.
    """
    next_greater_map = {}
    stack = []

    for num in nums2:
        while stack and stack[-1] < num:
            next_greater_map[stack.pop()] = num
        stack.append(num)

    while stack:
        next_greater_map[stack.pop()] = -1

    result = []
    for num in nums1:
        result.append(next_greater_map[num])
    return result

def run_tests():
    tests = [
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
            "nums2": [1, 2, 3, 4],
            "expected_output": [-1]
        },
        {
            "nums1": [4],
            "nums2": [1, 2, 3, 4],
            "expected_output": [-1]
        },
        {
            "nums1": [1, 2, 3, 4],
            "nums2": [1, 2, 3, 4],
            "expected_output": [-1, -1, -1, -1]
        },
        {
            "nums1": [1, 3, 5, 2, 4],
            "nums2": [6, 5, 4, 3, 2, 1, 7],
            "expected_output": [7, 7, 7, 7, 7]
        },
        {
            "nums1": [5, 3, 1],
            "nums2": [6, 5, 4, 3, 2, 1, 7],
            "expected_output": [7, 4, 2]
        }
    ]

    correct_tests = 0
    for i, test in enumerate(tests):
        nums1 = test["nums1"]
        nums2 = test["nums2"]
        expected_output = test["expected_output"]
        actual_output = nextGreaterElement(nums1, nums2)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
    print(f"{correct_tests}/{len(tests)}")

if __name__ == '__main__':
    run_tests()