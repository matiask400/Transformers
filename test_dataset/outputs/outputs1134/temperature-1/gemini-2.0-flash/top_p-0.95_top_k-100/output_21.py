def maxSideLength(mat, threshold):
    m = len(mat)
    n = len(mat[0])
    prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + mat[i - 1][j - 1]
    
    max_side = 0
    for side in range(1, min(m, n) + 1):
        found = False
        for i in range(side, m + 1):
            for j in range(side, n + 1):
                square_sum = prefix_sum[i][j] - prefix_sum[i - side][j] - prefix_sum[i][j - side] + prefix_sum[i - side][j - side]
                if square_sum <= threshold:
                    max_side = side
                    found = True
                    break
            if found:
                break
        if not found and side == 1 and max_side == 0:
            return 0
    return max_side

def test_maxSideLength():
    test_cases = [
        ([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4, 2),
        ([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], 1, 0),
        ([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 6, 3),
        ([[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], 40184, 2)
    ]
    
    correct_tests = 0
    total_tests = len(test_cases)
    
    for mat, threshold, expected in test_cases:
        result = maxSideLength(mat, threshold)
        if result == expected:
            print("True")
            correct_tests += 1
        else:
            print("False")
    
    print(f"{correct_tests}/{total_tests}")

if __name__ == "__main__":
    test_maxSideLength()