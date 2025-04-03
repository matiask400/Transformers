import heapq

def getSkyline(buildings):
    events = []
    for l, r, h in buildings:
        events.append((l, -h, r))  # start event, negate height for max heap
        events.append((r, 0, r))   # end event, height 0

    events.sort(key=lambda x: (x[0], x[1])) # Sort by x, then height (start before end, higher start first)

    skyline = []
    heap = [0]  # Max heap to store current heights, initialized with ground level
    max_height = 0

    for x, neg_h, r in events:
        while heap and heap[0] <= x: # Remove buildings that end before current x
            heapq.heappop(heap)

        if neg_h < 0: # Start event
            heapq.heappush(heap, -neg_h)
        # else: End event, handled in while loop above

        current_height = -heap[0] # Get max height

        if current_height != max_height:
            skyline.append([x, current_height])
            max_height = current_height

    res = []
    if not skyline:
        return res

    res.append(skyline[0])
    for i in range(1, len(skyline)):
        if res[-1][1] != skyline[i][1]:
            res.append(skyline[i])

    return res

def test_skyline():
    test_cases = [
        ([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]], [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]),
        ([[0,2,3],[2,5,3]], [[0,3],[5,0]]),
        ([[1,2,1],[1,2,2],[1,2,3]], [[1,3],[2,0]]),
        ([[1,3,4],[3,4,4],[1,4,5]], [[1,5],[4,0]]),
        ([[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[0,5,12],[0,20,12],[15,20,12],[0,10,12]], [[0,12],[20,0]]),
        ([], []),
        ([[0, 1, 1]], [[0, 1], [1, 0]]),
        ([[0, 1, 1], [2, 3, 2]], [[0, 1], [1, 0], [2, 2], [3, 0]]),
        ([[0, 1, 1], [0, 2, 2]], [[0, 2], [2, 0]])
    ]

    correct_count = 0
    for i, (buildings, expected_skyline) in enumerate(test_cases):
        result_skyline = getSkyline(buildings)
        if result_skyline == expected_skyline:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: {buildings}")
            print(f"  Expected: {expected_skyline}")
            print(f"  Result: {result_skyline}")

    print(f"\n{correct_count} correct out of {len(test_cases)}")

test_skyline()