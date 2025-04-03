def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: (x[1], x[0]))
    removed_count = 0
    last_end_time = float('-inf')
    for interval in intervals:
        start, end = interval
        if start >= last_end_time:
            last_end_time = end
        else:
            removed_count += 1
    return removed_count

def run_tests():
    test_cases = [
        ([[1,2],[2,3],[3,4],[1,3]], 1),
        ([[1,2],[1,2],[1,2]], 2),
        ([[1,2],[2,3]], 0),
        ([], 0),
        ([[1,10],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9]], 1)
    ]
    correct_tests = 0
    for i, (input_intervals, expected_output) in enumerate(test_cases):
        output = eraseOverlapIntervals(input_intervals)
        if output == expected_output:
            print(f'Test {i+1}: True')
            correct_tests += 1
        else:
            print(f'Test {i+1}: False')
    print(f'{correct_tests}/{len(test_cases)}')

if __name__ == '__main__':
    run_tests()