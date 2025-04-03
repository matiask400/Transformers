import sys
from collections import Counter
from typing import List

# Function Definition
def uniqueOccurrences(arr: List[int]) -> bool:
    """
    Given an array of integers arr, returns true if and only if
    the number of occurrences of each value in the array is unique.

    Args:
        arr: A list of integers.

    Returns:
        True if the number of occurrences of each value is unique, False otherwise.
    
    Constraints:
        1 <= arr.length <= 1000
       -1000 <= arr[i] <= 1000
    
    Examples:
        uniqueOccurrences([1, 2, 2, 1, 1, 3]) -> True 
        (1:3, 2:2, 3:1. Frequencies {1, 2, 3} are unique)
        
        uniqueOccurrences([1, 2]) -> False 
        (1:1, 2:1. Frequencies {1, 1} are not unique)
        
        uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]) -> True
        (-3:3, 0:2, 1:4, 10:1. Frequencies {1, 2, 3, 4} are unique)
    """
    # Step 1: Count occurrences of each number using Counter
    # Counter efficiently creates a hash map (dict) of {element: count}
    counts = Counter(arr)

    # Step 2: Extract the frequencies (the counts themselves)
    # We only care about the counts, not the elements they belong to.
    frequencies = list(counts.values())

    # Step 3: Check if all frequencies are unique
    # We can do this by comparing the number of frequencies found
    # with the number of *unique* frequencies (obtained by converting to a set).
    # If the lengths are equal, all frequencies were distinct.
    return len(frequencies) == len(set(frequencies))

# Test Runner Function
def run_tests():
    """
    Runs predefined test cases against the uniqueOccurrences function,
    prints 'True' for passed tests, 'False' for failed tests,
    and finally prints the ratio of correct tests over the total number of tests.
    """
    test_cases = [
        # Provided examples
        {"input": [1, 2, 2, 1, 1, 3], "expected": True, "id": "Example 1"},
        {"input": [1, 2], "expected": False, "id": "Example 2"},
        {"input": [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], "expected": True, "id": "Example 3"},
        # Additional test cases
        {"input": [], "expected": True, "id": "Empty Array"},                   # Edge case: Empty input
        {"input": [5], "expected": True, "id": "Single Element"},               # Edge case: Single element array
        {"input": [1, 1, 1, 1], "expected": True, "id": "Single Value Multiple Times"}, # All same element (count is unique)
        {"input": [1, 1, 2, 2], "expected": False, "id": "Multiple Values Same Frequency"}, # Non-unique frequencies
        {"input": [7, 7, 7, 8, 8, 9], "expected": True, "id": "Unique Frequencies"},      # All frequencies unique
        {"input": [1, 10, 100, 1000, 1], "expected": False, "id": "Non-Unique Frequencies Mixed"}, # Some frequencies non-unique
        {"input": list(range(500)) + list(range(500)), "expected": False, "id": "Large Input Non-Unique Freq"}, # Larger input, all count 2
        {"input": [i // 2 for i in range(10)], "expected": False, "id": "Generated Non-Unique Freq"}, # [0,0,1,1,2,2,3,3,4,4] -> all count 2
        {"input": [1]*5 + [2]*5 + [3]*4, "expected": False, "id": "Mixed Freq Non-Unique"}, # Counts 5, 5, 4 -> False
        {"input": [1]*5 + [2]*4 + [3]*3, "expected": True, "id": "Mixed Freq Unique"},      # Counts 5, 4, 3 -> True
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for test_case in test_cases:
        arr_input = test_case["input"]
        expected_output = test_case["expected"]
        test_id = test_case["id"] # For potential debugging, though not printed per instructions

        # Execute the student's function
        try:
            actual_output = uniqueOccurrences(arr_input)
        except Exception as e:
            print(f"False  # Error during execution for test '{test_id}': {e}")
            continue # Skip to next test case if error occurs


        # Verify the result
        test_passed = actual_output == expected_output
        
        # Print 'True' or 'False' for the test result as required
        print(f"{test_passed}") 

        if test_passed:
            correct_count += 1

    # Print the final summary score
    print(f"{correct_count}/{total_tests}")

# Guard for script execution: Ensures run_tests() is called only when the script is run directly
if __name__ == "__main__":
    run_tests()