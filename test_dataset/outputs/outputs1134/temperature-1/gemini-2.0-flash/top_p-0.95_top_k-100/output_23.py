class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlaps:
            if start < e and end > s:
                return False
        for s, e in self.calendar:
            if start < e and end > s:
                self.overlaps.append((max(start, s), min(end, e)))
        self.calendar.append((start, end))
        return True

def test_my_calendar_two():
    test_cases = [
        (
            [
                ["MyCalendarTwo", [], []],
                ["book", [10, 20], [True]],
                ["book", [50, 60], [True]],
                ["book", [10, 40], [True]],
                ["book", [5, 15], [False]],
                ["book", [5, 10], [True]],
                ["book", [25, 55], [True]]
            ],
            [True, True, True, False, True, True]
        ),
        (
            [
                ["MyCalendarTwo", [], []],
                ["book", [24, 40], [True]],
                ["book", [43, 50], [True]],
                ["book", [27, 43], [True]],
                ["book", [5, 21], [True]],
                ["book", [30, 40], [False]],
                ["book", [14, 29], [False]],
                ["book", [3, 19], [False]],
                ["book", [3, 14], [False]],
                ["book", [25, 39], [False]]
            ],
            [True, True, True, True, False, False, False, False, False]
        ),
    ]
    
    num_correct = 0
    total_tests = 0
    
    for test_case, expected_outputs in test_cases:
        obj = None
        results = []
        for i, operation in enumerate(test_case):
            method_name = operation[0]
            args = operation[1]
            
            if method_name == "MyCalendarTwo":
                obj = MyCalendarTwo()
                results.append(None)
            elif method_name == "book":
                result = obj.book(*args)
                results.append(result)
                
        actual_outputs = results[1:]  # Exclude the "MyCalendarTwo" call
        expected_outputs = expected_outputs
        
        for i in range(len(expected_outputs)):
            total_tests += 1
            if actual_outputs[i] == expected_outputs[i]:
                print("True")
                num_correct += 1
            else:
                print("False")

    print(f"{num_correct}/{total_tests}")

test_my_calendar_two()