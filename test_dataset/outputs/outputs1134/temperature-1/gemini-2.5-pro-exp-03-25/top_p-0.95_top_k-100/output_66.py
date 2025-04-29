# -*- coding: utf-8 -*-
import sys
from typing import List, Tuple

def numJewelsInStones(jewels: str, stones: str) -> int:
    """
    Counts how many stones are also jewels.

    Args:
        jewels: A string where each character is a unique type of jewel.
        stones: A string representing the stones you have.

    Returns:
        The number of stones you have that are also jewels.
    """
    # Create a set of jewels for efficient O(1) average time lookup.
    # Set creation takes O(len(jewels)) time.
    jewel_set = set(jewels)

    count = 0
    # Iterate through each stone. This takes O(len(stones)) time.
    for stone in stones:
        # Check if the stone is in the set of jewels. O(1) on average.
        if stone in jewel_set:
            count += 1

    # Overall time complexity: O(len(jewels) + len(stones))
    # Overall space complexity: O(len(jewels)) for the set.
    return count

# --- Testing Framework ---

def run_tests():
    """
    Runs predefined test cases against the numJewelsInStones function
    and prints the results.
    """
    # List of tuples: ( (jewels_input, stones_input), expected_output )
    test_cases: List[Tuple[Tuple[str, str], int]] = [
        (("aA", "aAAbbbb"), 3),
        (("z", "ZZ"), 0),
        (("abc", "aabbcc"), 6),
        (("Ab", "aABBb"), 3),
        (("X", ""), 0),
        (("", "xyz"), 0),
        (("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
          "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"),
         104),
        (("Jewels", "stones"), 0),
        (("a", "aaaaa"), 5),
        (("aBc", "AbcBCa"), 4), # Mixed case jewels and stones
        (("qwe", "qQwWeE"), 3), # Only lowercase jewels match
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, (inputs, expected_output) in enumerate(test_cases):
        jewels_input, stones_input = inputs
        try:
            # Execute the function with the current test case inputs
            result = numJewelsInStones(jewels_input, stones_input)

            # Compare the actual result with the expected output
            is_correct = (result == expected_output)

            # Print True or False for the test result
            print(f"{is_correct}")

            if is_correct:
                correct_tests += 1
        except Exception as e:
            # Print False if any exception occurs during the test
            print(f"False")
            print(f"  Test case {i+1} failed with error: {e}", file=sys.stderr)
            print(f"  Inputs: jewels='{jewels_input}', stones='{stones_input}'", file=sys.stderr)

    # Print the final summary
    print(f"{correct_tests}/{total_tests}")

# --- Main Execution Block ---

if __name__ == '__main__':
    # The script is designed to be executed directly to run the tests.
    run_tests()