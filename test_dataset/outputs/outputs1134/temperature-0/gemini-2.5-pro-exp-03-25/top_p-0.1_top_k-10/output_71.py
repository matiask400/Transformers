import collections
import math

def canReorderDoubled(arr: list[int]) -> bool:
    """
    Checks if an array of even length can be reordered such that 
    arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2.

    Args:
        arr: A list of integers with even length.

    Returns:
        True if such a reordering is possible, False otherwise.
    """
    count = collections.Counter(arr)
    
    # Handle zeros separately
    if count[0] % 2 != 0:
        return False
    # Zeros are paired with themselves, remove them from consideration
    del count[0] 
    # Or alternatively: count[0] = 0 
    # (but deleting is slightly cleaner if the key exists)

    # Sort keys by absolute value to process smaller numbers first
    # This ensures that when we check for x, we look for 2x. 
    # If we processed 2x first, we might incorrectly use it to match 4x.
    sorted_keys = sorted(count.keys(), key=abs)

    for x in sorted_keys:
        # If count[x] is already zero, it means x was used as a double (2*y) for some smaller y
        if count[x] == 0:
            continue

        target = 2 * x
        
        # Check if the required double exists and has sufficient count
        if count.get(target, 0) < count[x]:
            return False
        
        # Decrement the count of the double
        count[target] -= count[x]
        
        # Set the count of x to 0 as all instances of x have been paired
        # Although not strictly necessary because we iterate in sorted order 
        # and won't revisit x, it makes the state clearer.
        count[x] = 0 

    # If we successfully paired all numbers
    return True

# --- Testing Framework ---

def run_tests():
    """
    Runs predefined test cases against the canReorderDoubled function.
    """
    test_cases = [
        ([3, 1, 3, 6], False),
        ([2, 1, 2, 6], False),
        ([4, -2, 2, -4], True),
        ([1, 2, 4, 16, 8, 4], False),
        ([0, 0], True),
        ([], True),
        ([1, 2, 1, 2], True),
        ([-2, -4, 1, 2], True),
        ([-6, -3, 4, 8], True),
        ([-2, -6, -3, 4, 8, -4], True),
        ([1, 1, 2, 2], False), # Need pairs (1,2) and (1,2)
        ([1, 2, 4, 8], True),
        ([0, 0, 0, 0], True),
        ([0, 0, 1, 2], True),
        ([0, 1, 2, 0], True),
        ([1, 2, 0, 0], True),
        ([0, 0, 0, 1], False), # Odd number of zeros
        ([2, 4, 0, 0], True),
        ([-1, -2], True),
        ([-2, -1], False), # Order matters in the condition, but reordering is allowed
        ([4, 2, 2, 4], True), # Can form (2,4) and (2,4)
        ([10, 20, 40, 80], True),
        ([1, 1, 1, 2], False),
        ([-5, -2, -10, -4], True),
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (arr_input, expected_output) in enumerate(test_cases):
        result = canReorderDoubled(arr_input.copy()) # Use copy to avoid modifying original test case
        is_correct = (result == expected_output)
        print(f"Test {i + 1}: {is_correct}")
        if is_correct:
            correct_count += 1

    print(f"\n{correct_count} / {total_tests} correct tests.")

# Execute the tests
if __name__ == "__main__":
    run_tests()