import collections
import sys

# Increase recursion depth limit for deep graphs in DFS (though BFS is usually preferred for bipartite check)
# sys.setrecursionlimit(2005) 

def solve():
    """
    Solves the Possible Bipartition problem using Breadth-First Search (BFS) for graph coloring.
    """
    def possible_bipartition(N, dislikes):
        """
        Checks if a set of N people can be split into two groups based on dislikes.

        Args:
            N: The number of people (numbered 1 to N).
            dislikes: A list of pairs [a, b] indicating person a dislikes person b.

        Returns:
            True if the split is possible, False otherwise.
        """
        if not dislikes:
            return True # No dislikes, trivially possible

        # Build the adjacency list representation of the graph
        # Use N+1 size to handle 1-based indexing easily
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        # Color array: 0 = uncolored, 1 = group 1, -1 = group 2
        colors = [0] * (N + 1)

        for i in range(1, N + 1):
            # If person i is already colored (part of a visited component), skip
            if colors[i] != 0:
                continue

            # Start BFS for this connected component
            queue = collections.deque()
            colors[i] = 1  # Assign person i to group 1
            queue.append(i)

            while queue:
                person = queue.popleft()
                current_color = colors[person]

                for neighbor in graph[person]:
                    if colors[neighbor] == 0:
                        # If neighbor is uncolored, assign the opposite color
                        colors[neighbor] = -current_color
                        queue.append(neighbor)
                    elif colors[neighbor] == current_color:
                        # If neighbor has the same color, conflict found!
                        return False # Not bipartite

        # If the loop completes without conflicts, it's possible
        return True

    # --- Testing Framework ---
    tests = [
        {"input": {"N": 4, "dislikes": [[1,2],[1,3],[2,4]]}, "expected": True},
        {"input": {"N": 3, "dislikes": [[1,2],[1,3],[2,3]]}, "expected": False},
        {"input": {"N": 5, "dislikes": [[1,2],[2,3],[3,4],[4,5],[1,5]]}, "expected": False},
        {"input": {"N": 1, "dislikes": []}, "expected": True},
        {"input": {"N": 2, "dislikes": []}, "expected": True},
        {"input": {"N": 2, "dislikes": [[1,2]]}, "expected": True},
        {"input": {"N": 10, "dislikes": [[1,2],[3,4],[5,6],[7,8],[9,10]]}, "expected": True}, # Disconnected components
        {"input": {"N": 10, "dislikes": [[1,2],[2,3],[3,1]]}, "expected": False}, # Odd cycle
        {"input": {"N": 6, "dislikes": [[1,2],[2,3],[3,4],[4,5],[5,6],[6,1]]}, "expected": True}, # Even cycle
        {"input": {"N": 5, "dislikes": [[1, 2], [3, 4], [4, 5], [3, 5]]}, "expected": False}, # Disconnected component + odd cycle
    ]

    correct_count = 0
    for i, test in enumerate(tests):
        N_val = test["input"]["N"]
        dislikes_val = test["input"]["dislikes"]
        result = possible_bipartition(N_val, dislikes_val)
        expected = test["expected"]
        passed = result == expected
        print(f"Test {i + 1}: {passed}")
        if passed:
            correct_count += 1

    print(f"{correct_count}/{len(tests)} tests passed.")

# Execute the solver function
solve()