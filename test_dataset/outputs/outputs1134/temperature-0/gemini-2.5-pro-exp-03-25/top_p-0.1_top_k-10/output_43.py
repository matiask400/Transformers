import sys 
# Setting a reasonable recursion depth, although not strictly necessary for this iterative solution.
# This is more of a safeguard for potentially complex problems.
# sys.setrecursionlimit(2000) 

# The core function to solve the problem
def num_times_all_blue(light: list[int]) -> int:
    """
    Calculates the number of moments where all turned-on bulbs are blue.

    A bulb `i` turns blue only if it is on AND all bulbs `1, 2, ..., i-1` are also on.
    All turned-on bulbs are blue at moment `k` if the set of bulbs turned on 
    up to moment `k` (i.e., {light[0], ..., light[k]}) forms a prefix of the
    sequence 1, 2, ..., n. That is, the set must be exactly {1, 2, ..., m}
    where m is the number of bulbs turned on, which is k+1.
    
    This condition holds if and only if the maximum bulb number turned on 
    up to moment `k` is exactly equal to `k+1`.

    Args:
        light: A list of integers representing the order bulbs are turned on.
               `light` is guaranteed to be a permutation of [1, 2, ..., n],
               where n is the length of the list.

    Returns:
        The number of moments (from k=0 to n-1) where all turned-on bulbs are blue.
    """
    n = len(light)
    # Counter for the moments when all turned-on bulbs are blue
    blue_moments_count = 0
    # Tracks the maximum bulb number turned on so far
    max_bulb_turned_on = 0
    
    # Iterate through each moment k from 0 to n-1
    for k in range(n):
        # At moment k, the bulb light[k] is turned on.
        # Update the maximum bulb number seen so far.
        # Since bulb numbers are 1-based, this tracks the rightmost bulb turned on.
        max_bulb_turned_on = max(max_bulb_turned_on, light[k])
        
        # Check the condition:
        # All bulbs turned on are blue if the maximum bulb number turned on
        # is equal to the total number of bulbs turned on so far.
        # The number of bulbs turned on at moment k is k + 1.
        # If max_bulb_turned_on == k + 1, it means all bulbs from 1 to k+1
        # must have been turned on (because light is a permutation and we've seen
        # k+1 bulbs, the largest of which is k+1).
        if max_bulb_turned_on == k + 1:
            blue_moments_count += 1
            
    return blue_moments_count

# Function to run test cases
def run_tests():
    """
    Runs predefined test cases against the num_times_all_blue function
    and prints the results according to the specified format.
    Prints 'True' for each passed test, 'False' for each failed test,
    and finally prints the ratio of correct tests over the total number of tests.
    """
    test_cases = [
        # Provided examples
        ([2, 1, 3, 5, 4], 3),
        ([3, 2, 4, 1, 5], 2),
        ([4, 1, 2, 3], 1),
        ([2, 1, 4, 3, 6, 5], 3),
        ([1, 2, 3, 4, 5, 6], 6),
        # Edge cases
        ([1], 1), # n = 1
        ([5, 4, 3, 2, 1], 1), # Reverse sorted order
        # Additional test cases
        ([1, 3, 2, 4], 2), # Check intermediate moments
        ([6, 5, 4, 3, 2, 1], 1), # Larger reverse sorted
        ([3, 1, 2, 5, 4], 2), # Moments k=2 (max=3) and k=4 (max=5)
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    # Iterate through test cases, run the function, and check results
    for i, (light_input, expected_output) in enumerate(test_cases):
        # Calculate the actual result using the implemented function
        try:
            result = num_times_all_blue(light_input)
            # Compare actual result with the expected output
            passed = result == expected_output
        except Exception as e:
            # If the function throws an error, the test fails
            passed = False
            print(f