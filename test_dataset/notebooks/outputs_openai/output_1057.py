def assign_bikes(workers, bikes):
    from collections import defaultdict

    N = len(workers)
    M = len(bikes)
    distance_map = defaultdict(list)

    for i, (wx, wy) in enumerate(workers):
        for j, (bx, by) in enumerate(bikes):
            dist = abs(wx - bx) + abs(wy - by)
            distance_map[dist].append((i, j))

    assigned_workers = set()
    assigned_bikes = set()
    result = [-1] * N

    for dist in sorted(distance_map.keys()):
        pairs = sorted(distance_map[dist], key=lambda x: (x[0], x[1]))
        for worker, bike in pairs:
            if worker not in assigned_workers and bike not in assigned_bikes:
                assigned_workers.add(worker)
                assigned_bikes.add(bike)
                result[worker] = bike
                if len(assigned_workers) == N:
                    return result
    return result

# Test cases
test_cases = [
    {
        "workers": [[0,0],[2,1]],
        "bikes": [[1,2],[3,3]],
        "expected": [1,0]
    },
    {
        "workers": [[0,0],[1,1],[2,0]],
        "bikes": [[1,0],[2,2],[2,1]],
        "expected": [0,2,1]
    },
    {
        "workers": [[0,0]],
        "bikes": [[0,0]],
        "expected": [0]
    },
    {
        "workers": [[0,0],[1,0],[2,0]],
        "bikes": [[1,0],[2,0],[3,0]],
        "expected": [0,1,2]
    },
    {
        "workers": [[0,0],[0,2],[1,1]],
        "bikes": [[1,0],[2,2],[2,1]],
        "expected": [0,2,1]
    }
]

passed = 0
total = len(test_cases)

for idx, test in enumerate(test_cases):
    workers = test["workers"]
    bikes = test["bikes"]
    expected = test["expected"]
    output = assign_bikes(workers, bikes)
    if output == expected:
        print("True")
        passed += 1
    else:
        print("False")

print(f"{passed}/{total}")