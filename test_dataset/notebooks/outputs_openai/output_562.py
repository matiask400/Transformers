def longestLine(M):
    if not M or not M[0]:
        return 0
    rows, cols = len(M), len(M[0])
    dp = [ [ [0]*4 for _ in range(cols) ] for _ in range(rows) ]
    max_len = 0
    for i in range(rows):
        for j in range(cols):
            if M[i][j] == 1:
                # Horizontal
                dp[i][j][0] = dp[i][j-1][0] + 1 if j > 0 else 1
                # Vertical
                dp[i][j][1] = dp[i-1][j][1] + 1 if i > 0 else 1
                # Diagonal
                dp[i][j][2] = dp[i-1][j-1][2] + 1 if i > 0 and j > 0 else 1
                # Anti-diagonal
                dp[i][j][3] = dp[i-1][j+1][3] + 1 if i > 0 and j < cols-1 else 1
                max_len = max(max_len, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])
    return max_len

def run_tests():
    test_cases = [
        (
            [[0,1,1,0],
             [0,1,1,0],
             [0,0,0,1]],
            3
        ),
        (
            [[1,1,1,1]],
            4
        ),
        (
            [[1],[1],[1],[1]],
            4
        ),
        (
            [[1,0,0,1],
             [1,1,1,1],
             [1,0,0,1]],
            4
        ),
        (
            [[0,0,0],
             [0,0,0]],
            0
        ),
        (
            [[1]],
            1
        ),
        (
            [[1,1,0,1],
             [0,1,1,1],
             [1,0,1,1]],
            3
        ),
        (
            [[1,1,1],
             [1,1,1],
             [1,1,1]],
            3
        ),
        (
            [[0]],
            0
        ),
        (
            [[1,0,1,1,0,1],
             [1,1,1,0,1,1],
             [0,1,1,1,1,0],
             [1,1,1,1,0,1]],
            4
        )
    ]
    correct = 0
    total = len(test_cases)
    for idx, (input_matrix, expected) in enumerate(test_cases):
        output = longestLine(input_matrix)
        result = output == expected
        print(result)
        if result:
            correct +=1
    print(f"{correct} / {total}")

if __name__ == "__main__":
    run_tests()