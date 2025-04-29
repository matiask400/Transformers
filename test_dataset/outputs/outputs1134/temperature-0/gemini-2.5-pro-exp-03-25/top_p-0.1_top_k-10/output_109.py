import sys
import io

def solve():
    """
    Solves the Flip Game problem. Finds all possible states after one valid move.
    A valid move consists of flipping two consecutive "++" to "--".
    """
    def generatePossibleNextMoves(currentState: str) -> list[str]:
        """
        Generates all possible next states after one valid move.

        Args:
            currentState: The current state string containing '+' and '-'.

        Returns:
            A list of all possible states after one move. Returns an empty list
            if no moves are possible.
        """
        n = len(currentState)
        possible_moves = []
        for i in range(n - 1):
            # Check for two consecutive '+'
            if currentState[i] == '+' and currentState[i+1] == '+':
                # Construct the next state by flipping "++" to "--"
                next_state = currentState[:i] + "--" + currentState[i+2:]
                possible_moves.append(next_state)
        return possible_moves

    # --- Testing Framework ---
    test_cases = [
        ("++++", ["--++", "+--+", "++--"]),
        ("+", []),
        ("---", []),
        ("++", ["--"]),
        ("+-+-", []),
        ("+++++", ["--+++", "+--++", "++--+"]),
        ("++-++", ["-- -++", "++---"]), # Note: Added space for clarity, actual output won't have it
        ("--++--", ["---- --"]),        # Note: Added space for clarity, actual output won't have it
    ]
    
    # Adjust expected outputs to remove spaces used for clarity above
    test_cases[6] = ("++-++", ["---++", "++---"])
    test_cases[7] = ("--++--", ["------"])


    correct_count = 0
    total_tests = len(test_cases)

    for i, (input_str, expected_output) in enumerate(test_cases):
        # Capture the output of the function
        # Redirect stdout to capture print statements if needed, but here we compare return values
        
        # Run the function
        actual_output = generatePossibleNextMoves(input_str)

        # Compare the actual output with the expected output
        # Use sets for comparison as the order doesn't matter
        passed = set(actual_output) == set(expected_output)
        
        print(f"Test Case {i+1}:")
        print(f"Input: currentState = \"{input_str}\"")
        print(f"Expected Output: {sorted(expected_output)}")
        print(f"Actual Output:   {sorted(actual_output)}")
        print(f"Result: {passed}")
        print("-" * 20)

        if passed:
            correct_count += 1

    print(f"\nSummary: {correct_count} / {total_tests} tests passed.")

# Execute the solve function
if __name__ == "__main__":
    # Redirect stdout to capture the final summary correctly if needed,
    # but the current structure prints directly.
    # Keep the standard output for interactive testing results.
    solve()