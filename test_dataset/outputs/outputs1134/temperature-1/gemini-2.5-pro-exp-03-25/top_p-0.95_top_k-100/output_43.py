import sys 
# Setting a recursion depth limit is generally good practice, although not strictly necessary 
# for this specific iterative algorithm. Increasing it slightly just in case.
# sys.setrecursionlimit(2000) 

def num_times_all_blue(light: list[int]) -> int:
    """
    Calculates the number of moments where all turned-on bulbs are blue.

    There are n bulbs, numbered 1 to n. At moment k (0-indexed), bulb light[k] is turned on.
    A bulb turns blue if it's on and all bulbs to its left (with smaller numbers) are also on.
    We need to find the number of moments k where *all* bulbs that are currently turned on are blue.

    This condition holds if and only if the set of bulbs turned on at moment k 
    (i.e., {light[0], ..., light[k]}) is exactly the set {1, 2, ..., k+1}.
    This, in turn, is equivalent to checking if the maximum bulb number turned on
    up to moment k is equal to the total number of bulbs turned on so far, which is k+1.

    Args:
        light: A list of integers representing the order bulbs are turned on.
               It's guaranteed to be a permutation of [1, 2, ..., n], where n = len(light).

    Returns:
        The number of moments (from k=0 to n-1) where all turned-on bulbs are blue.
    """
    n = len(light)
    # If there are no bulbs, there are no moments to check.
    if n == 0:
        return 0

    count = 0  # Counter for moments when all turned-on bulbs are blue.
    max_so_far = 0  # Tracks the maximum bulb number turned on up to the current moment.
    
    # Iterate through each moment k from 0 to n-1.
    for k in range(n):
        # At moment k, the bulb light[k] is turned on.
        bulb = light[k]
        
        # Update the maximum bulb number seen so far.
        max_so_far = max(max_so_far, bulb)
        
        # The number of bulbs turned on after moment k is k + 1.
        # Check if the maximum bulb turned on equals the count of bulbs turned on.
        # If max_so_far == k + 1, it means all bulbs from 1 to k+1 must be on,
        # because we have turned on exactly k+1 distinct bulbs and the largest is k+1.
        # This ensures that the set of turned-on bulbs is {1, 2, ..., k+1},
        # which implies all turned-on bulbs satisfy the blue condition.
        if max_so_far == k + 1:
            count += 1
            
    return count

def run_tests():
    """
    Runs predefined test cases against the num_times_all_blue function
    and prints the results according to the specified format:
    - Prints 'True' for each test passed, 'False' otherwise.
    - Finally, prints the ratio of correct tests over the total number of tests.
    """
    test_cases = [
        # Provided examples
        {'input': [2,1,3,5,4], 'expected':