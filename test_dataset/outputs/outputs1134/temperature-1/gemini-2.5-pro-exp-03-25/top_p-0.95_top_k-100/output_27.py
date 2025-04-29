import sys
# Setting a reasonable recursion depth, although unlikely to be needed for typical sorting
# sys.setrecursionlimit(2000) 

def solve():
    """
    Solves the Non-overlapping Intervals problem.
    Finds the minimum number of intervals to remove to make the rest non-overlapping.
    Implements the solution function and runs tests against expected outputs.
    """

    def eraseOverlapIntervals(intervals):
        """
        Given a collection of intervals, find the minimum number of intervals 
        you need to remove to make the rest of the intervals non-overlapping.

        Args:
            intervals: A list of lists, where each inner list represents an interval [start, end].

        Returns:
            The minimum number of intervals to remove.
        """
        if not intervals:
            return 0

        # Sort intervals based on their end times.
        # This greedy approach works because choosing the interval that finishes earliest
        # leaves the maximum room for subsequent intervals.
        intervals.sort(key=lambda x: x[1])

        # Initialize count of non-overlapping intervals kept
        count_kept = 1 
        # The end time of the last interval kept
        last_kept_end = intervals[0][1] 

        # Iterate through the sorted intervals starting from the second one
        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            current_start = current_interval[0]

            # If the current interval's start time is greater than or equal to
            # the end time of the last kept interval, it doesn't overlap.
            if current_start >= last_kept_end:
                # Keep this interval
                count_kept += 1
                # Update the end time for the next comparison
                last_kept_end = current_interval[1]
            # Else (current_start < last_kept_end), the current interval overlaps
            # with the last kept interval. Since we sorted by end times, the
            # current interval ends no earlier than the last kept one.
            # By *not* keeping the current interval and *not* updating last_kept_end,
            # we effectively discard the current interval in favor of the one
            # that finished earlier, maximizing the potential to fit more intervals.

        # The minimum number of removals is the total number of intervals
        # minus the maximum number of non-overlapping intervals we could keep.
        total_intervals = len(intervals)
        min_removed = total_intervals - count_kept
        
        return min_removed

    # --- Test Cases ---
    tests = [
        # Example 1
        {"input": [[1,2],[2,3],[3,4],[1,3]], "expected": 1},
        # Example 2
        {"input": [[1,2],[1,2],[1,2]], "expected": 2},
        # Example 3
        {"input": [[1,2],[2,3]], "expected": 0},
        # Additional Tests
        {"input": [], "expected": 0}, # Empty list
        {"input": [[1,5]], "expected": 0}, # Single interval
        {"input": [[1,100],[11,22],[1,11],[2,12]], "expected": 2}, # Test case from thought process
        # Explanation: Sort by end: [[1,11], [2,12], [11,22], [1,100]]
        # Keep [1,11], end=11
        # Skip [2,12] (2 < 11)
        # Keep [11,22], end=22
        # Skip [1,100] (1 < 22)
        # Kept 2: [1,11], [11,22]. Total 4. Removed 4-2=2.
        {"input": [[0,2],[1,3],[2,4],[3,5],[4,6]], "expected": 2},
        # Explanation: Sort by end: [[0,2], [1,3], [2,4], [3,5], [4,6]]
        # Keep [0,2], end=2
        # Skip [1,3] (1 < 2)
        # Keep [2,4], end=4
        # Skip [3,5] (3 < 4)
        # Keep [4,6], end=6
        # Kept 3: [0,2], [2,4], [4,6]. Total 5. Removed 5-3=2.
         {"input": [[1,3],[2,4],[3,5],[4,6]], "expected": 2},
        # Explanation: Sort by end: [[1,3], [2,4], [3,5], [4,6]]
        # Keep [1,3], end=3
        # Skip [2,4] (2 < 3)
        # Keep [3,5], end=5
        # Skip [4,6] (4 < 5)
        # Kept 2: [1,3], [3,5]. Total 4. Removed 4-2=2.
    ]

    correct_count = 0
    total_tests = len(tests)

    for i, test in enumerate(tests):
        # The function sorts the input list in place. 
        # If preserving the original order in the test dictionary is important 
        # for inspection *after* the run, make a copy. Otherwise, it's fine.
        # input_copy = [list(interval) for interval in test["input"]] # Use if needed
        
        result = eraseOverlapIntervals(test["input"]) # Pass the original or copy
        expected = test["expected"]
        
        is_correct = (result == expected)
        print(f"Test {i + 1}: {is_correct}")
        if is_correct:
            correct_count += 1

    print(f"{correct_count}/{total_tests} tests passed.")

# Execute the solve function
solve()