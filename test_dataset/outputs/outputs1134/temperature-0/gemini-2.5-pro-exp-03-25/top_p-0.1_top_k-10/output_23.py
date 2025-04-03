import collections
import sys

# Set higher recursion depth for potentially deep checks in complex scenarios, though unlikely needed for this approach.
# sys.setrecursionlimit(2000)

class MyCalendarTwo:
    """
    Implements a calendar that allows booking events, preventing triple bookings.
    Double bookings are permitted. Uses the boundary counting (sweep line) technique.
    """
    def __init__(self):
        """
        Initializes the calendar.
        'delta' stores the change in the number of active events at specific time points.
        A positive value at time 't' means events start, negative means events end.
        """
        # Using collections.Counter is convenient as it handles zero counts naturally.
        # Keys are time points, values are the net change (+1 for start, -1 for end).
        self.delta = collections.Counter()

    def book(self, start: int, end: int) -> bool:
        """
        Attempts to book an event in the half-open interval [start, end).

        Args:
            start: The start time of the event (inclusive).
            end: The end time of the event (exclusive).

        Returns:
            True if the event can be booked without causing a triple booking,
            False otherwise. If False, the event is not added to the calendar.
        """
        # 1. Tentatively apply the changes for the new interval.
        # Increment count at the start time.
        self.delta[start] += 1
        # Decrement count at the end time.
        self.delta[end] -= 1

        # 2. Check if this booking causes a triple overlap.
        # Iterate through the timeline points in chronological order.
        active_bookings = 0
        sorted_times = sorted(self.delta.keys())

        for time in sorted_times:
            # Update the number of active bookings at this time point.
            active_bookings += self.delta[time]

            # If at any point, the number of active bookings reaches 3 or more,
            # it means adding the current event [start, end) resulted in a
            # triple booking.
            # Note: We check >= 3 because the 'active_bookings' count *includes*
            # the event we just tentatively added.
            # Also, we only need to check *after* processing the delta at 'time'.
            # The count 'active_bookings' represents the number of active events
            # in the interval starting *at* 'time' up to the next time point.
            if active_bookings >= 3:
                # 3. Triple booking detected: Rollback the changes and return False.
                self.delta[start] -= 1
                self.delta[end] += 1

                # Optional cleanup: If counts become zero, remove the keys.
                # This keeps the delta map slightly smaller but isn't strictly
                # necessary for correctness with Counter.
                if self.delta[start] == 0:
                    del self.delta[start]
                if self.delta[end] == 0:
                    del self.delta[end]

                return False

        # 4. No triple booking found: The booking is successful.
        # The tentative changes are kept.
        return True

# --- Test Harness ---

def run_tests(test_cases):
    """
    Runs a series of test cases against the MyCalendarTwo implementation.

    Args:
        test_cases: A list of dictionaries, where each dictionary represents
                    a test sequence with "commands", "args", and "expected" outputs.
    """
    correct_count = 0
    total_tests = 0 # Counts only the 'book' calls that have an expected boolean output

    for i, case in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        commands = case["commands"]
        args = case["args"]
        expected = case["expected"]

        obj = None
        results = []
        case_passed = True

        for j in range(len(commands)):
            command = commands[j]
            arg = args[j]
            exp = expected[j]

            if command == "MyCalendarTwo":
                obj = MyCalendarTwo()
                results.append(None)
                print(f"Test {j}: MyCalendarTwo() -> Initialized")
            elif command == "book":
                total_tests += 1
                if obj is None:
                     print(f"Test {j}: Error - 'book' called before constructor.")
                     results.append("Error")
                     passed = False
                else:
                    res = obj.book(arg[0], arg[1])
                    results.append(res)
                    passed = (res == exp)
                    print(f"Test {j}: book({arg[0]}, {arg[1]}) -> Expected: {exp}, Got: {res} -> {passed}")

                if not passed:
                    case_passed = False
                if passed:
                    correct_count +=1
            else:
                 print(f"Unknown command: {command}")
                 results.append("Unknown command")


    print(f"\n--- Summary ---")
    print(f"Result: {correct_count} / {total_tests} tests passed.")

# --- Test Cases ---

