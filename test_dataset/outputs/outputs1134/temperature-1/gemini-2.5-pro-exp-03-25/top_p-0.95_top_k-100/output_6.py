import collections

def solve():
    """
    Solves the matrix reconstruction problem.
    Reads inputs, calls the reconstruction function, and returns the result.
    Note: In a standard competitive programming setup, input reading would be
          handled differently (e.g., sys.stdin). Here, we'll define inputs
          within the function for self-contained execution.

    This function is not directly used by the testing framework below
    but demonstrates how the core logic could be invoked independently.
    """

    # Example Usage (replace with actual input reading if needed)
    upper = 2
    lower = 1
    colsum = [1, 1, 1]

    result = reconstructMatrix(upper, lower, colsum)
    print(f"Input: upper={upper}, lower={lower}, colsum={colsum}")
    print(f"Output: {result}")

def reconstructMatrix(upper: int, lower: int, colsum: list[int]) -> list[list[int]]:
    """
    Reconstructs a 2xN binary matrix given row sums and column sums.

    Args:
        upper: The required sum of the first row.
        lower: The required sum of the second row.
        colsum: A list where colsum[i] is the required sum of the i-th column.

    Returns:
        A 2D list representing the reconstructed matrix if a solution exists,
        otherwise an empty list.
    """
    n = len(colsum)
    
    # 1. Initial Check: Total sum consistency
    if upper + lower != sum(colsum):
        return []

    # Initialize the matrix with zeros
    matrix = [[0] * n, [0] * n]
    
    remaining_upper = upper
    remaining_lower = lower

    # 2. First Pass: Handle columns with sum 2 (mandatory placements)
    for i in range(n):
        if colsum[i] == 2:
            # Check if we have enough '1's available in both rows
            if remaining_upper < 1 or remaining_lower < 1:
                return [] # Impossible to place two '1's
            
            matrix[0][i] = 1
            matrix[1][i] = 1
            remaining_upper -= 1
            remaining_lower -= 1

    # 3. Second Pass: Handle columns with sum 1 (greedy placement)
    for i in range(n):
        if colsum[i] == 1:
            # Prioritize placing '1' in the upper row if quota available
            if remaining_upper > 0:
                matrix[0][i] = 1
                remaining_upper -= 1
            # Otherwise, place in the lower row if quota available
            elif remaining_lower > 0:
                matrix[1][i] = 1
                remaining_lower -= 1
            # If neither row has quota left, but colsum[i] is 1, it's impossible
            else:
                return [] 
                
    # 4. Final Check: Ensure all row sums are exactly met
    if remaining_upper == 0 and remaining_lower == 0:
        # Verify column sums explicitly (optional but good for debugging)
        # for j in range(n):
        #     if matrix[0][j] + matrix[1][j] != colsum[j]:
        #         # This should not happen if the logic above is correct
        #         # and the initial sum check passed.
        #         print("Error: Column sum mismatch detected post-construction.")
        #         return [] 
        return matrix
    else:
        # This means either upper/lower became negative (handled earlier)
        # or the greedy assignment used up the counts but didn't match the total needed,
        # contradicting the initial sum check.
        return []


# --- Testing Framework ---

