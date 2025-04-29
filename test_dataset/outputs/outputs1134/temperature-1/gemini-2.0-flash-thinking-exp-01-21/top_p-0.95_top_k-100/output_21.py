def maxSideLength(mat, threshold):
    m = len(mat)
    n = len(mat[0])
    prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + mat[i - 1][j - 1]

    def get_square_sum(row, col, side):
        if row + side > m or col + side > n:
            return float('inf')
        return prefix_sum[row + side][col + side] - prefix_sum[row][col + side] - prefix_sum[row + side][col] + prefix_sum[row][col]

    max_side = 0
    for side in range(1, min(m, n) + 1):
        found_square = False
        for r in range(m - side + 1):
            for c in range(n - side + 1):
                if get_square_sum(r, c, side) <= threshold:
                    found_square = True
                    break
            if found_square:
                break
        if found_square:
            max_side = side
        else:
            if max_side > 0:
                return max_side
            elif side == 1 and max_side == 0:
                for r in range(m):
                    for c in range(n):
                        if mat[r][c] <= threshold:
                            return 1
                return 0
            else:
                if max_side == 0:
                    for r in range(m):
                        for c in range(n):
                            if mat[r][c] <= threshold:
                                return 1
                    return 0
                else:
                    return max_side
    return max_side

def run_tests():
    test_cases = [
        ([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4, 2),
        ([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], 1, 0),
        ([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 6, 3),
        ([[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], 40184, 2),
        ([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]], 1, 1),
        ([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]], 16, 4),
        ([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]], 15, 3),
        ([[5,5,5],[5,5,5],[5,5,5]], 30, 2)
    ]
    correct_count = 0
    for i, (mat, threshold, expected) in enumerate(test_cases):
        result = maxSideLength(mat, threshold)
        if result == expected:
            print(True)
            correct_count += 1
        else:
            print(False)
    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()