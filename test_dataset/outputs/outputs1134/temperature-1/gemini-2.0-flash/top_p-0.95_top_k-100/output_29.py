import heapq

def getSkyline(buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """

    events = []
    for l, r, h in buildings:
        events.append((l, -h, r))  # Use negative height for start points
        events.append((r, 0, 0))   # Use 0 height for end points

    events.sort()

    skyline = []
    heap = [(0, float('inf'))]  # Max heap, (height, right)
    current_height = 0
    active_buildings = {}

    for x, h, r in events:
        # Remove expired buildings from heap
        while heap and heap[0][1] <= x:
            heapq.heappop(heap)

        if h < 0:  # Start of a building
            heapq.heappush(heap, (h, r))
        
        max_height = -heap[0][0]

        if max_height != current_height:
            current_height = max_height
            skyline.append([x, current_height])

    return skyline

def test_skyline():
    test_cases = [
        {
            "input": [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]],
            "expected": [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
        },
        {
            "input": [[0,2,3],[2,5,3]],
            "expected": [[0,3],[5,0]]
        },
        {
            "input": [[1,2,1],[1,2,2],[1,2,3]],
            "expected": [[1,3],[2,0]]
        },
        {
            "input": [[1,5,3],[1,5,3]],
            "expected": [[1,3],[5,0]]
        },
        {
            "input": [[1,3,4],[3,4,4],[2,6,2],[8,11,4],[7,9,3],[10,11,2]],
            "expected": [[1,4],[3,2],[6,0],[7,3],[9,4],[11,0]]
        },
        {
            "input": [],
            "expected": []
        },
        {
            "input": [[0, 31, 9], [1, 5, 8], [3, 31, 7], [7, 10, 6], [8, 12, 4], [11, 29, 3], [13, 21, 2], [14, 15, 10]],
            "expected": [[0, 9], [1, 8], [3, 7], [7, 6], [8, 4], [11, 3], [14, 10], [15, 3], [21, 2], [29, 3], [31, 0]]
        }
    ]

    num_correct = 0
    for i, test in enumerate(test_cases):
        buildings = test["input"]
        expected = test["expected"]
        result = getSkyline(buildings)
        if result == expected:
            print(f"True")
            num_correct += 1
        else:
            print(f"False")
            print(f"Test case {i+1} failed: Expected {expected}, got {result}")

    print(f"{num_correct}/{len(test_cases)}")

test_skyline()