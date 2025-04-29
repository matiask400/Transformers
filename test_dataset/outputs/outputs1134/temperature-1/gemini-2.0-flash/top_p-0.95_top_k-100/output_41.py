import heapq

def mincostToHireWorkers(quality, wage, K):
    N = len(quality)
    workers = []
    for i in range(N):
        workers.append((wage[i] / quality[i], quality[i]))

    workers.sort()
    
    total_quality = 0
    heap = []
    ans = float('inf')

    for ratio, q in workers:
        heapq.heappush(heap, -q)
        total_quality += q

        if len(heap) > K:
            total_quality += heapq.heappop(heap)

        if len(heap) == K:
            ans = min(ans, ratio * total_quality)

    return ans

def test_mincostToHireWorkers():
    tests = [
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
            "quality": [3, 1, 10, 10, 1],
            "wage": [4, 8, 2, 2, 7],
            "K": 2,
            "expected": 24.0
        }
    ]

    num_tests = len(tests)
    num_correct = 0

    for i, test in enumerate(tests):
        quality = test["quality"]
        wage = test["wage"]
        K = test["K"]
        expected = test["expected"]
        
        actual = mincostToHireWorkers(quality, wage, K)
        
        if abs(actual - expected) < 1e-5:
            print("True")
            num_correct += 1
        else:
            print("False")
            print(f"Test {i+1}: Expected {expected}, but got {actual}")

    print(f"{num_correct}/{num_tests}")

if __name__ == "__main__":
    test_mincostToHireWorkers()