test_cases = [
    # Example 1 from description
    {
        "commands": ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"],
        "args": [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
        "expected": [None, True, True, True, False, True, True]
    },
    # Test case with exact same interval booked three times
    {
        "commands": ["MyCalendarTwo", "book", "book", "book"],
        "args": [[], [10, 20], [10, 20], [10, 20]],
        "expected": [None, True, True, False]
    },
    # Test case with overlapping intervals leading to triple booking
    {
        "commands": ["MyCalendarTwo", "book", "book", "book", "book"],
        "args": [[], [0, 10], [5, 15], [10, 20], [12, 17]],
        "expected": [None, True, True, True, False] # [12, 15) would be triple booked by [5,15), [10,20), [12,17)
    },
    # Test case with contained intervals
    {
        "commands": ["MyCalendarTwo", "book", "book", "book", "book"],
        "args": [[], [10, 30], [5, 20], [15, 25], [18, 22]],
        # [10, 30] -> ok
        # [5, 20] -> ok, double book [10, 20)
        # [15, 25] -> ok, double book [15, 20) with [5,20], double book [20, 25) with [10, 30]
        # At this point:
        # [5, 10) single ([5,20])
        # [10, 15) double ([10,30], [5,20])
        # [15, 20) double ([10,30], [5,20], [15,25]) -> Wait, this looks like triple already? Let's retrace.
        # After book(10, 30): {[10, 30)}
        # After book(5, 20): {[10, 30), [5, 20)}. Overlap: [10, 20) is double.
        # After book(15, 25): Check [15, 25).
        #   Overlap with [10, 30) -> [15, 25)
        #   Overlap with [5, 20) -> [15, 20)
        #   Check existing double overlaps: [10, 20). Does [15, 25) overlap with [10, 20)? Yes, at [15, 20).
        #   So, adding [15, 25) would make [15, 20) triple booked.
        #   Therefore, book(15, 25) should return False.
        # Let's re-run the logic with the boundary counter:
        # book(10, 30): delta={10: 1, 30: -1}. Max active = 1. Returns True.
        # book(5, 20): delta={5: 1, 10: 1, 20: -1, 30: -1}.
        #   Check: delta={5: 1, 10: 1, 20: -1, 30: -1}. Add {5:1, 20:-1} -> {5:2, 10:1, 20:-2, 30:-1} NO, add first: {5:1, 10:1, 20:-1, 30:-1}
        #   Tentative: delta={5: 1, 10: 1, 20: -1, 30: -1}. Add {5:1, 20:-1} -> {5: 1+1=2, 10: 1, 20: -1-1=-2, 30: -1}
        #   Sweep: t=5, active=2. t=10, active=2+1=3. t=20, active=3-2=1. t=30, active=1-1=0. Max active = 3.
        #   Wait, the sweep line logic:
        #   book(10, 30): delta={10: 1, 30: -1}. Sweep: t=10, active=1. t=30, active=0. Max=1. OK. Return True.
        #   book(5, 20): Tentative delta={5: 1, 10: 1, 20: -1, 30: -1}. Add {5:1, 20:-1} -> {5: 1, 10: 1, 20: -1} + {5:1, 20:-1} = {5:1, 10:1, 20:-1, 30:-1} + {5:1, 20:-1} = {5:1+1=2, 10:1, 20:-1-1=-2, 30:-1} NO, add to existing delta:
        #   Current delta: {10: 1, 30: -1}
        #   Tentative add [5, 20): delta[5]+=1, delta[20]-=1 -> {5: 1, 10: 1, 20: -1, 30: -1}
        #   Sweep: t=5, active=1. t=10, active=1+1=2. t=20, active=2-1=1. t=30, active=1-1=0. Max=2. OK. Return True. Keep delta={5: 1, 10: 1, 20: -1, 30: -1}.
        #   book(15, 25): Current delta={5: 1, 10: 1, 20: -1, 30: -1}.
        #   Tentative add [15, 25): delta[15]+=1, delta[25]-=1 -> {5: 1, 10: 1, 15: 1, 20: -1, 25: -1, 30: -1}
        #   Sweep: t=5, active=1. t=10, active=1+1=2. t=15, active=2+1=3. t=20, active=3-1=2. t=25, active=2-1=1. t=30, active=1-1=0. Max=3.
        #   Triple booking detected at t=15. Rollback: delta[15]-=1, delta[25]+=1. Remove if 0. -> {5: 1, 10: 1, 20: -1, 30: -1}. Return False.
        #   book(18, 22): Current delta={5: 1, 10: 1, 20: -1, 30: -1}.
        #   Tentative add [18, 22): delta[18]+=1, delta[22]-=1 -> {5: 1, 10: 1, 18: 1, 20: -1, 22: -1, 30: -1}
        #   Sweep: t=5, active=1. t=10, active=1+1=2. t=18, active=2+1=3. t=20, active=3-1=2. t=22, active=2-1=1. t=30, active=1-1=0. Max=3.
        #   Triple booking detected at t=18. Rollback. Return False.
        #   My manual trace was wrong initially. The boundary counter seems correct.
        "expected": [None, True, True, False, False]
    },
     # Another contained intervals test
    {
        "commands": ["MyCalendarTwo", "book", "book", "book", "book", "book"],
        "args": [[], [1, 10], [2, 8], [3, 6], [4, 5]],
        # book(1, 10): delta={1:1, 10:-1}. Max=1. True.
        # book(2, 8): delta={1:1, 2:1, 8:-1, 10:-1}. Tentative={1:1, 2:1+1=2, 8:-1, 10:-1}. Sweep: t=1, a=1. t=2, a=1+1=2. t=8, a=2-1=1. t=10, a=1-1=0. Max=2. True. Keep delta={1:1, 2:1, 8:-1, 10:-1}.
        # book(3, 6): delta={1:1, 2:1, 8:-1, 10:-1}. Tentative={1:1, 2:1, 3:1, 6:-1, 8:-1, 10:-1}. Sweep: t=1, a=1. t=2, a=1+1=2. t=3, a=2+1=3. t=6, a=3-1=2. t=8, a=2-1=1. t=10, a=1-1=0. Max=3. False. Rollback. Keep delta={1:1, 2:1, 8:-1, 10:-1}.
        # book(4, 5): delta={1:1, 2:1, 8:-1, 10:-1}. Tentative={1:1, 2:1, 4:1, 5:-1, 8:-1, 10:-1}. Sweep: t=1, a=1. t=2, a=1+1=2. t=4, a=2+1=3. t=5, a=3-1=2. t=8, a=2-1=1. t=10, a=1-1=0. Max=3. False. Rollback. Keep delta={1:1, 2:1, 8:-1, 10:-1}.
        # Wait, the example says book(4,5) should be True. Let's re-read the example explanation.
        # Example 1: book(5, 15) -> False. Events: [10,20), [50,60), [10,40). Interval [10, 20) is double booked. Adding [5, 15) makes [10, 15) triple booked. Correct.
        # Example 1: book(5, 10) -> True. Events: [10,20), [50,60), [10,40). Interval [10, 20) is double booked. Adding [5, 10) makes [10, 10) empty intersection, so no triple booking. Correct.
        # Example 1: book(25, 55) -> True. Events: [10,20), [50,60), [10,40), [5,10).
        #   Double bookings: [10, 20) from [10,20)&[10,40).
        #   Add [25, 55). Check overlaps with double bookings: [10, 20). Intersection is empty. So, should be True.
        #   Let's trace book(25, 55) with boundary counter:
        #   Delta before: {5:1, 10:1+1-1=1, 20:-1, 40:-1, 50:1, 60:-1} -> {5:1, 10:1, 20:-1, 40:-1, 50:1, 60:-1}
        #   Tentative add [25, 55): delta[25]+=1, delta[55]-=1 -> {5:1, 10:1, 20:-1, 25:1, 40:-1, 50:1, 55:-1, 60:-1}
        #   Sweep: t=5, a=1. t=10, a=1+1=2. t=20, a=2-1=1. t=25, a=1+1=2. t=40, a=2-1=1. t=50, a=1+1=2. t=55, a=2-1=1. t=60, a=1-1=0. Max=2. True. Correct.
        #
        # Now back to the contained intervals test case:
        # ["MyCalendarTwo", "book", "book", "book", "book"]
        # ["args": [[], [1, 10], [2, 8], [3, 6], [4, 5]]
        # book(1, 10): True. delta={1:1, 10:-1}
        # book(2, 8): True. delta={1:1, 2:1, 8:-1, 10:-1}
        # book(3, 6): False. Max active becomes 3 at t=3. delta remains {1:1, 2:1, 8:-1, 10:-1}
        # book(4, 5): Tentative add [4, 5). delta={1:1, 2:1, 4:1, 5:-1, 8:-1, 10:-1}.
        #   Sweep: t=1, a=1. t=2, a=1+1=2. t=4, a=2+1=3. t=5, a=3-1=2. t=8, a=2-1=1. t=10, a=1-1=0. Max=3. False.
        # It seems my trace consistently gives False for book(4,5), while the comment in the test case definition expected True. Let's assume my trace is correct based on the algorithm.
        "expected": [None, True, True, False, False]
    },
    # Edge case: Zero length interval (should technically