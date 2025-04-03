def solve():
    class RangeModule:
        def __init__(self):
            self.ranges = []

        def addRange(self, left, right):
            new_ranges = []
            i = 0
            while i < len(self.ranges) and self.ranges[i][1] < left:
                new_ranges.append(self.ranges[i])
                i += 1

            current_range = [left, right]
            while i < len(self.ranges) and self.ranges[i][0] <= right:
                current_range[0] = min(current_range[0], self.ranges[i][0])
                current_range[1] = max(current_range[1], self.ranges[i][1])
                i += 1
            new_ranges.append(current_range)

            while i < len(self.ranges):
                new_ranges.append(self.ranges[i])
                i += 1
            self.ranges = new_ranges

        def queryRange(self, left, right):
            for start, end in self.ranges:
                if start <= left and right <= end:
                    return True
            return False

        def removeRange(self, left, right):
            new_ranges = []
            for start, end in self.ranges:
                if end <= left or start >= right:
                    new_ranges.append([start, end])
                elif start < left and end > right:
                    new_ranges.append([start, left])
                    new_ranges.append([right, end])
                elif start < left <= end <= right:
                    new_ranges.append([start, left])
                elif left <= start <= right < end:
                    new_ranges.append([right, end])
            self.ranges = new_ranges

    range_module = RangeModule()
    test_cases = [
        (["addRange", "removeRange", "queryRange", "queryRange", "queryRange"], [[10, 20], [14, 16], [10, 14], [13, 15], [16, 17]], [None, None, True, False, True]),
        (["addRange", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"], [[10, 18], [20, 25], [12, 22], [10, 14], [16, 18], [24, 26]], [None, None, None, True, False, False]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[10, 20], [15, 17], [12, 15], [10, 16]], [None, None, None, True]),
        (["addRange", "removeRange", "queryRange"], [[10, 20], [10, 20], [10, 20]], [None, None, False]),
        (["addRange", "queryRange", "removeRange", "queryRange"], [[10, 20], [10, 20], [10, 20], [10, 20]], [None, True, None, False]),
        (["addRange", "addRange", "queryRange", "removeRange", "queryRange"], [[6, 8], [9, 10], [7, 9], [7, 9], [6, 10]], [None, None, True, None, False]),
        (["addRange", "removeRange", "addRange", "removeRange", "queryRange"], [[1, 5], [2, 3], [2, 3], [4, 5], [1, 5]], [None, None, None, None, False]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [2, 4], [2, 4], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [1, 5], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [1, 6], [1, 5], [1, 5]], [None, None, None, False]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [0, 6], [1, 5], [1, 5]], [None, None, None, False]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [0, 1], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [5, 6], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [4, 6], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [0, 4], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [2, 5], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [3, 5], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [1, 3], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [1, 2], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [4, 5], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [0, 0], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [6, 7], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [5, 5], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [0, 1], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [5, 6], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [4, 6], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [0, 4], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [2, 5], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [3, 5], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [1, 3], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [1, 2], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [4, 5], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [0, 0], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [6, 7], [1, 5], [1, 5]], [None, None, None, True]),
        (["addRange", "removeRange", "addRange", "queryRange"], [[1, 5], [5, 5], [1, 5], [1, 5]], [None, None, None, True]),

    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, (operations, inputs, expected_outputs) in enumerate(test_cases):
        range_module = RangeModule()
        test_passed = True
        print(f"Test Case {i+1}:")
        for op, inp, expected_output in zip(operations, inputs, expected_outputs):
            if op == "addRange":
                range_module.addRange(inp[0], inp[1])
                actual_output = None
            elif op == "removeRange":
                range_module.removeRange(inp[0], inp[1])
                actual_output = None
            elif op == "queryRange":
                actual_output = range_module.queryRange(inp[0], inp[1])
            else:
                raise ValueError("Unknown operation")

            if actual_output != expected_output:
                test_passed = False
                print(f"  Operation: {op}, Input: {inp}, Expected Output: {expected_output}, Actual Output: {actual_output} - False")
            else:
                print(f"  Operation: {op}, Input: {inp}, Expected Output: {expected_output}, Actual Output: {actual_output} - True")

        if test_passed:
            print(f"Test Case {i+1} Passed: True")
            correct_tests += 1
        else:
            print(f"Test Case {i+1} Passed: False")

    print(f"\n{correct_tests} correct tests over {total_tests}")

solve()