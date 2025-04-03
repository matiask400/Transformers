import heapq

def getSkyline(buildings):
    events = []
    for l, r, h in buildings:
        events.append((l, -h)) # start event, negative height
        events.append((r, h))  # end event, positive height

    events.sort(key=lambda x: (x[0], x[1])) # sort by x, then by height (start before end)

    skyline = []
    height_heap = [0] # initialize with 0 to handle ground level
    last_max_height = 0

    for x, height in events:
        if height < 0: # start event
            heapq.heappush(height_heap, height)
        else: # end event
            height_heap.remove(-height)
            heapq.heapify(height_heap)

        current_max_height = -height_heap[0]
        if current_max_height != last_max_height:
            skyline.append([x, current_max_height])
            last_max_height = current_max_height

    return skyline

def test_skyline():
    test_cases = [
        {
            "buildings": [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]],
            "expected_output": [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
        },
        {
            "buildings": [[0,2,3],[2,5,3]],
            "expected_output": [[0,3],[5,0]]
        },
        {
            "buildings": [[1,2,1],[1,2,2],[1,2,3]],
            "expected_output": [[1,3],[2,0]]
        },
        {
            "buildings": [[1,5,1],[2,3,2]],
            "expected_output": [[1,1],[2,2],[3,1],[5,0]]
        },
        {
            "buildings": [[0,1,3],[0,2,3],[0,3,3]],
            "expected_output": [[0,3],[3,0]]
        },
        {
            "buildings": [[1,3,4],[3,4,4],[2,4,3],[1,4,2]],
            "expected_output": [[1,4],[4,0]]
        }
    ]

    num_tests = len(test_cases)
    correct_tests = 0

    for i, case in enumerate(test_cases):
        buildings = case["buildings"]
        expected