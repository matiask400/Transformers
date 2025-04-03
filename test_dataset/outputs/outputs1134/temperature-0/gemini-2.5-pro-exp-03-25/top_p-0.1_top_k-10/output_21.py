import sys

# Set higher recursion depth for potentially deep calculations, although not strictly necessary for this iterative approach.
# sys.setrecursionlimit(2000) 

def solve():
    """
    Solves the maximum side-length square problem using prefix sums and binary search.
    """
    def maxSideLength(mat, threshold):
        """
        Finds the maximum side-length of a square subgrid with sum <= threshold.

        Args:
            mat: A list of lists representing the m x n matrix.
            threshold: An integer threshold for the sum.

        Returns:
            The maximum side length k, or 0 if no such square exists.
        """
        if not mat or not mat[0]:
            return 0

        m = len(mat)
        n = len(mat[0])

        # 1. Compute prefix sums (integral image)
        # prefix_sum[i][j] stores the sum of the rectangle from (0, 0) to (i-1, j-1)
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                prefix_sum[r + 1][c + 1] = mat[r][c] + \
                                           prefix_sum[r][c + 1] + \
                                           prefix_sum[r + 1][c] - \
                                           prefix_sum[r][c]

        # Helper function to calculate the sum of a square subgrid
        def get_square_sum(r, c, k):
            """Calculates sum of square with top-left (r, c) and side k using prefix sums."""
            # Note: (r, c) are 0-based indices in the original matrix 'mat'.
            # The corresponding bottom-right corner in 'mat' is (r + k - 1, c + k - 1).
            # In the 1-based prefix_sum array, this corresponds to:
            # Bottom-right: (r + k, c + k)
            # Top-right:    (r, c + k)
            # Bottom-left:  (r + k, c)
            # Top-left (to subtract): (r, c)
            
            # Ensure indices are within bounds for prefix_sum access
            r1, c1 = r, c           # Top-left corner for subtraction (exclusive in prefix sum terms)
            r2, c2 = r + k, c + k   # Bottom-right corner (inclusive in prefix sum terms)

            if r2 > m or c2 > n: # Should not happen if check() loops correctly, but good practice
                 return float('inf') 

            return prefix_sum[r2][c2] - prefix_sum[r1][c2] - prefix_sum[r2][c1] + prefix_sum[r1][c1]

        # Helper function to check if any square of size k has sum <= threshold
        def check(k):
            """Checks if there exists a k x k square with sum <= threshold."""
            if k == 0:
                return True # A 0x0 square trivially exists with sum 0

            # Iterate through all possible top-left corners (r, c) for a k x k square
            # The bottom-right corner is (r + k - 1, c + k - 1)
            # So, r + k - 1 < m => r < m - k + 1 => r <= m - k
            # And, c + k - 1 < n => c < n - k + 1 => c <= n - k
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if get_square_sum(r, c, k) <= threshold:
                        return True
            return False

        # 2. Binary search for the maximum side length k
        low = 0
        high = min(m, n)
        max_k = 0 # Stores the largest k found so far that satisfies the condition

        while low <= high:
            k = low + (high - low) // 2
            if check(k):
                # A square of size k exists, this k is a potential answer.
                # Try to find a larger one.
                max_k = k
                low = k + 1
            else:
                # No square of size k exists (or all have sum > threshold).
                # Need to try smaller sizes.
                high = k - 1

        return max_k

    # --- Test Harness ---
    test_cases = [
        ([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4, 2),
        ([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], 1, 0),
        ([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 6, 3),
        ([[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], 40184, 2),
        ([[1]], 0, 0), # Single element, threshold 0
        ([[1]], 1, 1), # Single element, threshold 1
        ([[10]], 5, 0), # Single element, threshold 5
        ([[0,0,0],[0,0,0],[0,0,0]], 0, 3), # All zeros
        ([[10,20],[30,40]], 9, 0), # No 1x1 square possible
        ([[10,20],[30,40]], 10, 1), # Only 1x1 square at (0,0)
        ([[10,20],[30,5]], 35, 1), # Only 1x1 squares possible (at (0,0) and (1,1))
        ([[1,1,1],[1,1,1],[1,1,1]], 4, 2), # 2x2 square sum is 4
        ([[1,1,1],[1,1,1],[1,1,1]], 3, 1), # Only 1x1 possible
        ([[1,1,1],[1,1,1],[1,1,1]], 9, 3), # 3x3 square sum is 9
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (mat, threshold, expected_output) in enumerate(test_cases):
        # Deep copy mat if necessary, though this function doesn't modify it
        # mat_copy = [row[:] for row in mat] 
        
        result = maxSideLength(mat, threshold)
        
        passed = (result == expected_output)
        print(f"Test Case {i + 1}: {passed}")
        if passed:
            correct_count += 1
        # Optional: Print details on failure
        # else:
        #    print(f"  Input Mat: {mat}")
        #    print(f"  Input Threshold: {threshold}")
        #    print(f"  Expected Output: {expected_output}")
        #    print(f"  Actual Output: {result}")


    print(f"\n{correct_count} / {total_tests} correct tests.")

# Execute the solution and tests
solve()