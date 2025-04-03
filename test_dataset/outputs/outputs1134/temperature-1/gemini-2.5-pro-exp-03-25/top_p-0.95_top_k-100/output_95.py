import math # Not strictly needed, but good practice

def assignBikes(workers, bikes):
    """
    Assigns bikes to workers based on shortest Manhattan distance with tie-breaking rules.

    The assignment process iteratively selects the (worker, bike) pair with the 
    shortest Manhattan distance among available pairs. Ties are broken first by 
    smallest worker index, then by smallest bike index.

    Args:
        workers: A list of lists, where each inner list is [x, y] coordinates for a worker.
                   Example: [[0,0], [2,1]]
        bikes:   A list of lists, where each inner list is [x, y] coordinates for a bike.
                   Example: [[1,2], [3,3]]

    Returns:
        A list `ans` of length N (number of workers), where `ans[i]` is the 
        index (0-indexed) of the bike assigned to the i-th worker.
        Example: [1, 0]
    """
    n = len(workers)
    m = len(bikes)

    # 1. Calculate all worker-bike pair distances and store relevant information
    # We need distance, worker index, and bike index for sorting and assignment.
    all_pairs = []
    for i in range(n):  # Iterate through each worker
        for j in range(m):  # Iterate through each bike
            worker_coord = workers[i]
            bike_coord = bikes[j]
            # Calculate Manhattan distance
            dist = abs(worker_coord[0] - bike_coord[0]) + abs(worker_coord[1] - bike_coord[1])
            # Store as a tuple: (distance, worker_index, bike_index)
            # This structure allows sorting based on the required criteria.
            all_pairs.append((dist, i, j))

    # 2. Sort the pairs based on the assignment criteria:
    #    - Primary key: distance (ascending)
    #    - Secondary key: worker index (ascending)
    #    - Tertiary key: bike index (ascending)
    # Python's default tuple sorting handles this automatically.
    all_pairs.sort()

    # 3. Perform the assignment process iteratively using the sorted list
    result = [-1] * n          # Initialize result array for N workers with -1 (unassigned)
    worker_assigned = [False] * n # Track if worker i has been assigned a bike
    bike_assigned = [False] * m   # Track if bike j has been assigned to a worker
    assigned_count = 0        # Keep track of how many workers have been assigned

    # Iterate through the sorted pairs (best pairs first)
    for dist, worker_idx, bike_idx in all_pairs:
        # Check if both the worker and the bike are currently available
        if not worker_assigned[worker_idx] and not bike_assigned[bike_idx]:
            # Assign this bike to this worker
            result[worker_idx] = bike_idx
            # Mark both as assigned
            worker_assigned[worker_idx] = True
            bike_assigned[bike_idx] = True
            # Increment the count of assigned workers
            assigned_count += 1

            # Optimization: If all workers have been assigned, we can stop early.
            if assigned_count == n:
                break

    return result

# --- Test Framework ---
def run_tests():
    """
    Runs predefined test cases against the assignBikes function and prints results.
    """
    test_cases = [
        # Example 1 from description
        {"input": {"workers": [[0,0],[2,1]], "bikes": [[1,2],[3,3]]}, "expected": [1,0]},
        # Example 2 from description
        {"input": {"workers": [[0,0],[1,1],[2,0]], "bikes": [[1,0],[2,2],[2,1]]}, "expected": [0,2,1]},
        # Additional Test Case 1: Different coordinates
        {"input": {"workers": [[10,20],[30,50]], "bikes": [[5,5],[15,25],[35,55],[40,60]]}, "expected": [1,2]},
         # Additional Test Case 2: Single worker
        {"input": {"workers": [[0,0]], "bikes": [[0,0],[1,1]]}, "expected": [0]},
         # Additional Test Case 3: Tie in distance, broken by worker index
        {"input": {"workers": [[0,0],[1,0]], "bikes": [[0,1], [1,1]]}, "expected": [0,1]},
        # Additional Test Case 4: Tie in distance and worker index, broken by bike index
        {"input": {"workers": [[0,0]], "bikes": [[1,0],[0,1]]}, "expected": [0]},
        # Additional Test Case 5: More workers/bikes, various distances
        {"input": {"workers": [[0,0],[1,0],[2,0]], "bikes": [[0,1],[1,1],[2,1],[3,1]]}, "expected": [0,1,2]},
         # Additional Test Case 6: All bikes equidistant to one worker initially
        {"input": {"workers": [[0,0]], "bikes": [[1,0],[0,1],[-1,0],[0,-1]]}, "expected": [0]}, # Dist = 1 for all. Choose bike 0 first.
         # Additional Test Case 7: Larger coordinates
        {"input": {"workers": [[100,100],[200,200]], "bikes": [[101,101],[201,201],[50,50]]}, "expected": [0,1]}, # Dist(0,0)=2, Dist(0,1)=202, Dist(0,2)=100. Dist(1,0)=198, Dist(1,1)=2, Dist(1,2)=300. Pairs:(2,0,0), (2,1,1), ... Assign 0->0, then 1->1.
    ]

    correct_count = 0
    total_tests = len(test_cases)

    print("Running Tests...")
    for i, test in enumerate(test_cases):
        workers_input = test["input"]["workers"]
        bikes_input = test["input"]["bikes"]
        expected_output = test["expected"]

        # Execute the function with the test case inputs
        actual_output = assignBikes(workers_input, bikes_input)

        # Compare the actual output with the expected output
        passed = (actual_output == expected_output)
        print(f"Test {i + 1}: {passed}") # Print True for pass, False for fail
        if passed:
            correct_count += 1

    # Print the final summary