def run_tests():
    test_cases = [
        # Example 1
        {"input": {"upper": 2, "lower": 1, "colsum": [1, 1, 1]}, 
         "expected": [[1, 1, 0], [0, 0, 1]]}, # One possible valid output
        # Example 2
        {"input": {"upper": 2, "lower": 3, "colsum": [2, 2, 1, 1]}, 
         "expected": []},
        # Example 3
        {"input": {"upper": 5, "lower": 5, "colsum": [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]}, 
         "expected": [[1, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]]}, # One possible valid output
        # Additional Test Cases
        # Sum mismatch
        {"input": {"upper": 1, "lower": 1, "colsum": [1, 0, 1]}, 
         "expected": []},
        # All zeros
        {"input": {"upper": 0, "lower": 0, "colsum": [0, 0, 0]}, 
         "expected": [[0, 0, 0], [0, 0, 0]]},
        # All twos
        {"input": {"upper": 3, "lower": 3, "colsum": [2, 2, 2]}, 
         "expected": [[1, 1, 1], [1, 1, 1]]},
        # Impossible distribution (enough total sum, but not distributable)
        {"input": {"upper": 1, "lower": 1, "colsum": [2, 0, 0]}, 
         "expected": []}, # Corrected: Should be [[1,0,0],[1,0,0]] -> let's re-verify
         # Trace: u=1, l=1, cs=[2,0,0]. Sum=2. u+l=2. OK.
         # i=0, cs[0]=2. Need u>=1, l>=1. OK. M[0][0]=1, M[1][0]=1. rem_u=0, rem_l=0.
         # i=1, cs[1]=0. Do nothing.
         # i=2, cs[2]=0. Do nothing.
         # Final check: rem_u=0, rem_l=0. OK. Return [[1,0,0],[1,0,0]]. My manual trace was wrong initially.
        {"input": {"upper": 1, "lower": 1, "colsum": [2, 0, 0]}, 
         "expected": [[1,0,0],[1,0,0]]}, # Corrected expected output
         # Impossible distribution 2
        {"input": {"upper": 0, "lower": 2, "colsum": [1, 1, 0]},
         "expected": [[0, 0, 0], [1, 1, 0]]},
         # Trace: u=0, l=2, cs=[1,1,0]. Sum=2. u+l=2. OK.
         # No cs==2.
         # i=0, cs[0]=1. rem_u=0. Check rem_l=2 > 0. M[1][0]=1. rem_l=1.
         # i=1, cs[1]=1. rem_u=0. Check rem_l=1 > 0. M[1][1]=1. rem_l=0.
         # i=2, cs[2]=0. Do nothing.
         # Final check: rem_u=0, rem_l=0. OK. Return [[0,0,0],[1,1,0]].
        # Impossible distribution 3
        {"input": {"upper": 1, "lower": 0, "colsum": [1, 0, 0]},
         "expected": [[1, 0, 0], [0, 0, 0]]},
         # Trace: u=1, l=0, cs=[1,0,0]. Sum=1. u+l=1. OK.
         # No cs==2.
         # i=0, cs[0]=1. rem_u=1 > 0. M[0][0]=1. rem_u=0.
         # i=1, cs[1]=0. Do nothing.
         # i=2, cs[2]=0. Do nothing.
         # Final check: rem_u=0, rem_l=0. OK. Return [[1,0,0],[0,0,0]].
        # Large case
        {"input": {"upper": 1, "lower": 1, "colsum": [1]*100000}, 
         "expected": "valid_output"}, # Expect a valid output, specific content depends on greedy choice
         # Empty case (not allowed by constraints, but good to consider)
         #{"input": {"upper": 0, "lower": 0, "colsum": []}, "expected": [[], []]}, # Actually should be [[],[]] if n=0
         # Let's stick to constraints: n >= 1
         {"input": {"upper": 0, "lower": 0, "colsum": [0]}, 
          "expected": [[0], [0]]},
         {"input": {"upper": 1, "lower": 0, "colsum": [1]}, 
          "expected": [[1], [0]]},
         {"input": {"upper": 0, "lower": 1, "colsum": [1]}, 
          "expected": [[0], [1]]},
          {"input": {"upper": 1, "lower": 1, "colsum": [2]}, 
          "expected": [[1], [1]]},
          {"input": {"upper": 1, "lower": 1, "colsum": [1]}, 
          "expected": []}, # Sum mismatch
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, test in enumerate(test_cases):
        upper = test["input"]["upper"]
        lower = test["input"]["lower"]
        colsum = test["input"]["colsum"]
        expected = test["expected"]

        result = reconstructMatrix(upper, lower, colsum)
        
        # Special handling for the large case where any valid output is okay
        if expected == "valid_output":
             is_correct = is_valid_reconstruction(upper, lower, colsum, result)
        # Standard comparison
        elif isinstance(expected, list) and not expected: # Expecting empty list
             is_correct = (result == [])
        elif isinstance(expected, list) and expected: # Expecting a non-empty list
            is_correct = is_valid_reconstruction(upper, lower, colsum, result)
            # If there are multiple valid solutions, we just need to check if
            # the *returned* solution is valid, not necessarily identical to the
            # 'expected' one provided in the test case (which is just *one* example).
        else: # Should not happen based on test case structure
            is_correct = False
            print(f"Warning: Unexpected expected value type for test {i+1}")


        print(f"Test {i+1}: {is_correct}")
        if is_correct:
            correct_count += 1

    print(f"\nResult: {correct_count} / {total_tests} correct")

def is_valid_reconstruction(upper: int, lower: int, colsum: list[int], matrix: list[list[int]]) -> bool:
    """Checks if a given matrix is a valid reconstruction."""
    if not matrix: # If reconstructMatrix returned [], it's invalid unless expected was []
         return False
         
    if not isinstance(matrix, list) or len(matrix) != 2:
        return False # Must be a list of 2 rows
        
    n = len(colsum)
    
    if not matrix[0] or not matrix[1] or len(matrix[0]) != n or len(matrix[1]) != n:
         # print(f"Dimension mismatch: colsum len={n}, matrix dims={len(matrix[0]) if matrix[0] else 'N/A'}x{len(matrix[1]) if matrix[1] else 'N/A'}")
         return False # Rows must exist and have correct length
         
    # Check upper row sum
    if sum(matrix[0]) != upper:
        # print(f"Upper sum mismatch: expected {upper}, got {sum(matrix[0])}")
        return False
        
    # Check lower row sum
    if sum(matrix[1]) != lower:
        # print(f"Lower sum mismatch: expected {lower}, got {sum(matrix[1])}")
        return False
        
    # Check column sums and binary values
    for j in range(n):
        val0 = matrix[0][j]
        val1 = matrix[1][j]
        if val0 not in [0, 1] or val1 not in [0, 1]:
            # print(f"Non-binary value at column {j}: ({val0}, {val1})")
            return False # Check binary constraint
        if val0 + val1 != colsum[j]:
            # print(f"Column sum mismatch at column {j}: expected {colsum[j]}, got {val0 + val1}")
            return False # Check column sum constraint
            
    return True


# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()