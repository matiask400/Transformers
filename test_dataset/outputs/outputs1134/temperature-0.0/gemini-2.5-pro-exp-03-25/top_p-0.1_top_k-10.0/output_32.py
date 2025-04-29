import collections
import sys

# Redirect stdout to capture print statements for testing purposes if needed,
# but the problem asks to print directly.
# original_stdout = sys.stdout
# from io import StringIO
# sys.stdout = captured_output = StringIO()

def numSubarraysWithSum(A, S):
    """
    Calculates the number of non-empty subarrays in A with sum S.
    A contains only 0s and 1s.

    Args:
        A: A list of integers (0s and 1s).
        S: The target sum.

    Returns:
        The number of subarrays with sum S.
    """
    # Approach: Prefix Sum with Hash Map
    # Let P[i] be the prefix sum A[0] + ... + A[i-1]. P[0] = 0.
    # The sum of subarray A[i..j] is P[j+1] - P[i].
    # We want P[j+1] - P[i] = S, which means P[i] = P[j+1] - S.
    # As we iterate through the array calculating the current prefix sum (P[j+1]),
    # we look for how many times the required previous prefix sum (P[j+1] - S)
    # has occurred.

    count = 0
    current_sum = 0
    # Stores frequency of prefix sums encountered so far.
    # Initialize with {0: 1} to handle subarrays starting from index 0.
    # A prefix sum of 0 occurs once before processing any element (empty prefix).
    prefix_sum_counts = collections.defaultdict(int)
    prefix_sum_counts[0] = 1

    for x in A:
        current_sum += x
        # Calculate the prefix sum value we need to find (target_prefix_sum)
        # such that current_sum - target_prefix_sum = S.
        target_prefix_sum = current_sum - S

        # If target_prefix_sum exists in our map, it means there are
        # prefix_sum_counts[target_prefix_sum] subarrays ending at the current
        # position with sum S.
        if target_prefix_sum in prefix_sum_counts:
            count += prefix_sum_counts[target_prefix_sum]

        # Increment the count for the current prefix sum in the map.
        prefix_sum_counts[current_sum] += 1

    return count

def run_tests():
    """
    Runs predefined test cases against the numSubarraysWithSum function.
    """
    test_cases = [
        # Example 1
        ([1, 0, 1, 0, 1], 2, 4),
        # Case: S = 0
        ([0, 0, 0, 0, 0], 0, 15),
        # Case: All ones
        ([1, 1, 1, 1, 1], 5, 1),
        ([1, 1, 1, 1, 1], 1, 5),
        ([1, 1, 1, 1, 1], 2, 4),
        # Mixed cases
        ([0, 0, 1, 0, 0, 1, 0], 2, 1), # Subarray [1, 0, 0, 1]
        ([0, 0, 1, 0, 0, 1, 0], 1, 4), # [1], [1,0,0], [0,1], [0,0,1]
        ([0, 0, 1, 0, 0, 1, 0], 0, 7), # [0], [0], [0,0] (first block) + [0],[0],[0,0] (second block) + [0] (third block) = 3+3+1=7
        # Edge cases
        ([], 0, 0),                     # Empty array
        ([1], 0, 0),
        ([0], 0, 1),
        ([1], 1, 1),
        ([0], 1, 0),
        # More complex case
        ([1,0,0,0,1,0,1], 2, 4),       # [1,0,0,0,1], [1,0,0,0,1,0], [0,1,0,1], [1,0,1]
        # Large S
        ([1,0,1,0,1], 5, 0),
        # S larger than possible sum
        ([1,0,1], 3, 0),
        # S = 0 with ones present
        ([1,0,0,1,0], 0, 3),           # [0,0], [0], [0]
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (A, S, expected) in enumerate(test_cases):
        # In a real testing scenario, might capture stdout, but here we print directly.