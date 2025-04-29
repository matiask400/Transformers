import heapq

def getSkyline(buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    events = []
    for l, r, h in buildings:
        events.append((l, -h, r))  # Start of building, negative height
        events.append((r, 0, 0))  # End of building, height 0

    events.sort()

    skyline = []
    live = [(0, float('inf'))]  # (height, end)
    heapq.heapify(live)
    
    for x, neg_h, r in events:
        while live[0][1] <= x:
            heapq.heappop(live)
        
        if neg_h != 0:
            heapq.heappush(live, (neg_h, r))
        
        if not skyline or -skyline[-1][1] != live[0][0]:
            skyline.append((x, -live[0][0]))
    
    return skyline

def test_getSkyline():
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
            "input": [[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[0,5,12],[20,25,7]],
            "expected": [[0,12],[5,12],[10,7],[15,7],[20,7],[25,0]]
        },
        {
            "input": [],
            "expected": []
        }
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        buildings = test_case["input"]
        expected = test_case["expected"]
        actual = getSkyline(buildings)

        if actual == expected:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: {buildings}")
            print(f"  Expected: {expected}")
            print(f"  Actual: {actual}")

    print(f"\nCorrect: {num_correct}/{total_tests}")

if __name__ == "__main__":
    test_getSkyline()