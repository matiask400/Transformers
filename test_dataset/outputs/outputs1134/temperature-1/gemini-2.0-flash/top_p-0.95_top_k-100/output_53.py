class RangeModule:
    def __init__(self):
        self.ranges = []

    def addRange(self, left, right):
        new_ranges = []
        i = 0
        while i < len(self.ranges) and self.ranges[i][1] < left:
            new_ranges.append(self.ranges[i])
            i += 1
        
        interval = [left, right]
        while i < len(self.ranges) and self.ranges[i][0] <= right:
            interval[0] = min(interval[0], self.ranges[i][0])
            interval[1] = max(interval[1], self.ranges[i][1])
            i += 1
        new_ranges.append(interval)

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
            else:
                if start < left:
                    new_ranges.append([start, left])
                if end > right:
                    new_ranges.append([right, end])
        self.ranges = new_ranges

def test_range_module():
    range_module = RangeModule()
    
    # Test case 1
    range_module.addRange(10, 20)
    range_module.removeRange(14, 16)
    result1 = range_module.queryRange(10, 14)
    expected1 = True
    print(result1 == expected1)
    result2 = range_module.queryRange(13, 15)
    expected2 = False
    print(result2 == expected2)
    result3 = range_module.queryRange(16, 17)
    expected3 = True
    print(result3 == expected3)

    # Test case 2
    range_module = RangeModule()
    range_module.addRange(10, 180)
    range_module.addRange(150, 200)
    range_module.addRange(250, 500)
    result4 = range_module.queryRange(50, 100)
    expected4 = False
    print(result4 == expected4)
    result5 = range_module.queryRange(10, 20)
    expected5 = True
    print(result5 == expected5)
    result6 = range_module.queryRange(50, 100)
    expected6 = False
    print(result6 == expected6)
    range_module.removeRange(50, 150)
    result7 = range_module.queryRange(50, 100)
    expected7 = False
    print(result7 == expected7)
    result8 = range_module.queryRange(10, 20)
    expected8 = False
    print(result8 == expected8)
    
    #test case 3
    range_module = RangeModule()
    range_module.addRange(1,2)
    range_module.removeRange(1,2)
    result9 = range_module.queryRange(1,2)
    expected9 = False
    print(result9 == expected9)

    correct_count = sum([
        result1 == expected1,
        result2 == expected2,
        result3 == expected3,
        result4 == expected4,
        result5 == expected5,
        result6 == expected6,
        result7 == expected7,
        result8 == expected8,
        result9 == expected9
    ])
    
    print(f"{correct_count}/9")
    
test_range_module()