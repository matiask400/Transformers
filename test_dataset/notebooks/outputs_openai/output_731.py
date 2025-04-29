class MyCalendarTwo:
    def __init__(self):
        self.bookings = []
        self.overlaps = []
    
    def book(self, start, end):
        for o_start, o_end in self.overlaps:
            if start < o_end and end > o_start:
                return False
        for b_start, b_end in self.bookings:
            if start < b_end and end > b_start:
                self.overlaps.append((max(start, b_start), min(end, b_end)))
        self.bookings.append((start, end))
        return True

def run_tests():
    commands = ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
    arguments = [[], [10,20], [50,60], [10,40], [5,15], [5,10], [25,55]]
    expected = [None, True, True, True, False, True, True]
    
    obj = None
    correct = 0
    total = len(commands)
    
    for cmd, arg, exp in zip(commands, arguments, expected):
        if cmd == "MyCalendarTwo":
            obj = MyCalendarTwo()
            result = None
        elif cmd == "book":
            result = obj.book(*arg)
        else:
            result = None
        if result == exp:
            print(True)
            correct +=1
        else:
            print(False)
    print(f"{correct}/{total}")

run_tests()