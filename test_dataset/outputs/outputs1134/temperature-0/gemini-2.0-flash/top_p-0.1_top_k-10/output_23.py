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
    cal = MyCalendarTwo()
    
    test_cases = [
        ((10, 20), True),
        ((50, 60), True),
        ((10, 40), True),
        ((5, 15), False),
        ((5, 10), True),
        ((25, 55), True),
    ]
    
    results = []
    for event, expected in test_cases:
        result = cal.book(*event)
        results.append(result == expected)
        print(result == expected)
    
    print(f"{sum(results)}/{len(results)}")

if __name__ == "__main__":
    test_my_calendar_two()