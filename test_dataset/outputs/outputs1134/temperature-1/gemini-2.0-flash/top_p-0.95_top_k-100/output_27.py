def erase_overlap_intervals(intervals):
    """
    Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

    Example 1:
    Input: [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.


    Example 2:
    Input: [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.


    Example 3:
    Input: [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

    Note:
    You may assume the interval's end point is always bigger than its start point.

    Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])  # Sort by end time
    
    count = 0
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]
            
    return count

def run_tests():
    tests = [
        ([[1,2],[2,3],[3,4],[1,3]], 1),
        ([[1,2],[1,2],[1,2]], 2),
        ([[1,2],[2,3]], 0),
        ([[1,100],[11,22],[1,11],[2,12]], 2),
        ([], 0),
        ([[1,2]], 0)
    ]

    correct_count = 0
    total_count = len(tests)

    for i, (intervals, expected) in enumerate(tests):
        result = erase_overlap_intervals(intervals)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    run_tests()