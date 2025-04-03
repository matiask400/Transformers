import collections
from collections import deque

def solve():
    """
    Solves the Possible Bipartition problem and runs tests.
    """

    def possibleBipartition(N, dislikes):
        """
        Checks if N people can be split into two groups based on dislikes.

        Args:
            N: The number of people (numbered 1 to N).
            dislikes: A list of pairs [a, b] indicating person a dislikes person b.

        Returns:
            True if a valid bipartition exists, False otherwise.
        """
        # Build the adjacency list representation of the graph
        # Nodes are people (1 to N)
        # Edges represent dislikes
        adj = collections.defaultdict(list)
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u) # Dislike is mutual for grouping purposes

        # colors dictionary stores the group (color) assigned to each person
        # -1: uncolored, 0: group 0, 1: group 1
        colors = {} 

        # Iterate through each person. If a person hasn't been assigned a group yet,
        # start a traversal (BFS or DFS) from that person to color their connected component.
        for i in range(1, N + 1):
            if i not in colors:
                # Start BFS from person i, assign them to group 0 initially
                q = deque([(i, 0)]) # Store (person, color)
                colors[i] = 0

                while q:
                    u, color_u = q.popleft()

                    # Check all neighbors (people disliked by u)
                    for v in adj[u]:
                        if v not in colors:
                            # If neighbor v is uncolored, assign the opposite color
                            colors[v] = 1 - color_u
                            q.append((v, 1 - color_u))
                        elif colors[v] == color_u:
                            # If neighbor v has the same color, it's impossible to partition
                            return False # Conflict found

        # If the loop completes without finding any conflicts, a valid partition exists
        return True

    # Test cases
    tests = [
        {"N": 4, "dislikes": [[1,2],[1,3],[2,4]], "expected": True},
        {"N": 3, "dislikes": [[1,2],[1,3],[2,3]], "expected": False},
        {"N": 5, "dislikes": [[1,2],[2,3],[3,4],[4,5],[1,5]], "expected": False},
        {"N": 1, "dislikes": [], "expected": True},
        {"N": 2, "dislikes": [], "expected": True},
        {"N": 2, "dislikes": [[1,2]], "expected": True},
        {"N": 10, "dislikes": [[1,2],[3,4],[5,6],[7,8],[9,10]], "expected": True}, # Disconnected components
        {"N": 10, "dislikes": [[1,2],[2,3],[3,1]], "expected": False}, # Odd cycle (triangle)
        {"N": 5, "dislikes": [[1,2],[3,4],[1,5],[2,5]], "expected": False}, # Conflict: 1(0)-2(1), 1(0)-5(1), but 2(1)-5(1) conflict
        {"N": 6, "dislikes": [[1,2],[1,3],[4,5],[4,6]], "expected": True}, # Two separate bipartite components
        {"N": 100, "dislikes": [], "expected": True}, # Larger N, no dislikes
        # A slightly larger test case with a potential cycle
        {"N": 8, "dislikes": [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,1]], "expected": True}, # Even cycle (length 8)
        {"N": 7, "dislikes": [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,1]], "expected": False}, # Odd cycle (length 7)
    ]

    correct_count = 0
    for i, test in enumerate(tests):
        N = test["N"]
        dislikes = test["dislikes"]
        expected = test["expected"]
        # Make a copy of dislikes if the function modifies it (though this one doesn't)
        # dislikes_copy = [list(pair) for pair in dislikes] 
        result = possibleBipartition(N, dislikes)
        passed = result == expected
        print(f"{passed}") # Print True or False per test
        if passed:
            correct_count += 1

    print(f"{correct_count}/{len(tests)}") # Print final score

# Execute the solve function
solve()