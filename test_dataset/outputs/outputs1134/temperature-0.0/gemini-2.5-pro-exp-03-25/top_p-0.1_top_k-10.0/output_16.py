import collections
import sys

# Define the main function that includes the solution and test runner
def solve():
    """
    Solves the Subarray Sums Divisible by K problem and runs tests.
    """

    # Define the core logic function
    def subarraysDivByK(A, K):
        """
        Calculates the number of contiguous subarrays whose sum is divisible by K.

        Args:
            A: A list of integers.
            K: An integer divisor (K >= 2).

        Returns:
            The number of subarrays with sum divisible by K.
        
        Approach:
        Uses the concept of prefix sums and modular arithmetic.
        Let P[i] be the prefix sum A[0] + ... + A[i-1]. P[0] = 0.
        The sum of subarray A[i:j+1] is P[j+1] - P[i].
        We want (P[j+1] - P[i]) % K == 0, which implies P[j+1] % K == P[i] % K.
        We iterate through the array, calculating prefix sums and their remainders modulo K.
        We use a hash map (or dictionary) to store the frequency of each remainder encountered so far.
        If the current prefix sum's remainder `r` has been seen `c` times before, it means there are `c`
        starting indices `i` such that the subarray ending at the current position has a sum divisible by K.
        We add `c` to our total count and then update the frequency of remainder `r`.
        """
        count = 0
        prefix_sum = 0
        # Use defaultdict for convenience, stores frequency of remainders
        # remainder_counts[r] stores how many times a prefix sum with remainder r has been seen.
        remainder_counts = collections.defaultdict(int)
        # Initialize with remainder 0 having count 1 (for the empty prefix sum P[0]=0)
        # This handles subarrays starting from index 0 whose sum is divisible by K.
        remainder_counts[0] = 1

        for num in A:
            prefix_sum += num
            # Calculate remainder (Python's % operator works correctly for positive K,
            # giving results in [0, K-1])
            remainder = prefix_sum % K

            # If this remainder `remainder` has been seen before (i.e., remainder_counts[remainder] > 0),
            # it means there are `remainder_counts[remainder]` previous prefix sums P[i]
            # such that P[current] % K == P[i] % K.
            # Each such P[i] corresponds to a subarray A[i:current_index+1] whose sum is divisible by K.
            count +=