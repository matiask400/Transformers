def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = intervals[0][1]
    for interval in intervals[1:]:
        if interval[0] < end:
            count +=1
        else:
            end = interval[1]
    return count

def run_tests():
    test_cases = [
        ([[1,2],[2,3],[3,4],[1,3]], 1),
        ([[1,2],[1,2],[1,2]], 2),
        ([[1,2],[2,3]], 0),
    ]
    correct = 0
    for i, (inp, expected) in enumerate(test_cases):
        result = eraseOverlapIntervals(inp)
        is_correct = result == expected
        print(is_correct)
        if is_correct:
            correct +=1
    print(f"{correct}/{len(test_cases)}")

run_tests()