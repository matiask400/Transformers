import collections

def subarraySum(nums: list[int], k: int) -> int:
    """
    Given an array of integers nums and an integer k, return the total
    number of continuous subarrays whose sum equals to k.

    Args:
        nums: A list of integers.
        k: The target sum.

    Returns:
        The total number of continuous subarrays summing to k.
    """
    count = 0
    current_sum = 0
    # Use a hash map (dictionary) to store the frequency of prefix sums.
    # Initialize with {0: 1} to handle subarrays starting from index 0.
    # A prefix sum of 0 means an empty prefix before the array starts.
    prefix_sum_counts = {0: 1}

    for num in nums:
        current_sum += num

        # Check if (current_sum - k) exists in the prefix sums encountered so far.
        # If it exists, it means there was a previous point in the array
        # where the sum up to that point was `current_sum - k`.
        # The subarray between that point (exclusive) and the current point (inclusive)
        # must sum to k.
        complement = current_sum - k
        if complement in prefix_sum_counts:
            count += prefix_sum_counts[complement]

        # Update the frequency of the current prefix sum in the map.
        prefix_sum_counts[current_sum] = prefix_sum_counts.get(current_sum, 0) + 1

    return count

def run_tests():
    """
    Runs test cases against the subarraySum function and prints the results.
    """
    test_cases = [
        # Format: (nums, k, expected_output)
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1], 1, 1),
        ([1], 0, 0),
        ([-1, -1, 1], 0, 1),
        ([1, -1, 0], 0, 3), # Subarrays: [1, -1], [0], [1, -1, 0]
        ([0, 0, 0, 0, 0], 0, 15), # n*(n+1)/2 = 5*6/2 = 15
        ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4), # Subarrays: [3,4], [7], [7,2,-3,1], [-3,1,4,2]
        ([1, 1, 1, 1, 1], 3, 3),
        ([10, 2, -2, -20, 10], -10, 3), # Subarrays: [10, 2, -2, -20], [2, -2, -20, 10], [-20, 10]
        ([5], 5, 1),
        ([5, -5, 5, -5, 5], 0, 4), # [-5, 5], [5, -5], [-5, 5], [5, -5] -> Check this:
            # Prefixes: 0, 5, 0, 5, 0, 5
            # k=0
            # num=5, sum=5, comp=5, map={0:1, 5:1}, count=0
            # num=-5, sum=0, comp=0, map[0]=1, count=1, map={0:2, 5:1} -> [5,-5]
            # num=5, sum=5, comp=5, map[5]=1, count=1+1=2, map={0:2, 5:2} -> [-5,5]
            # num=-5, sum=0, comp=0, map[0]=2, count=2+2=4, map={0:3, 5:2} -> [5,-5]
            # num=5, sum=5, comp=5, map[5]=2, count=4+2=6, map={0:3, 5:3} -> [-5,5]
            # Expected: 6. Let's re-list: [5,-5], [-5,5], [5,-5], [-5,5], [5,-5,5,-5], [-5,5,-5,5]
            # Ah, the example description was maybe incomplete. Let's trust the algorithm.
            # Test case updated expected output to 6.
        ([5, -5, 5, -5, 5], 0, 6), # Corrected expected output based on algorithm trace
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, (nums, k, expected) in enumerate(test_cases):
        result = subarraySum(nums, k)
        passed = result == expected
        print(f"{passed}") # Print True or False for each test
        if passed:
            correct_tests += 1
        # Optional: Print details on failure
        # else:
        #     print(f"Test {i+1} Failed: Input ({nums}, {k}), Expected {expected}, Got {result}")

    print(f"\n{correct_tests}/{total_tests}") # Print final score

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()