import sys

# This global variable will store the graph for the current test case.
# The knows function will access this variable.
_graph = None
# Counter for API calls (optional, for verifying the 3n constraint)
_api_calls = 0

def knows(a: int, b: int) -> bool:
    """
    Helper function simulation based on the graph.
    Returns true if person 'a' knows person 'b', false otherwise.
    Increments the API call counter.
    """
    global _graph
    global _api_calls
    if _graph is None:
        # This should not happen if the testing framework is used correctly
        raise ValueError("Graph not set for knows function")
    
    # Increment call counter (for analysis/debugging)
    _api_calls += 1
    
    # graph[i][j] == 1 means person i knows person j
    # graph[i][j] == 0 means person i does not know person j
    # The problem statement guarantees graph[i][i] == 1, but the definition
    # of a celebrity requires they don't know *others*.
    return _graph[a][b] == 1

def findCelebrity(n: int) -> int:
    """
    Finds the celebrity in a group of n people.
    
    The definition of a celebrity is that all the other n - 1 people know 
    him/her, but he/she does not know any of them.
    
    Args:
        n: The number of people (labeled 0 to n-1).
        
    Returns:
        The label of the celebrity if one exists, otherwise -1.
        
    Constraints:
        - Uses the knows(a, b) function.
        - Aims for O(n) time complexity and <= 3n calls to knows().
    """
    if n <= 1:
        # A single person cannot be a celebrity by the definition 
        # (requires others to know them). Constraints say n >= 2 anyway.
        return -1

    # Step 1: Find a potential candidate using elimination.
    # After this loop, 'candidate' is the only person who *could* be a celebrity.
    candidate = 0
    for i in range(1, n):
        # Ask: Does the current candidate know person i?
        if knows(candidate, i):
            # If candidate knows i, then 'candidate' cannot be the celebrity
            # because a celebrity knows no one else.
            # Therefore, 'i' becomes the new potential candidate.
            candidate = i
        # else (candidate does not know i):
            # If candidate does not know i, then 'i' cannot be the celebrity
            # because a celebrity must be known by everyone else (including candidate).
            # So, 'candidate' remains the potential celebrity.

    # Step 2: Verify if the potential candidate is actually the celebrity.
    # We need to check two conditions:
    # 1. The candidate knows no one else (except potentially themselves, although
    #    the definition implies not knowing *any* of the *other* n-1 people).
    # 2. Everyone else knows the candidate.
    
    for i in range(n):
        if i == candidate:
            continue # Don't check interactions with self based on definition

        # Check condition 1: Does the candidate know person i?
        # If candidate knows i (and i is not the candidate), then candidate is not a celebrity.
        if knows(candidate, i):
            return -1

        # Check condition 2: Does person i know the candidate?
        # If person i does NOT know the candidate, then candidate is not a celebrity.
        if not knows(i, candidate):
            return -1

    # If the candidate passed both verification checks for all other people,
    # then they are the celebrity.
    return candidate

# --- Testing Framework ---
def run_tests(test_cases):
    """
    Runs the provided test cases against the findCelebrity function.
    
    Args:
        test_cases: A list of tuples, where each tuple contains:
                    (graph_input, expected_output)
    """
    correct_count = 0
    total_tests = len(test_cases)
    global _graph  # Allow modification of the global graph
    global _api_calls # Allow modification/resetting of the call counter

    for i, (graph_input, expected_output) in enumerate(test_cases):
        _graph = graph_input  # Set the graph for the knows function for this test
        _api_calls = 0        # Reset API call counter for this test
        n = len(graph_input)
        
        # Check if graph dimensions are consistent
        valid_graph = True
        if n == 0:
             valid_graph = False
        else:
            for row in graph_input:
                if len(row) != n:
                    valid_graph = False
                    break
        
        if not valid_graph:
            print(f"Test {i+1}: Skipped (Invalid Graph Dimensions)")
            total_tests -= 1 # Adjust total count if skipping
            continue

        # Check n constraint
        if not (2 <= n <= 100):
             print(f"Test {i+1}: Skipped (n={n} out of range [2, 100])")
             total_tests -= 1 # Adjust total count if skipping
             continue
             
        actual_output = findCelebrity(n)
        result = actual_output == expected_output
        
        # Optional: Check API call count against 3n limit
        call_limit_ok = _api_calls <= 3 * n
        
        print(f"Test {i+1}: {result} (Output: {actual_output}, Expected: {expected_output}, API Calls: {_api_calls}, Limit: {3*n}, Within Limit: {call_limit_ok})")
        
        if result:
            correct_count += 1
        # You might want to fail the test if the call limit is exceeded, even if the result is correct
        # if result and not call_limit_ok:
        #    print(f"  -> Warning: Correct result but exceeded API call limit!")
            # correct_count -= 1 # Uncomment if exceeding limit invalidates the test pass

    print(f"\n{correct_count}/{total_tests} tests passed.")
    # Reset graph after all tests
    _graph = None 

