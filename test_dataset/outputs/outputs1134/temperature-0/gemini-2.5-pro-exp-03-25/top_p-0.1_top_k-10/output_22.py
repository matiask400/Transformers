import sys
from collections import Counter
from typing import List, Tuple, Any

# Core logic function
def uniqueOccurrences(arr: List[int]) -> bool:
    """
    Checks if the number of occurrences of each value in the array is unique.

    Args:
        arr: A list of integers.

    Returns:
        True if the number of occurrences of each value is unique, False otherwise.
    """
    # Constraints state 1 <= arr.length <= 1000, so no need to check for empty array.

    # 1. Count occurrences of each number using collections.Counter
    # Example: arr = [1, 2, 2, 1, 1, 3] -> counts = {1: 3, 2: 2, 3: 1}
    counts = Counter(arr)

    # 2. Get the list/collection of the occurrence counts (the frequencies)
    # Example: counts.values() -> [3, 2, 1]
    occurrence_counts = list(counts.values())

    # 3. Check if all occurrence counts are unique.
    # We can do this by comparing the number of counts
    # with the number of unique counts (using a set).
    # Example: len([3, 2, 1]) == len({3, 2, 1}) -> 3 == 3 -> True
    # Example: arr = [1, 2] -> counts = {1: 1, 2: 1} -> occ_counts = [1, 1]
    #          len([1, 1]) == len({1}) -> 2 == 1 -> False
    return len(occurrence_counts) == len(set(occurrence_counts))

# Test runner function
def run_tests():
    """
    Runs predefined test cases against the uniqueOccurrences function
    and prints the results according to the specified format.
    """
    # List of tuples: (input_list, expected_output)
    test_cases: List[Tuple[List[int], bool]] = [
        ([1, 2, 2, 1, 1, 3], True),        # Example 1
        ([1, 2], False),                   # Example 2
        ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True), # Example 3
        ([1, 1, 1, 1], True),              # Single distinct element, count [4] is unique
        ([1, 2, 3, 4], False),             # All elements unique, counts [1, 1, 1, 1] are not unique
        ([7], True),                       # Single element array, count [1] is unique
        ([2, 2, 5, 5, 5], True),           # Counts [2, 3] are unique
        ([1, 1, 2, 2, 2, 3, 3, 3], False), # Counts [2, 3, 3] are not unique
        ([10, 20, 20, 10, 10], False),     # Counts [3, 2] are unique -> Should be True. Let's recheck. 10:3, 20:2. Counts [3,2]. len([3,2])==len({3,2}) -> 2==2 -> True. Corrected expected output.
        ([0,0,0], True),                   # Count [3] is unique
    ]
    
    # Correcting the test case based on re-evaluation
    test_cases[8] = ([10, 20, 20, 10, 10], True)


    correct_count = 0
    total_tests = len(test_cases)

    for i, (arr_input, expected_output) in enumerate(test_cases):
        # Run the student's function
        try:
            actual_output = uniqueOccurrences(arr_input)
            # Compare results
            passed = actual_output == expected_output
            print(f"{passed}") # Print True or False for the test result
        except Exception as e:
            print(f"False # Error occurred: {e}")
            passed = False

        # Increment correct count if passed
        if passed:
            correct_count += 1

    # Print the final summary
    print(f"{correct_count}/{total_tests}")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()