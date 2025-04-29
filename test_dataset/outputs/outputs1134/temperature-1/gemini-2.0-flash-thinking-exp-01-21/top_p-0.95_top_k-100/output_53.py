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
                if start <= left and end >= right:
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

    def test_range_module():
        rm = RangeModule()
        test_cases = [
            (["addRange", 10, 20], None),
            (["removeRange", 14, 16], None),
            (["queryRange", 10, 14], True),
            (["queryRange", 13, 15], False),
            (["queryRange", 16, 17], True),
            (["removeRange", 11, 18], None),
            (["queryRange", 10, 20], False),
            (["queryRange", 10, 11], True),
            (["queryRange", 18, 20], True),
            (["queryRange", 11, 18], False),

             (["addRange", 6, 8], None),
             (["removeRange", 7, 8], None),
             (["removeRange", 8, 9], None),
             (["addRange", 8, 9], None),
             (["removeRange", 1, 3], None),
             (["addRange", 4, 6], None),
             (["removeRange", 3, 5], None),
             (["addRange", 1, 10], None),
             (["removeRange", 6, 10], None),
             (["queryRange", 1, 10], False),
             (["queryRange", 1, 6], True),
             (["queryRange", 6, 8], False),
             (["queryRange", 8, 10], False),

        ]

        results = []
        expected_outputs = [None, None, True, False, True, None, False, True, True, False, None, None, None, None, None, None, None, None, None, False, True, False, False]

        correct_count = 0
        for i in range(len(test_cases)):
            action = test_cases[i][0]
            params = test_cases[i][1:]

            output = None
            if action == "addRange":
                rm.addRange(params[0], params[1])
            elif action == "removeRange":
                rm.removeRange(params[0], params[1])
            elif action == "queryRange":
                output = rm.queryRange(params[0], params[1])

            expected_output = expected_outputs[i]

            if output == expected_output:
                print("True")
                correct_count += 1
            else:
                print("False")

        print(f"{correct_count}/{len(test_cases)}")

    test_range_module()

solve()