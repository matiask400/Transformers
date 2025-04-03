import sys
import io

def find_center(edges):
    """
    Finds the center of a star graph given its edges.

    Args:
        edges: A list of lists, where each inner list [u, v] represents an edge.
               It's guaranteed that the input represents a valid star graph with n >= 3.

    Returns:
        The label of the center node.
    """
    # The center node must be present in every edge.
    # Since n >= 3, there are at least two edges.
    # The center node must be the common node between the first two edges.
    # Let the first edge be [u1, v1] and the second edge be [u2, v2].
    # The center node must be in {u1, v1} and also in {u2, v2}.
    # We can just check which node from the first edge also appears in the second edge.

    node1_edge1 = edges[0][0]
    node2_edge1 = edges[0][1]
    
    node1_edge2 = edges[1][0]
    node2_edge2 = edges[1][1]

    # Check if node1_edge1 is the common node (the center)
    if node1_edge1 == node1_edge2 or node1_edge1 == node2_edge2:
        return node1_edge1
    else:
        # If node1_edge1 is not the center, then node2_edge1 must be the center,
        # because it's guaranteed to be a star graph.
        return node2_edge1

# --- Testing Framework ---

def solve():
    """
    Runs test cases against the find_center function and prints the results.
    """
    test_cases = [
        {"input": [[1, 2], [2, 3], [4, 2]], "expected": 2},
        {"input": [[1, 2], [5, 1], [1, 3], [1, 4]], "expected": 1},
        # Additional Test Cases
        {"input": [[3,5],[1,5],[5,2],[5,4]], "expected": 5}, # n=5
        {"input": [[10,1],[1,2],[1,3],[1,4],[5,1],[6,1],[7,1],[8,1],[9,1]], "expected": 1}, # n=10
        {"input": [[1,100],[2,100],[3,100]], "expected": 100}, # n=4, center=100
    ]

    num_tests = len(test_cases)
    passed_tests = 0

    # Capture print statements
    old_stdout = sys.stdout
    redirected_output = io.StringIO()
    sys.stdout = redirected_output

    for i, test in enumerate(test_cases):
        edges_input = test["input"]
        expected_output = test["expected"]
        
        # Temporarily restore stdout for the print inside the loop
        sys.stdout = old_stdout
        print(f"--- Test Case {i+1} ---")
        print(f"Input: edges = {edges_input}")
        print(f"Expected Output: {expected_output}")
        
        # Redirect stdout again for the function call and result check
        sys.stdout = redirected_output
        
        actual_output = find_center(edges_input)
        
        # Restore stdout to print the result comparison
        sys.stdout = old_stdout
        
        is_correct = (actual_output == expected_output)
        print(f"Actual Output: {actual_output}")
        print(f"Result: {is_correct}")
        if is_correct:
            passed_tests += 1
        print("-" * 20)
        
        # Redirect stdout back for the next iteration or final summary
        sys.stdout = redirected_output

    # Restore stdout for the final summary
    sys.stdout = old_stdout
    
    print(f"\n--- Summary ---")
    print(f"Passed {passed_tests} out of {num_tests} tests.")

    # You can optionally print the captured output from the function if needed
    # captured = redirected_output.getvalue()
    # print("\nCaptured output:\n", captured)
    redirected_output.close()


# Execute the solve function
if __name__ == "__main__":
    # The problem description asks for a specific output format during testing.
    # We will implement a slightly different runner function to match that exactly.

    def run_tests():
        test_cases = [
            {"input": [[1, 2], [2, 3], [4, 2]], "expected": 2},
            {"input": [[1, 2], [5, 1], [1, 3], [1, 4]], "expected": 1},
            {"input": [[3,5],[1,5],[5,2],[5,4]], "expected": 5},
            {"input": [[10,1],[1,2],[1,3],[1,4],[5,1],[6,1],[7,1],[8,1],[9,1]], "expected": 1},
            {"input": [[1,100],[2,100],[3,100]], "expected": 100},
        ]
        
        num_tests = len(test_cases)
        passed_count = 0
        
        for i, test in enumerate(test_cases):
            edges_input = test["input"]
            expected_output = test["expected"]
            actual_output = find_center(edges_input)
            result = actual_output == expected_output
            print(result) # Print True or False for each test
            if result:
                passed_count += 1
                
        print(f"{passed_count}/{num_tests}") # Print final score

    run_tests()