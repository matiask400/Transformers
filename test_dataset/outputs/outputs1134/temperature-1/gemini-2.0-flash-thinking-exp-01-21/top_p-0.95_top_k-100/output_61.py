def solve():
    def min_arrows_to_burst_balloons(points):
        if not points:
            return 0
        points.sort(key=lambda x: x[1])  # Sort by end x-coordinate
        arrow_count = 0
        current_arrow_pos = -float('inf')
        for start, end in points:
            if start > current_arrow_pos:
                arrow_count += 1
                current_arrow_pos = end
        return arrow_count

    def run_test(points, expected_output):
        output = min_arrows_to_burst_balloons(points)
        if output == expected_output:
            print('True')
        else:
            print('False')
        return output == expected_output

    test_cases = [
        ([[10,16],[2,8],[1,6],[7,12]], 2),
        ([[1,2],[3,4],[5,6],[7,8]], 4),
        ([[1,2],[2,3],[3,4],[4,5]], 2),
        ([], 0),
        ([[1,2]], 1),
        ([[1,3],[2,3]], 1),
        ([[1,3],[2,4]], 1),
        ([[1,3],[3,4]], 2),
    ]

    correct_count = 0
    for points, expected_output in test_cases:
        if run_test(points, expected_output):
            correct_count += 1

    print(f'{correct_count}/{len(test_cases)}')

    return min_arrows_to_burst_balloons

solve()