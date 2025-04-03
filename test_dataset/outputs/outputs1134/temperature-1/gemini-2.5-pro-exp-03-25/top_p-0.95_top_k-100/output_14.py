import sys
from collections import deque

# Set higher recursion depth limit for deep DFS cases, though BFS is often preferred for large grids.
# sys.setrecursionlimit(2000) # Uncomment if using DFS and hitting recursion depth limits

class Solution:
    """
    Solves the Pacific Atlantic Water Flow problem.
    Finds grid coordinates where water can flow to both the Pacific (top/left)
    and Atlantic (bottom/right) oceans.
    Water flows from a cell to an adjacent one with equal or lower height.
    """
    def pacificAtlantic_dfs(self, heights: list[list[int]]) -> list[list[int]]:
        """
        Solves the problem using Depth First Search (DFS).
        """
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        pacific_reachable = [[False for _ in range(n)] for _ in range(m)]
        atlantic_reachable = [[False for _ in range(n)] for _ in range(m)]

        def dfs(r, c, visited):
            """Performs DFS starting from (r, c) marking reachable cells."""
            # Mark current cell as visited
            visited[r][c] = True

            # Explore neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                # Check bounds for neighbor
                if 0 <= nr < m and 0 <= nc < n:
                    # Check if neighbor already visited for THIS ocean
                    if not visited[nr][nc]:
                        # Check height condition (can flow "up-stream" from current to neighbor)
                        if heights[nr][nc] >= heights[r][c]:
                            dfs(nr, nc, visited)

        # Start DFS from Pacific borders (top and left)
        for r in range(m):
            if not pacific_reachable[r][0]:
                dfs(r, 0, pacific_reachable)
        for c in range(n):
            if not pacific_reachable[0][c]:
                dfs(0, c, pacific_reachable)

        # Start DFS from Atlantic borders (bottom and right)
        for r in range(m):
            if not atlantic_reachable[r][n - 1]:
                dfs(r, n - 1, atlantic_reachable)
        for c in range(n):
            if not atlantic_reachable[m - 1][c]:
                dfs(m - 1, c, atlantic_reachable)

        # Find intersection of reachable cells
        result = []
        for r in range(m):
            for c in range(n):
                if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                    result.append([r, c])

        return result

    def pacificAtlantic_bfs(self, heights: list[list[int]]) -> list[list[int]]:
        """
        Solves the problem using Breadth First Search (BFS).
        """
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        pacific_reachable = [[False for _ in range(n)] for _ in range(m)]
        atlantic_reachable = [[False for _ in range(n)] for _ in range(m)]

        def bfs(queue, visited):
            """Performs BFS starting from initial cells in the queue."""
            q = deque(queue)
            while q:
                r, c = q.popleft()

                # Explore neighbors
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc

                    # Check bounds
                    if 0 <= nr < m and 0 <= nc < n:
                        # Check if visited and height condition
                        if not visited[nr][nc] and heights[nr][nc] >= heights[r][c]:
                            visited[nr][nc] = True
                            q.append((nr, nc))


        # Initialize queues and visited status for Pacific borders
        pacific_queue = []
        for r in range(m):
            if not pacific_reachable[r][0]:
                 pacific_reachable[r][0] = True
                 pacific_queue.append((r, 0))
        for c in range(n):
            if not pacific_reachable[0][c]: # Avoid adding (0,0) twice
                 pacific_reachable[0][c] = True
                 pacific_queue.append((0, c))

        # Initialize queues and visited status for Atlantic borders
        atlantic_queue = []
        for r in range(m):
             if not atlantic_reachable[r][n - 1]:
                 atlantic_reachable[r][n - 1] = True
                 atlantic_queue.append((r, n - 1))
        for c in range(n):
             if not atlantic_reachable[m - 1][c]: # Avoid adding (m-1, n-1) twice
                 atlantic_reachable[m - 1][c] = True
                 atlantic_queue.append((m - 1, c))

        # Run BFS for both oceans
        bfs(pacific_queue, pacific_reachable)
        bfs(atlantic_queue, atlantic_reachable)

        # Find intersection of reachable cells
        result = []
        for r in range(m):
            for c in range(n):
                if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                    result.append([r, c])

        return result

    # Use BFS by default as it avoids potential recursion depth issues
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
         return self.pacificAtlantic_bfs(heights)


def run_tests():
    solver = Solution()
    tests = [
        {
            "heights": [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]],
            "expected": [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        },
        {
            "heights": [[2,1],[1,2]],
            "expected": [[0,0],[0,1],[1,0],[1,1]]
        },
        {
            "heights": [[1]],
            "expected": [[0,0]]
        },
        {
            "heights": [[1,1],[1,1]],
            "expected": [[0,0],[0,1],[1,0],[1,1]]
        },
        {
            "heights": [[3,3,3],[3,0,3],[3,3,3]],
             "expected": [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]
        },
        {
             "heights": [[10,10,10],[10,1,10],[10,10,10]],
             "expected": [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]
        },
        {
             "heights": [[1,2,3],[8,9,4],[7,6,5]], # Example from LeetCode discussion
             "expected": [[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        },
         {
            "heights": [], # Edge case: empty grid
            "expected": []
        },
        {
             "heights": [[]], # Edge case: grid with empty row
             "expected": []
        }
    ]

    correct_count = 0
    print("Running tests...")
    for i, test in enumerate(tests):
        heights = test["heights"]
        expected = test["expected"]

        # The order of coordinates in the output list doesn't matter.
        # Sort both actual and expected results before comparison.
        # Alternatively, convert to sets of tuples.
        actual_raw = solver.pacificAtlantic(heights)

        # Sort lists of lists for consistent comparison
        actual_sorted = sorted(actual_raw)
        expected_sorted = sorted(expected)

        # Using sets of tuples is another robust way to compare regardless of order
        # actual_set = set(tuple(coord) for coord in actual_raw)
        # expected_set = set(tuple(coord) for coord in expected)
        # passed = (actual_set == expected_set)

        passed = (actual_sorted == expected_sorted)

        print(f"Test {i+1}: {passed}")
        if passed:
            correct_count += 1
        else:
            # Optionally print details for failed tests
            print(f"  Input: heights = {heights}")
            print(f"  Expected (sorted): {expected_sorted}")
            print(f"  Actual (sorted): {actual_sorted}")


    print(f"\n{correct_count}/{len(tests)} tests passed.")

# Main execution block
if __name__ == "__main__":
    run_tests()