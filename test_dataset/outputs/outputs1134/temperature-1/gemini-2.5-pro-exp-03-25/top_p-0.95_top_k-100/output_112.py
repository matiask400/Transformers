import sys
from io import StringIO

def solve():
    """
    Solves the longest line of consecutive ones problem using dynamic programming.
    """
    def longestLine(M):
        """
        Finds the longest line of consecutive ones in a 01 matrix M.

        Args:
            M: A list of lists representing the 01 matrix.

        Returns:
            An integer representing the length of the longest line.
        """
        if not M or not M[0]:
            return 0

        rows = len(M)
        cols = len(M[0])
        max_len = 0

        # dp[r][c][d] stores the length of the consecutive line of 1s
        # ending at cell (r, c) in direction d.
        # Directions:
        # 0: Horizontal (left-to-right)
        # 1: Vertical (top-to-bottom)
        # 2: Diagonal (top-left to bottom-right)
        # 3: Anti-diagonal (top-right to bottom-left)
        dp = [[[0] * 4 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if M[r][c] == 1:
                    # Horizontal
                    if c > 0:
                        dp[r][c][0] = dp[r][c-1][0] + 1
                    else:
                        dp[r][c][0] = 1

                    # Vertical
                    if r > 0:
                        dp[r][c][1] = dp[r-1][c][1] + 1
                    else:
                        dp[r][c][1] = 1

                    # Diagonal
                    if r > 0 and c > 0:
                        dp[r][c][2] = dp[r-1][c-1][2] + 1
                    else:
                        dp[r][c][2] = 1

                    # Anti-diagonal
                    if r > 0 and c < cols - 1:
                        dp[r][c][3] = dp[r-1][c+1][3] + 1
                    else:
                        dp[r][c][3] = 1

                    # Update the overall maximum length
                    max_len = max(max_len, dp[r][c][0], dp[r][c][1], dp[r][c][2], dp[r][c][3])

        return max_len

    # --- Test Runner ---
    def run_tests():
        """
        Runs test cases against the longestLine function.
        """
        test_cases = [
            ([[0,1,1,0],
              [0,1,1,0],
              [0,0,0,1]], 3),
            ([[1,1,1,1],
              [0,1,1,0],
              [0,0,0,1]], 4),
            ([[0,0,0],
              [0,0,0],
              [0,0,0]], 0),
            ([[1]], 1),
            ([[0]], 0),
            ([[]], 0), # Empty matrix
            ([], 0),    # Empty list
            ([[1,0,0,1],
              [0,1,0,1],
              [0,0,1,1],
              [1,1,1,1]], 4), # Diagonal and horizontal
             ([[1,1,0,1],
              [1,1,1,1],
              [0,1,1,1],
              [1,0,1,1]], 4), # Vertical and anti-diagonal
            ([[0,1,0,1,1],
              [1,1,0,1,0],
              [0,1,0,1,1],
              [1,0,1,0,1],
              [1,1,1,1,1]], 5) # Long horizontal
        ]

        correct_count = 0
        total_tests = len(test_cases)

        # Redirect stdout to capture print statements
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()

        for i, (matrix, expected) in enumerate(test_cases):
            # Create a copy to avoid modifying the original test case if needed
            matrix_copy = [row[:] for row in matrix]
            result = longestLine(matrix_copy)
            passed = result == expected
            print(passed)
            if passed:
                correct_count += 1

        # Restore stdout
        sys.stdout = old_stdout
        # Print captured output
        print(captured_output.getvalue(), end="")

        # Print summary
        print(f"{correct_count}/{total_tests}")

    run_tests()

# Execute the solver function
solve()