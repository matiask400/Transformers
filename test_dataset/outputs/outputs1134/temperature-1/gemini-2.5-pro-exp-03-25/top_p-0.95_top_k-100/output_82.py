import sys 
# Setting higher recursion depth for potential edge cases, though likely not needed for constraints.
# sys.setrecursionlimit(2000) 

def solve():
    """
    Solves the Next Greater Element I problem and runs tests.
    """

    def nextGreaterElement(nums1, nums2):
        """
        Finds the next greater element for each element in nums1 within nums2.

        Args:
            nums1: A list of unique integers, subset of nums2.
            nums2: A list of unique integers.

        Returns:
            A list where the i-th element is the next greater element in nums2
            for nums1[i], or -1 if none exists.
        """
        
        # O(nums2.length) space and time using monotonic stack
        next_greater_map = {} # Dictionary to store next greater element for each num in nums2
        stack = []            # Monotonic decreasing stack (stores elements from nums2)

        # Iterate through nums2 from right to left to find the next greater element for each number
        for num in reversed(nums2):
            # Pop elements from stack that are less than or equal to the current number.
            # These elements cannot be the next greater element for 'num' (as 'num' is greater/equal and to their left)
            # and they cannot be the next greater element for numbers further left than 'num' 
            # (as 'num' is closer and greater/equal).
            while stack and stack[-1] <= num:
                stack.pop()
            
            # After popping, if the stack is empty, 'num' has no greater element to its right.
            # Otherwise, the top of the stack is the first greater element to the right of 'num'.
            if not stack:
                next_greater_map[num] = -1
            else:
                next_greater_map[num] = stack[-1]
            
            # Push the current number onto the stack. It might be the next greater element
            # for numbers appearing earlier (to the left) in nums2.
            stack.append(num)

        # O(nums1.length) time to lookup results
        # Construct the result list by looking up each element of nums1 in the map.
        result = [next_greater_map[num] for num in nums1]
        
        return result

    # --- Test Runner ---
    test_cases = [
        # Format: ( (nums1, nums2), expected_output )
        (([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1]),
        (([2, 4], [1, 2, 3, 4]), [3, -1]),
        (([], [1, 2, 3]), []), # Empty nums1
        (([1], [1]), [-1]), # Single element lists
        (([1, 2], [1, 2, 3]), [2, 3]), # Ascending nums2
        (([3, 2, 1], [3, 2, 1]), [-1, -1, -1]), # Descending nums2
        (([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]), [7, 7, 7, 7, 7]), # More complex case
        (([6], [6, 5, 4, 3, 2, 1, 7]), [7]), # Element at start
        (([7], [6, 5, 4, 3, 2, 1, 7]), [-1]), # Element at end
        (([1, 2, 3], [3, 1, 2]), [-1, -1, -1]) # Permutation
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, (inputs, expected) in enumerate(test_cases):
        nums1_test, nums2_test = inputs
        # Make copies to avoid modifying original test case data if function mutates input (though this one doesn't)
        nums1_copy = list(nums1_test) 
        nums2_copy = list(nums2_test)
        
        try:
            actual = nextGreaterElement(nums1_copy, nums2_copy)
            passed = (actual == expected)
            print(f"{passed}")
            if passed:
                num_correct += 1
        except Exception as e:
            print(f"False  # Error occurred: {e}")

    print(f"{num_correct} / {total_tests} correct")

# Execute the solve function which includes the test runner
solve()