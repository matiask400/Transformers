import sys
import io

def solve():
    """
    Solves the maximum side length problem using prefix sums and binary search.
    """
    def maxSideLength(mat, threshold):
        """
        Finds the maximum side length of a square subgrid with sum <= threshold.

        Args:
            mat: A list of lists representing the m x n matrix.
            threshold: The maximum allowed sum for a square subgrid.

        Returns:
            The maximum side length k, or 0 if no such square exists.
        """
        if not mat or not mat[0]:
            return 0

        m = len(mat)
        n = len(mat[0])

        # 1. Calculate Prefix Sums
        # P[r+1][c+1] stores the sum of the rectangle from mat[0][0] to mat[r][c]
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                P[r + 1][c + 1] = mat[r][c] + P[r][c + 1] + P[r + 1][c] - P[r][c]

        # Helper function to get sum of a square using prefix sums
        def get_square_sum(r, c, k):
            """
            Calculates the sum of a square of side k with top-left corner (r, c) in mat.
            Uses the 1-based indexed prefix sum array P.
            """
            # Coordinates in P corresponding to the square corners in mat
            # mat top-left (r, c) corresponds to P indices just before it: P[r][c]
            # mat bottom-right (r+k-1, c+k-1) corresponds to P index P[r+k][c+k]
            r1, c1 = r, c       # Top-left corner in mat (used to index P)
            r2, c2 = r + k, c + k # Bottom-right corner + 1 for P indexing

            # Check bounds (although loops in check should prevent out-of-bounds)
            if r2 > m or c2 > n:
                return float('inf') # Should not happen if called correctly

            # Calculate sum using the inclusion-exclusion principle on P
            return P[r2][c2] - P[r1][c2] - P[r2][c1] + P[r1][c1]

        # Helper function check(k): checks if any square of side k has sum <= threshold
        def check(k):
            """
            Checks if there exists at least one square of side k
            whose sum is less than or equal to the threshold.
            """
            if k == 0:
                return True # A square of size 0 always "exists" conceptually
            # If k is larger than the matrix dimensions, no such square can exist
            if k > m or k > n:
                return False

            # Iterate through all possible top-left corners (r, c) for a k x k square
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    square_sum = get_square_sum(r, c, k)
                    if square_sum <= threshold:
                        return True # Found a valid square
            return False # No square of size k found

        # 2. Binary Search for the maximum side length k
        low = 0
        high = min(m, n)
        max_k = 0 # Stores the largest k found so far for which check(k) is true

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                # If a square of size 'mid' works, it's a potential answer.
                # Try searching for larger squares.
                max_k = mid
                low = mid + 1
            else:
                # If no square of size 'mid' works, 'mid' is too large.
                # Try searching for smaller squares.
                high = mid - 1

        return max_k

    # --- Testing Framework ---
    tests = [
        {"input": {"mat": [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], "threshold": 4}, "expected": 2},
        {"input": {"mat": [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], "threshold": 1}, "expected": 0},
        {"input": {"mat": [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], "threshold": 6}, "expected": 3},
        {"input": {"mat": [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], "threshold": 40184}, "expected": 2},
        {"input": {"mat": [[1]], "threshold": 0}, "expected": 0},
        {"input": {"mat": [[1]], "threshold": 1}, "expected": 1},
        {"input": {"mat": [[10000]], "threshold": 9999}, "expected": 0},
        {"input": {"mat": [[10000]], "threshold": 10000}, "expected": 1},
        {"input": {"mat": [[0,0,0],[0,0,0],[0,0,0]], "threshold": 0}, "expected": 3},
         {"input": {"mat": [[1,2,3],[4,5,6],[7,8,9]], "threshold": 1}, "expected": 0},
         {"input": {"mat": [[1,2,3],[4,5,6],[7,8,9]], "threshold": 5}, "expected": 1}, # 1x1 squares [1],[2],[3],[4],[5] work
         {"input": {"mat": [[1,2,3],[4,5,6],[7,8,9]], "threshold": 12}, "expected": 1}, # 2x2 squares: 1+2+4+5=12 works
         {"input": {"mat": [[1,2,3],[4,5,6],[7,8,9]], "threshold": 11}, "expected": 1}, # 2x2 squares: 1+2+4+5=12 > 11, 2+3+5+6=16, 4+5+7+8=24, 5+6+8+9=28
         {"input": {"mat": [[1,2,3],[4,5,6],[7,8,9]], "threshold": 45}, "expected": 3}, # 3x3 square sum = 45
         {"input": {"mat": [[1,2,3],[4,5,6],[7,8,9]], "threshold": 44}, "expected": 2}, # Max 2x2 sum is 28 <= 44, 3x3 sum is 45 > 44
    ]

    correct_count = 0
    for i, test in enumerate(tests):
        mat_input = test["input"]["mat"]
        threshold_input = test["input"]["threshold"]
        expected_output = test["expected"]
        # Redirect stdout to capture print statements
        old_stdout = sys.stdout
        sys.stdout = captured_output = io.StringIO()
        # Execute the function
        actual_output = maxSideLength(mat_input, threshold_input)
        # Restore stdout
        sys.stdout = old_stdout
        # Get printed output
        # printed_output = captured_output.getvalue().strip()

        # Compare results
        result = actual_output == expected_output
        print(result)
        if result:
            correct_count += 1

    print(f"{correct_count}/{len(tests)}")

# Execute the solver function that includes the tests
solve()