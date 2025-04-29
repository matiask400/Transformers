import heapq

def mincost_to_hire(quality, wage, K):
    workers = sorted([(w/q, q) for q, w in zip(quality, wage)], key=lambda x: x[0])
    heap = []
    sumq = 0
    res = float('inf')
    for ratio, q in workers:
        heapq.heappush(heap, -q)
        sumq += q
        if len(heap) > K:
            removed = -heapq.heappop(heap)
            sumq -= removed
        if len(heap) == K:
            res = min(res, ratio * sumq)
    return res

if __name__ == "__main__":
    tests = [
        {
            'quality': [10,20,5],
            'wage': [70,50,30],
            'K': 2,
            'expected': 105.00000
        },
        {
            'quality': [3,1,10,10,1],
            'wage': [4,8,2,2,7],
            'K': 3,
            'expected': 30.66667
        },
        # Additional tests can be added here
    ]

    correct = 0
    total = len(tests)
    for test in tests:
        result = mincost_to_hire(test['quality'], test['wage'], test['K'])
        expected = test['expected']
        if abs(result - expected) <= 1e-5:
            print('True')
            correct +=1
        else:
            print('False')
    print(f"{correct}/{total}")