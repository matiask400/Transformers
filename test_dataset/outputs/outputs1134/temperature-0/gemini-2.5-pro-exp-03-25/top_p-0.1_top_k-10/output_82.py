import collections

def solve():
    """
    Solves the Next Greater Element I problem using a monotonic stack and a hash map.
    Finds the next greater element in nums2 for each element in nums1.
    """
    def nextGreaterElement(nums1, nums2):
        """
        Finds the next greater element for each element in nums1 within nums2.

        Args:
            nums1: A list of unique integers, a subset of nums2.
            nums2: A list of unique integers.

        Returns:
            A list where each element is the next greater element in nums2
            corresponding to the element in nums1 at the same index, or -1
            if no such element exists.
        """
        next_greater_map = {} # Stores {element: next_greater_element}
        stack = [] # Monotonic decreasing stack (stores elements from nums2)

        # Iterate through nums2 to precompute next greater elements
        for num in nums2:
            # While stack is not empty and current num is greater than stack top
            while stack and num > stack[-1]:
                # The current num is the next greater element for the stack top
                popped_num = stack.pop()
                next_greater_map[popped_num] = num
            # Push the current number onto the stack
            stack.append(num)

        # Any elements remaining in the stack have no next greater element in nums2
        # The .get() method below handles this by defaulting to -1

        # Build the result array for nums1
        result = []
        for num in nums1:
            # Look up the next greater element in the map
            # If not found (was left on stack or not processed), default to -1
            result.append(next_greater_map.get(num, -1))

        return result

    # --- Test Cases ---
    test_cases = [
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
        ([2, 4], [1, 2, 3, 4], [3, -1]),
        ([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7], [7, 7, 7, 7, 7]),
        ([1], [1, 2, 3], [2]),
        ([3], [1, 2, 3], [-1]),
        ([1,2], [1,2,3], [2,3]),
        ([4,1,2], [1,2,3,4], [-1,2,3]), # Test case where elements are not in increasing order in nums2
        ([3,1,5,7,9,2,6], [1,2,3,5,6,7,9,11], [5,2,6,9,11,3,7]) # More complex case
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (nums1_input, nums2_input, expected_output) in enumerate(test_cases):
        actual_output = nextGreaterElement(list(nums1_input), list(nums2_input)) # Pass copies
        result = actual_output == expected_output
        print(f"Test Case {i+1}: {result}")
        if result:
            correct_count += 1

    print(f"\n{correct_count} / {total_tests} correct tests.")

# Execute the solution and tests
solve()