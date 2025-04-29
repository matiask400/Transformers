class MyCalendarTwo:
    def __init__(self):
        self.booked = []
        self.double_booked = []

    def book(self, start: int, end: int) -> bool:
        for db_start, db_end in self.double_booked:
            intersection_start = max(db_start, start)
            intersection_end = min(db_end, end)
            if intersection_start < intersection_end:
                return False

        current_double_booked = []
        for b_start, b_end in self.booked:
            intersection_start = max(b_start, start)
            intersection_end = min(b_end, end)
            if intersection_start < intersection_end:
                current_double_booked.append((intersection_start, intersection_end))

        self.double_booked.extend(current_double_booked)
        self.booked.append((start, end))
        return True

def run_tests():
    cal = MyCalendarTwo()
    test_cases = [
        ((10, 20), True),
        ((50, 60), True),
        ((10, 40), True),
        ((5, 15), False),
        ((5, 10), True),
        ((25, 55), True),
    ]
    correct_tests = 0
    for i, ((start, end), expected_output) in enumerate(test_cases):
        actual_output = cal.book(start, end)
        if actual_output == expected_output:
            print(f'Test {i+1}: True')
            correct_tests += 1
        else:
            print(f'Test {i+1}: False')
    print(f'{correct_tests}/{len(test_cases)}')

if __name__ == '__main__':
    run_tests()