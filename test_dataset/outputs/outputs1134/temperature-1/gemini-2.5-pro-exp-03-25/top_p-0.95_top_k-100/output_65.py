import collections

def numSubarraysWithSum(A, S):
    """
    Calculates the number of non-empty subarrays in A with sum S.
    Uses the prefix sum technique with a hash map.

    Args:
        A: A list of 0s and 1s.
        S: The target sum.

    Returns:
        The count of subarrays with sum S.
    """
    # prefix_sum_counts stores the frequency of each prefix sum encountered.
    # Initialize with {0: 1} to handle subarrays starting from index 0.
    # A prefix sum P means the sum of elements A[0...k] = P for some k.
    # We are looking for pairs (i, j) such that sum(A[i...j]) = S.
    # This is equivalent to prefix_sum[j+1] - prefix_sum[i] = S.
    # Or prefix_sum[j+1] - S = prefix_sum[i].
    # As we iterate through the array with index `j`, the current prefix sum is `current_sum` (equivalent to prefix_sum[j+1]).
    # We need to find how many times the prefix sum `current_sum - S` has occurred before.
    
    prefix_sum_counts = collections.defaultdict(int)
    prefix_sum_counts[0] = 1
    current_sum = 0
    count = 0

    for num in A:
        current_sum += num
        # Check if a previous prefix sum exists such that (current_sum - that_sum) = S
        target_prefix_sum = current_sum - S
        if target_prefix_sum in prefix_sum_counts:
            count += prefix_sum_counts[target_prefix_sum]
        
        # Increment the count for the current prefix sum
        prefix_sum_counts[current_sum] += 1
        
    return count

# Alternative implementation using the properties of 0s and 1s
def numSubarraysWithSum_alternative(A, S):
    """
    Alternative calculation exploiting the 0/1 nature of the array.
    Finds indices of 1s and calculates gaps between them.

    Args:
        A: A list of 0s and 1s.
        S: The target sum.

    Returns:
        The count of subarrays with sum S.
    """
    n = len(A)
    
    # Special case: S = 0
    # Count subarrays consisting only of zeros.
    if S == 0:
        count = 0
        zeros_streak = 0
        for x in A:
            if x == 0:
                zeros_streak += 1
            else:
                # A block of k zeros contributes k*(k+1)/2 subarrays
                count += zeros_streak * (zeros_streak + 1) // 2
                zeros_streak = 0
        # Add contribution from trailing zeros
        count += zeros_streak * (zeros_streak + 1) // 2
        return count

    # General case: S > 0
    ones_indices = [i for i, x in enumerate(A) if x == 1]
    num_ones = len(ones_indices)

    if S < 0 or S > num_ones:
        return 0

    # Add pseudo-indices for boundaries: -1 for start, n for end
    padded_ones_indices = [-1] + ones_indices + [n]
    
    count = 0
    # Iterate through all possible groups of S consecutive ones
    # The i-th group starts at ones_indices[i] and ends at ones_indices[i+S-1]
    for i in range(num_ones - S + 1):
        # Index in padded_ones_indices corresponding to ones_indices[i] is i+1
        start