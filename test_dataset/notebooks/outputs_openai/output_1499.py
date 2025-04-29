def findMaxValueOfEquation(points, k):
    import heapq
    max_val = float('-inf')
    heap = []  # max heap, store (-yi + xi, xi)
    for x, y in points:
        while heap and x - heap[0][1] > k:
            heapq.heappop(heap)
        if heap:
            max_val = max(max_val, y + x + heap[0][0])
        heapq.heappush(heap, (-(y - x), x))
    return max_val

def run_tests():
    test_cases = [
        {
            "points": [[1,3],[2,0],[5,10],[6,-10]],
            "k": 1,
            "expected": 4
        },
        {
            "points": [[0,0],[3,0],[9,2]],
            "k": 3,
            "expected": 3
        },
        {
            "points": [[1,1],[2,2],[3,3],[4,4],[5,5]],
            "k": 2,
            "expected": 9
        },
        {
            "points": [[-1, -2],[0,0],[3,1],[5,10],[7,5]],
            "k": 4,
            "expected": 16
        },
        {
            "points": [[0,0],[1,1]],
            "k": 0,
            "expected": float('-inf')  # No pair satisfies |xj - xi| <=0 except i=j, which is invalid
        },
        {
            "points": [[1,5],[4,6],[5,10],[6,5]],
            "k": 3,
            "expected": 16
        }
    ]
    
    correct = 0
    total = len(test_cases)
    for idx, test in enumerate(test_cases):
        points = test["points"]
        k = test["k"]
        expected = test["expected"]
        result = findMaxValueOfEquation(points, k)
        is_correct = result == expected
        print(is_correct)
        if is_correct:
            correct +=1
    print(f"{correct}/{total}")

run_tests()