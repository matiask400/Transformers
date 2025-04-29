import collections
from typing import List

def generatePossibleNextMoves(currentState: str) -> List[str]:
    """
    Generates all possible states of the string after one valid move.
    A valid move consists of flipping two consecutive "++" into "--".

    Args:
        currentState: The current state of the string containing '+' and '-'.

    Returns:
        A list of all possible states after one move. Returns an empty list
        if no valid move is possible.
    """
    n = len(currentState)
    possible_next_states = []

    # Iterate through the string up to the second to last character
    # to check for consecutive "++"
    for i in range(n - 1):
        # Check if the characters at index i and i+1 are both '+'
        if currentState[i] == '+' and currentState[i+1] == '+':
            # Construct the next state by replacing "++" with "--"
            # Slicing creates the parts before and after the flip
            next_state = currentState[:i] + "--" + currentState[i+2:]
            possible_next_states.append(next_state)

    return possible_next_states

def run_tests():
    """
    Runs predefined test cases against the generatePossibleNextMoves function
    and prints the results.
    """
    test_cases = [
        {"input": "++++", "expected_output": ["--++", "+--+", "++--"]},
        {"input": "+", "expected_output": []},
        {"input": "++", "expected_output": ["--"]},
        {"input": "---", "expected_output": []},
        {"input": "--++--", "expected_output": ["----"]},
        {"input": "+-+-+-", "expected_output": []},
        {"input": "+++++++", "expected_output": ["--+++++", "+--++++", "++--+++", "+++--++", "++++--+"]},
        {"input": "++-++", "expected_output": ["---++", "++---"]},
        {"input": "-+", "expected_output": []},
        {"input": "++++++++++", "expected_output": ["--++++++++", "+--+++++++", "++--++++++", "+++--+++++", "++++--++++", "+++++--+++", "++++++--++", "+++++++--+", "++++++++--"]},
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, test in enumerate(test_cases):
        input_str = test["input"]
        expected_output = test["expected_output"]

        # Get the result from the function
        result = generatePossibleNextMoves(input_str)

        # Sort both lists for comparison as order doesn't matter
        result_sorted = sorted(result)
        expected_output_sorted = sorted(expected_output)

        # Compare the sorted lists
        if result_sorted == expected_output_sorted:
            print(f"Test {i + 1}: True")
            correct_count += 1
        else:
            print(f"Test {i + 1}: False")
            # Optional: print details on failure
            # print(f"  Input:    '{input_str}'")
            # print(f"  Expected: {expected_output_sorted}")
            # print(f"  Got:      {result_sorted}")

    print(f"\nResult: {correct_count} / {total_tests} tests passed.")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()