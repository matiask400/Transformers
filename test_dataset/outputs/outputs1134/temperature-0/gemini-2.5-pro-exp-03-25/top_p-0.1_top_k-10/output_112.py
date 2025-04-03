import sys 
# Setting a reasonable recursion depth, although the iterative DP doesn't need it.
# sys.setrecursionlimit(20000) 

def solve():
    """
    Solves the longest line of consecutive ones problem using Dynamic Programming
    and runs test cases.
    """

    def longestLine(M):
        """
        Finds the longest line of consecutive ones in a 01 matrix M.
        The line can be horizontal, vertical, diagonal, or anti-diagonal.

        Args:
            M: A list of lists of integers (0 or 1) representing the matrix.

        Returns:
            An integer representing the length of the longest line.
        """
        # Handle empty matrix edge cases
        if not M: 
            return 0
        rows = len(M)
        if rows == 0:
             return 0
        cols = len(M[0])
        if cols == 0:
            return 0
            
        max_length = 0
        
        # dp[r][c][k] stores the length of the line of consecutive 1s
        # ending at cell (r, c) in direction k.
        # k=0: horizontal (left to right)
        # k=1: vertical (top to bottom)
        # k=2: diagonal (top-left to bottom-right)
        # k=3: anti-diagonal (top-right to bottom-left)
        dp = [[[0] * 4 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if M[r][c] == 1:
                    # Calculate length for each direction ending at (r, c)
                    
                    # Horizontal (k=0)
                    if c > 0:
                        dp[r][c][0] = dp[r][c-1][0] + 1
                    else:
                        dp[r][c][0] = 1
                    
                    # Vertical (k=1)
                    if r > 0:
                        dp[r][c][1] = dp[r-1][c][1] + 1
                    else:
                        dp[r][c][1] = 1
                        
                    # Diagonal (k=2)
                    if r > 0 and c > 0:
                        dp[r][c][2] = dp[r-1][c-1][2] + 1
                    else:
                        dp[r][c][2] = 1
                        
                    # Anti-diagonal (k=3)
                    # Depends on the cell top-right: (r-1, c+1)
                    if r > 0 and c < cols - 1:
                        dp[r][c][3] = dp[r-1][c+1][3] + 1
                    else:
                        dp[r][c][3] = 1

                    # Update the overall maximum length found so far
                    current_max = max(dp[r][c][0], dp[r][c][1], dp[r][c][2], dp[r][c][3])
                    max_length = max(max_length, current_max)
                    
        return max_length

    # --- Test Framework ---
    test_cases = [
        ([[0,1,1,0], [0,1,1,0], [0,0,0,1]], 3),
        ([[1,1,1,1], [0,1,1,0], [0,0,0,1]], 4),
        ([[0,0,0],[0,0,0],[0,0,0]], 0),
        ([[1,1],[1,1]], 2),
        ([[1]], 1),
        ([[0]], 0),
        ([], 0), # Test case for empty list
        ([[]], 0), # Test case for list containing an empty list
        ([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], 4), # Diagonal
        ([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]], 4), # Anti-diagonal
        ([[1,1,0,1,1,1]], 3), # Horizontal
        ([[1],[0],[1],[1]], 2), # Vertical
        ([[1,1,1],[1,0,1],[1,1,1]], 3),
        ([[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,0,1],[1,0,0,0,1]], 3), # Mixed
        ([[1 for _ in range(100)] for _ in range(100)], 100), # Large all ones
        ([[0 for _ in range(50)] for _ in range(50)], 0), # Large all zeros
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (matrix, expected_output) in enumerate(test_cases):