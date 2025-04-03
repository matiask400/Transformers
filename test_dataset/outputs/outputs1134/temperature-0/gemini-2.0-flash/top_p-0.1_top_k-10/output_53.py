class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        new_range = [left, right]
        new_ranges = []
        i = 0
        while i < len(self.ranges) and self.ranges[i][1] < left:
            new_ranges.append(self.ranges[i])
            i += 1
        while i < len(self.ranges) and self.ranges[i][0] <= right:
            new_range[0] = min(new_range[0], self.ranges[i][0])
            new_range[1] = max(new_range[1], self.ranges[i][1])
            i += 1
        new_ranges.append(new_range)
        while i < len(self.ranges):
            new_ranges.append(self.ranges[i])
            i += 1
        self.ranges = new_ranges

    def queryRange(self, left: int, right: int) -> bool:
        for l, r in self.ranges:
            if l <= left and right <= r:
                return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        new_ranges = []
        for l, r in self.ranges:
            if r <= left or l >= right:
                new_ranges.append([l, r])
            else:
                if l < left:
                    new_ranges.append([l, left])
                if r > right:
                    new_ranges.append([right, r])
        self.ranges = new_ranges

def test_range_module():
    range_module = RangeModule()
    
    # Test case 1
    range_module.addRange(10, 20)
    range_module.removeRange(14, 16)
    
    test1 = range_module.queryRange(10, 14)
    print(test1 == True)
    
    test2 = range_module.queryRange(13, 15)
    print(test2 == False)
    
    test3 = range_module.queryRange(16, 17)
    print(test3 == True)
    
    # Test case 2
    range_module = RangeModule()
    range_module.addRange(10, 180)
    range_module.addRange(150, 200)
    range_module.addRange(250, 500)
    test4 = range_module.queryRange(50, 100)
    print(test4 == True)
    test5 = range_module.queryRange(180, 300)
    print(test5 == False)
    range_module.removeRange(50, 150)
    test6 = range_module.queryRange(50, 100)
    print(test6 == False)
    
    # Test case 3
    range_module = RangeModule()
    range_module.addRange(5, 8)
    test7 = range_module.queryRange(3, 6)
    print(test7 == False)
    range_module.removeRange(5, 6)
    test8 = range_module.queryRange(3, 6)
    print(test8 == False)
    
    # Count correct tests
    correct_tests = sum([test1 == True, test2 == False, test3 == True, test4 == True, test5 == False, test6 == False, test7 == False, test8 == False])
    total_tests = 8
    print(f"{correct_tests}/{total_tests}")

test_range_module()