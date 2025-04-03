class RangeModule:
    def __init__(self):
        self.intervals = []
    
    def addRange(self, left: int, right: int) -> None:
        new = []
        placed = False
        for i in self.intervals:
            if i[1] < left:
                new.append(i)
            elif i[0] > right:
                if not placed:
                    new.append([left, right])
                    placed = True
                new.append(i)
            else:
                left = min(left, i[0])
                right = max(right, i[1])
        if not placed:
            new.append([left, right])
        self.intervals = new

    def queryRange(self, left: int, right: int) -> bool:
        import bisect
        idx = bisect.bisect_right(self.intervals, [left, float('inf')])
        if idx == 0:
            return False
        return self.intervals[idx-1][0] <= left and self.intervals[idx-1][1] >= right

    def removeRange(self, left: int, right: int) -> None:
        new = []
        for i in self.intervals:
            if i[1] <= left or i[0] >= right:
                new.append(i)
            else:
                if i[0] < left:
                    new.append([i[0], left])
                if i[1] > right:
                    new.append([right, i[1]])
        self.intervals = new

def run_tests():
    rm = RangeModule()
    tests = [
        ('addRange', 10, 20, None),
        ('removeRange', 14, 16, None),
        ('queryRange', 10, 14, True),
        ('queryRange', 13, 15, False),
        ('queryRange', 16, 17, True),
    ]
    expected_results = [None, None, True, False, True]
    total = len(tests)
    correct = 0
    for i, test in enumerate(tests):
        op, left, right, expected = test
        if op == 'addRange':
            rm.addRange(left, right)
            result = None
        elif op == 'removeRange':
            rm.removeRange(left, right)
            result = None
        elif op == 'queryRange':
            result = rm.queryRange(left, right)
        pass_test = (result == expected)
        print(pass_test)
        if pass_test:
            correct +=1
    print(f"{correct}/{total}")

run_tests()