import sys
import io

def solve():
    """
    Solves the Missing Number problem.
    Finds the missing number in an array containing n distinct numbers
    in the range [0, n]. Uses O(1) extra space and O(n) runtime.
    """

    def missingNumber(nums: list[int]) -> int:
        """
        Given an array nums containing n distinct numbers in the range [0, n],
        return the only number in the range that is missing from the array.

        Uses the XOR approach for O(n) time and O(1) space.
        """
        n = len(nums)
        # Initialize missing with n because the range is [0, n]
        # and the loop iterates indices from 0 to n-1.
        # The number n is part of the expected full range but not an index.
        missing = n
        for i in range(n):
            # XOR the index i (representing the expected number at this position
            # if the array were complete and sorted) and the actual number nums[i].
            # If a number `x` is present, it will be XORed twice (once as `i`
            # if it's in its "correct" place, or later as `nums[j]`, and once
            # as `nums[i]`). The `x ^ x` cancels out.
            # The missing number will only be XORed once (as an index `i`
            # when we iterate up to `n`) and will remain in the `missing` variable.
            # The number `n` is initially in `missing` and is never XORed as `nums[i]`
            # (since indices only go up to n-1). If `n` is the missing number,
            # all other numbers [0...n-1] will cancel out, leaving `n`.
            # If another number `m` is missing, `n` will be XORed with `n`
            # (from the index loop when i=m, and from nums[j] where nums[j]=n),
            # cancelling `n` out, and `m` will remain.
            missing ^= i ^ nums[i]
        return missing

    # --- Alternative Solution using Summation ---
    # def missingNumber_sum(nums: list[int]) -> int:
    #     """
    #     Alternative solution using summation. O(n) time, O(1) space.
    #     Might be prone to overflow for very large n, but fine for constraints.
    #     """
    #     n = len(nums)
    #     expected_sum = n * (n + 1) // 2
    #     actual_sum = sum(nums)
    #     return expected_sum - actual_sum

    # --- Test Cases ---
    test_cases = [
        {"input": ([3, 0, 1]), "expected": 2},
        {"input": ([0, 1]), "expected": 2},
        {"input": ([9, 6, 4, 2, 3, 5, 7, 0, 1]), "expected": 8},
        {"input": ([0]), "expected": 1},
        {"input": ([1]), "expected": 0}, # Edge case: missing 0
        {"input": (list(range(100))), "expected": 100}, # Missing n
        {"input": ([i for i in range(101) if i != 50]), "expected": 50}, # Missing middle
        {"input": (list(range(1, 101))), "expected": 0}, # Missing 0
        # Larger test case within constraints (n=10000)
        {"input": (list(range(10000))), "expected": 10000},
        {"input": ([i for i in range(10001) if i != 9999]), "expected": 9999},
    ]

    correct_count = 0
    total_tests = len(test_cases)

    # --- Test Runner ---
    for i, test in enumerate(test_cases):
        nums_input = test["input"]
        expected_output = test["expected"]

        # Choose the function to test (e.g., missingNumber or missingNumber_sum)
        # Using the primary XOR solution as required by the follow-up preference
        actual_output = missingNumber(nums_input)

        result = actual_output == expected_output
        print(f"{result}") # Print True or False per test

        if result:
            correct_count += 1
        # Optional: Print details on failure
        # else:
        #     print(f"Test Case {i+1} Failed:")
        #     print(f"  Input: {nums_input}")
        #     print(f"  Expected: {expected_output}")
        #     print(f"  Actual: {actual_output}")

    # --- Final Summary ---
    print(f"{correct_count}/{total_tests}")

# --- Execute the solution ---
# The prompt asks for *only* executable code.
solve()