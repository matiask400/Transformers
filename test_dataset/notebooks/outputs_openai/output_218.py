import heapq

def skyline_test():
    def get_skyline(buildings):
        # Create events: (x, height, is_start)
        events = []
        for left, right, height in buildings:
            events.append((left, -height, True))  # start event
            events.append((right, height, False))  # end event
        # Sort events. If x is the same, start events come before end events
        events.sort(key=lambda x: (x[0], x[1]))
        
        result = []
        heap = [0]  # Max-heap (as min-heap with negative heights)
        active = {}
        prev = 0
        
        for x, h, is_start in events:
            if is_start:
                heapq.heappush(heap, h)
                active[h] = active.get(h, 0) + 1
            else:
                active[-h] -= 1
                if active[-h] == 0:
                    del active[-h]
            # Clean the heap
            while heap and (-heap[0] not in active):
                heapq.heappop(heap)
            current = -heap[0] if heap else 0
            if current != prev:
                result.append([x, current])
                prev = current
        return result

    test_cases = [
        {
            "buildings": [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]],
            "expected": [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
        },
        {
            "buildings": [[0,2,3],[2,5,3]],
            "expected": [[0,3],[5,0]]
        },
        {
            "buildings": [[1,3,3],[2,4,4],[5,6,1]],
            "expected": [[1,3],[2,4],[4,0],[5,1],[6,0]]
        },
        {
            "buildings": [[0,5,3],[2,7,3],[4,9,3]],
            "expected": [[0,3],[9,0]]
        },
        {
            "buildings": [[0,2,3],[2,5,3],[5,7,3]],
            "expected": [[0,3],[7,0]]
        },
        {
            "buildings": [[1,2,1]],
            "expected": [[1,1],[2,0]]
        },
        {
            "buildings": [[0,2147483647,2147483647]],
            "expected": [[0,2147483647],[2147483647,0]]
        }
    ]

    correct = 0
    total = len(test_cases)
    for i, test in enumerate(test_cases):
        output = get_skyline(test["buildings"])
        is_correct = output == test["expected"]
        print(is_correct)
        if is_correct:
            correct += 1
    print(f"{correct}/{total}")

skyline_test()