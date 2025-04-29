def max_side_length(mat, threshold):
    m = len(mat)
    n = len(mat[0])
    prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            prefix_sum[i + 1][j + 1] = prefix_sum[i + 1][j] + prefix_sum[i][j + 1] - prefix_sum[i][j] + mat[i][j]

    max_side = 0
    for side in range(1, min(m, n) + 1):
        found_square = False
        for i in range(m - side + 1):
            for j in range(n - side + 1):
                square_sum = prefix_sum[i + side][j + side] - prefix_sum[i][j + side] - prefix_sum[i + side][j] + prefix_sum[i][j]
                if square_sum <= threshold:
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
                for i in range(m):
                    for j in range(n):
                        if mat[i][j] <= threshold:
                            return 1
                return 0
            elif side == 1 and max_side > 0:
                return max_side
            elif max_side > 0:
                return max_side
            else:
                continue
    return max_side

def test_max_side_length():
    test_cases = [
        ([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4, 2),
        ([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], 1, 0),
        ([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 6, 3),
        ([[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], 40184, 2),
        ([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]], 1, 0),
        ([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]], 4, 2),
        ([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]], 16, 4),
        ([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]], 17, 4),
        ([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]], 0, 0),
        ([[5,5,5],[5,5,5],[5,5,5]], 10, 1),
        ([[5,5,5],[5,5,5],[5,5,5]], 20, 2),
        ([[5,5,5],[5,5,5],[5,5,5]], 45, 3),
        ([[5,5,5],[5,5,5],[5,5,5]], 46, 3),
        ([[1,1],[1,1]], 5, 2)
    ]
    correct_count = 0
    for i, (mat, threshold, expected) in enumerate(test_cases):
        result = max_side_length(mat, threshold)
        if result == expected:
            print(f'Test {i+1}: True')
            correct_count += 1
        else:
            print(f'Test {i+1}: False, Input: mat={mat}, threshold={threshold}, Expected: {expected}, Got: {result}')
    print(f'{correct_count}/{len(test_cases)}')

if __name__ == '__main__':
    test_max_side_length()