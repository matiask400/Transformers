import math # Not strictly necessary for Manhattan distance, but good practice

# Function to calculate Manhattan distance
def manhattan_distance(p1, p2):
    """Calculates the Manhattan distance between two points p1 and p2."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def assign_bikes(workers, bikes):
    """
    Assigns bikes to workers based on shortest Manhattan distance with tie-breaking.

    Args:
        workers: A list of worker coordinates [[x1, y1], [x2, y2], ...].
        bikes: A list of bike coordinates [[x1, y1], [x2, y2], ...].

    Returns:
        A list ans of length N, where ans[i] is the index of the bike assigned 
        to the i-th worker.
    """
    N = len(workers)
    M = len(bikes)

    # 1. Calculate all possible (worker, bike) pairs with their distances.
    # Store them as tuples: (distance, worker_index, bike_index)
    all_pairs = []
    for i in range(N):
        for j in range(M):
            dist = manhattan_distance(workers[i], bikes[j])
            all_pairs.append((dist, i, j))

    # 2. Sort the pairs. Python's default tuple sorting works correctly:
    #    - Sorts primarily by distance (ascending).
    #    - For ties in distance, sorts by worker_index (ascending).
    #    - For ties in both distance and worker_index, sorts by bike_index (ascending).
    all_pairs.sort()

    # 3. Iterate through sorted pairs and assign bikes greedily.
    worker_assigned = [False] * N  # Track if a worker has been assigned a bike
    bike_taken = [False] * M      # Track if a bike has been taken
    result = [-1] * N             # Stores the assigned bike index for each worker
    assigned_count = 0            # Count how many workers have been assigned

    for dist, worker_idx, bike_idx in all_pairs:
        # Stop if all workers have been assigned
        if assigned_count == N:
            break

        # Check if both the worker and the bike are available
        if not worker_assigned[worker_idx] and not bike_taken[bike_idx]:
            # Assign the bike to the worker
            result[worker_idx] = bike_idx
            
            # Mark worker as assigned and bike as taken
            worker_assigned[worker_idx] = True
            bike_taken[bike_idx] = True
            
            # Increment the count of assigned workers
            assigned_count += 1

    return result

# --- Test Framework ---
def run_tests():
    """Runs test cases against the assign_bikes function."""
    test_cases = [
        # Example 1
        {
            "input": {"workers": [[0,0],[2,1]], "bikes": [[1,2],[3,3]]},
            "expected": [1,0]
        },
        # Example 2
        {
            "input": {"workers": [[0,0],[1,1],[2,0]], "bikes": [[1,0],[2,2],[2,1]]},
            "expected": [0,2,1]
        },
        # Simple case
        {
            "input": {"workers": [[1,1],[5,5]], "bikes": [[2,2],[6,6],[7,7]]},
            "expected": [0,1]
        },
        # One worker
        {
            "input": {"workers": [[0,0]], "bikes": [[1,1],[2,2]]},
            "expected": [0]
        },
        # Tie-breaking case (distance tie, worker index tie)
        {
             "input": {"workers": [[10,10],[11,11]], "bikes": [[0,0],[1,1],[10,11]]},
             # W0(10,10), W1(11,11) | B0(0,0), B1(1,1), B2(10,11)
             # Pairs:
             # (W0,B0): dist=20 -> (20, 0, 0)
             # (W0,B1): dist=18 -> (18, 0, 1)
             # (W0,B2): dist=1  -> (1, 0, 2)
             # (W1,B0): dist=22 -> (22, 1, 0)
             # (W1,B1): dist=20 -> (20, 1, 1)
             # (W1,B2): dist=1  -> (1, 1, 2)
             # Sorted: [(1, 0, 2), (1, 1, 2), (18, 0, 1), (20, 0, 0), (20, 1, 1), (22, 1, 0)]
             # 1. (1, 0, 2): Assign B2 to W0. res=[2,-1], w=[T,F], b=[F,F,T], cnt=1
             # 2. (1, 1, 2): W1 avail, B2 *not* avail. Skip.
             # 3. (18, 0, 1): W0 *not* avail. Skip.
             # 4. (20, 0, 0): W0 *not* avail. Skip.
             # 5. (20, 1, 1): W1 avail, B1 avail. Assign B1 to W1. res=[2,1], w=[T,T], b=[F,T,T], cnt=2
             # Done. Expected: [2, 1]
             "expected": [2, 1]
        },
        # Tie-breaking case (distance tie, worker index decides)
        {
            "input": {"workers": [[0,0],[0,1]], "bikes": [[1,0],[1,1]]},
             # W0(0,0), W1(0,1) | B0(1,0), B1(1,1)
             # Pairs:
             # (W0, B0): dist=1 -> (1, 0, 0)
             # (W0, B1): dist=2 -> (2, 0, 1)
             # (W1, B0): dist=2 -> (2, 1, 0)
             # (W1, B1): dist=1 -> (1, 1, 1)
             # Sorted: [(1, 0, 0), (1, 1, 1), (2, 0, 1), (2, 1, 0)]
             # 1. (1, 0, 0): Assign B0 to W0. res=[0,-1], w=[T,F], b=[T,F], cnt=1
             # 2. (1, 1, 1): W1 avail, B1 avail. Assign B1 to W1. res=[0,1], w=[T,T], b=[T,T], cnt=2
             # Done. Expected: [0, 1]
            "expected": [0,1]
        },
         # Larger coordinates
        {
            "input": {"workers": [[100, 100], [200, 200]], "bikes": [[101, 101], [201, 201], [50, 50]]},
            # W0(100,100), W1(200,200) | B0(101,101), B1(201,201), B2(50,50)
            # Pairs:
            # (W0,B0): dist=2 -> (2, 0, 0)
            # (W0,B1): dist=202 -> (202, 0, 1)
            # (W0,B2): dist=100 -> (100, 0, 2)
            # (W1,B0): dist=198 -> (198, 1, 0)
            # (W1,B1): dist=2 -> (2, 1, 1)
            # (W1,B2): dist=300 -> (300, 1, 2)
            # Sorted: [(2, 0, 0), (2, 1, 1), (100, 0, 2), (198, 1, 0), (202, 0, 1), (300, 1, 2)]
            # 1. (2, 0, 0): Assign B0 to W0. res=[0,-1], w=[T,F], b=[T,F,F], cnt=1
            # 2. (2, 1, 1): Assign B1 to W1. res=[0,1], w=[T,T], b=[T,T,F], cnt=2
            # Done. Expected: [0, 1]
            "expected": [0, 1]
        }
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        workers_input = test_case["input"]["workers"]
        bikes_input = test_case["input"]["bikes"]
        expected_output = test_case["expected"]
        
        # Make copies to avoid modifying original test case data if function mutates input
        workers_copy = [list(w) for w in workers_input]