# --- Define Test Cases ---
# Format: (graph_matrix, expected_celebrity_label_or_-1)
test_cases = [
    # Example 1
    ([[1,1,0],[0,1,0],[1,1,1]], 1), 
    # Example 2
    ([[1,0,1],[1,1,0],[0,1,1]], -1),
    # Basic cases
    ([[1,1],[1,1]], -1), # Two people know each other, no celebrity
    ([[1,0],[1,1]], 0),  # Person 0 is celebrity (1 knows 0, 0 knows no one else)
    ([[1,1],[0,1]], 1),  # Person 1 is celebrity (0 knows 1, 1 knows no one else)
    # More complex cases
    ([[1,0,0],[0,1,0],[1,1,1]], 1), # Person 1 is celebrity (0 knows 1, 2 knows 1; 1 knows no one else)
    ([[1,1,1],[1,1,1],[1,1,1]], -1), # Everyone knows everyone
    ([[1,0,0],[0,1,0],[0,0,1]], -1), # No one knows anyone else (except self)
    ([[1,0,1,0],[0,1,1,0],[0,0,1,0],[1,0,1,1]], 2), # Person 2 is celebrity (0,1,3 know 2; 2 knows no one else)
    ([[1,1,0,0],[0,1,0,0],[1,1,1,0],[1,1,1,1]], -1), # Person 2 knows 0 and 1, Person 3 knows everyone. No celebrity.
    # Larger case (n=5)
    ([
        [1, 1, 1, 0, 1],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0], # Person 2 is potential candidate (knows no one else)
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 1]
    ], 2), # Check: 0 knows 2? No. So 2 is not celebrity. Expected: -1
    # Corrected Larger case (n=5) where 2 IS celebrity
     ([
        [1, 0, 1, 1, 0], # 0 knows 2, 3
        [1, 1, 1, 0, 0], # 1 knows 0, 2
        [0, 0, 1, 0, 0], # 2 knows no one (else) -> Candidate
        [1, 0, 1, 1, 0], # 3 knows 0, 2
        [1, 1, 1, 1, 1]  # 4 knows 0, 1, 2, 3
    ], 2), # Verification: 2 knows 0? No. 2 knows 1? No. 2 knows 3? No. 2 knows 4? No.
           # 0 knows 2? Yes. 1 knows 2? Yes. 3 knows 2? Yes. 4 knows 2? Yes. -> Celebrity is 2.
    # Case with no celebrity, close call
     ([
        [1, 0, 1, 1, 0], # 0 knows 2, 3
        [1, 1, 1, 0, 0], # 1 knows 0, 2
        [0, 1, 1, 0, 0], # 2 knows 1 -> Not celebrity
        [1, 0, 1, 1, 0], # 3 knows 0, 2
        [1, 1, 1, 1, 1]  # 4 knows 0, 1, 2, 3
    ], -1),
    # Edge case n=2
    ([[1,0],[0,1]], -1), # Neither knows the other
]

# --- Run the tests ---
if __name__ == "__main__":
    run_tests(test_cases)