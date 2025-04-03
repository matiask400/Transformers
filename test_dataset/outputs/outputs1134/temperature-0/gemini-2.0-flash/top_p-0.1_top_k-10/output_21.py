def maxSideLength(mat, threshold):
    m = len(mat)
    n = len(mat[0])
    prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + mat[i - 1][j - 1]
    
    def get_square_sum(row, col, side):
        if row - side < 0 or col - side < 0:
            return float('inf')
        return prefix_sum[row][col] - prefix_sum[row - side][col] - prefix_sum[row][col - side] + prefix_sum[row - side][col - side]
    
    max_side = 0
    for side in range(1, min(m, n) + 1):
        found = False
        for i in range(side, m + 1):
            for j in range(side, n + 1):
                if get_square_sum(i, j, side) <= threshold:
                    max_side = side
                    found = True
                    break
            if found:
                break
        if not found and max_side == 0:
            return 0
        elif not found:
            break
    return max_side

def test_maxSideLength():
    test_cases = [
        ([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4, 2),
        ([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], 1, 0),
        ([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 6, 3),
        ([[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], 40184, 2)
    ]
    
    correct_count = 0
    total_count = len(test_cases)
    
    for i, (mat, threshold, expected) in enumerate(test_cases):
        result = maxSideLength(mat, threshold)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Got: {result})")
    
    print(f"\nCorrect: {correct_count}/{total_count}")

if __name__ == "__main__":
    test_maxSideLength()