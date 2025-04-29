import heapq

def mincostToHireWorkers(quality, wage, K):
    N = len(quality)
    workers = []
    for i in range(N):
        workers.append((wage[i] / quality[i], quality[i]))
    workers.sort()
    
    heap = []
    quality_sum = 0
    min_cost = float('inf')
    
    for ratio, q in workers:
        heapq.heappush(heap, -q)
        quality_sum += q
        
        if len(heap) > K:
            quality_sum += heapq.heappop(heap)
        
        if len(heap) == K:
            min_cost = min(min_cost, ratio * quality_sum)
            
    return min_cost

def test_mincostToHireWorkers():
    test_cases = [
        {
            "quality": [10, 20, 5],
            "wage": [70, 50, 30],
            "K": 2,
            "expected": 105.00000
        },
        {
            "quality": [3, 1, 10, 10, 1],
            "wage": [4, 8, 2, 2, 7],
            "K": 3,
            "expected": 30.66667
        },
        {
            "quality": [1, 2, 3, 4, 5],
            "wage": [5, 4, 3, 2, 1],
            "K": 3,
            "expected": 6.00000
        },
        {
            "quality": [3, 1, 10, 10, 1],
            "wage": [4, 8, 2, 2, 7],
            "K": 2,
            "expected": 24.00000
        },
        {
            "quality": [10, 20, 5],
            "wage": [70, 50, 30],
            "K": 3,
            "expected": 155.00000
        }
    ]
    
    num_correct = 0
    total_tests = len(test_cases)
    
    for i, test_case in enumerate(test_cases):
        quality = test_case["quality"]
        wage = test_case["wage"]
        K = test_case["K"]
        expected = test_case["expected"]
        
        result = mincostToHireWorkers(quality, wage, K)
        
        if abs(result - expected) < 1e-5:
            print("True")
            num_correct += 1
        else:
            print("False")
            print(f"Test case {i+1} failed: Expected {expected}, got {result}")
            
    print(f"{num_correct}/{total_tests}")

test_mincostToHireWorkers()