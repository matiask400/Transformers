import sys

# Setting a reasonable recursion depth, although not strictly necessary for this iterative solution
# sys.setrecursionlimit(2000)

def solve(intervals):
    """
    Given a collection of intervals, find the minimum number of intervals
    you need to remove to make the rest of the intervals non-overlapping.

    Args:
        intervals: A list of lists, where each inner list represents an interval [start, end].

    Returns:
        The minimum number of intervals to remove.
    """
    # If there are no intervals or only one, no removals are needed.
    if not intervals:
        return 0

    # Sort the intervals based on their end points.
    # This greedy approach prioritizes keeping intervals that finish earlier,
    # as they leave more room for subsequent intervals.
    # The key=lambda x: x[1] tells sort to use the second element (end point) for comparison.
    intervals.sort(key=lambda x: x[1])

    n = len(intervals)
    # Initialize the count of non-overlapping intervals we can keep.
    # We always keep the first interval after sorting (the one that ends earliest).
    kept_count = 1
    # Keep track of the end point of the last interval kept.
    last_end = intervals[0][1]

    # Iterate through the rest of the intervals starting from the second one.
    for i in range(1, n):
        current_start = intervals[i][0]
        current_end = intervals[i][1]

        # If the current interval's start time is greater than or equal to
        # the end time of the last kept interval, it means they don't overlap.
        # Note: Intervals like [1,2] and [2,3] are considered non-overlapping.
        if current_start >= last_end:
            # We can keep this interval. Increment the count and update the last end time.
            kept_count += 1
            last_end = current_end
        # Else (if current_start < last_end), the current interval overlaps
        # with the last kept interval. Since we sorted by end times, the current
        # interval ends later than or at the same time as the last kept one.
        # The greedy choice is to discard the current interval because keeping
        # the one that finishes earlier (last_end) leaves more potential
        # room for future intervals. So, we do nothing and move to the next interval.

    # The minimum number of intervals to remove is the total number of intervals
    # minus the maximum number of non-overlapping intervals we could keep.
    removals = n - kept_count
    return removals

def run_tests():
    """
    Runs predefined test cases against the solve function and prints the results.
    """
    test_cases = [
        # Input intervals, Expected output (min removals)
        ([[1,2],[2,3],[3,4],[1,3]], 1),
        ([[1,2],[1,2],[1,2]], 2),
        ([[1,2],[2,3]], 0),
        ([], 0), # Edge case: empty list
        ([[1,100]], 0), # Edge case: single interval
        ([[1,5],[2,4],[3,6]], 1), # Sort: [2,4], [1,5], [3,6]. Keep [2,4]. Skip [1,5]. Keep [3,6]. Kept=2. Total=3. Remove=1.
        ([[0,2],[1,3],[2,4],[3,5],[4,6]], 2), # Sort: [0,2], [1,3], [2,4], [3,5], [4,6]. Keep [0,2]. Skip [1,3]. Keep [2,4]. Skip [3,5]. Keep [4,6]. Kept=3. Total=5. Remove=2.
        ([[7,9],[2,4],[5,8]], 0), # Sort: [2,4], [5,8], [7,9]. Keep [2,4]. Keep [5,8]. Skip [7,9]. Kept=2. Total=3. Remove=1. Let's recheck this one.
                                         # Sort by end: [2,4], [5,8], [7,9]
                                         # Keep [2,4]. last_end = 4. kept_count = 1.
                                         # Consider [5,8]. start=5 >= last_end=4. Keep. last_end = 8. kept_count = 2.
                                         # Consider [7,9]. start=7 < last_end=8. Skip.
                                         # Max kept = 2. Total = 3. Removals = 3 - 2 = 1. The expected output should be 1. Let's fix the test case.
        ([[7,9],[2,4],[5,8]], 1), # Corrected expected output
        ([[1,3],[3,5],[5,7]], 0), # Already non-overlapping
        ([[1,5],[1,5],[1,5]], 2), # Identical overlapping intervals
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, (intervals_input, expected_output) in enumerate(test_cases):
        # The solve function sorts the list in-place.
        # To ensure the original test case input isn't modified for potential re-use
        # or inspection, pass a copy. List comprehension creates a shallow copy,
        # which is sufficient here as the inner lists (intervals) are not modified.
        intervals_copy = [list(interval) for interval in intervals_input]
        result = solve(intervals_copy)
        passed = result == expected_output
        print(f"{passed}") # Print True or False for each test
        if passed:
            correct_tests += 1
        # Optional: Print details on failure
        # else:
        #     print(f"Test {i+1} Failed: Input={intervals_input}, Expected={expected_output}, Got={result}")


    print(f"\n{correct_tests}/{total_tests}") # Final summary

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()