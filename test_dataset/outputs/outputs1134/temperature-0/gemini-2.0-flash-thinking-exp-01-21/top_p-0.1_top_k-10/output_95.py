def assign_bikes(workers, bikes):
    n_workers = len(workers)
    n_bikes = len(bikes)
    distances = []
    for i in range(n_workers):
        for j in range(n_bikes):
            dist = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
            distances.append((dist, i, j))

    distances.sort()

    worker_assigned = [False] * n_workers
    bike_assigned = [False] * n_bikes
    ans = [-1] * n_workers

    for dist, worker_index, bike_index in distances:
        if not worker_assigned[worker_index] and not bike_assigned[bike_index]:
            worker_assigned[worker_index] = True
            bike_assigned[bike_index] = True
            ans[worker_index] = bike_index

    return ans

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def test_assign_bikes():
    test_cases = [
        {
            "workers": [[0,0],[2,1]],
            "bikes": [[1,2],[3,3]],
            "expected_output": [1,0]
        },
        {
            "workers": [[0,0],[1,1],[2,0]],
            "bikes": [[1,0],[2,2],[2,1]],
            "expected_output": [0,2,1]
        },
        {
            "workers": [[7,7],[7,3],[1,7],[6,0],[4,5],[5,1],[6,6],[6,1]],
            "bikes": [[2,6],[5,3],[5,4],[6,1],[0,5],[7,7],[3,4],[2,7]],
            "expected_output": [5, 3, 4, 7, 2, 1, 0, 6]
        }
    ]

    num_correct = 0
    for i, case in enumerate(test_cases):
        workers = case["workers"]
        bikes = case["bikes"]
        expected_output = case["expected_output"]
        output = assign_bikes(workers, bikes)
        if output == expected_output:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: workers={workers}, bikes={bikes}")
            print(f"  Expected Output: {expected_output}")
            print(f"  Your Output: {output}")

    print(f"\n{num_correct} correct out of {len(test_cases)}")

if __name__ == '__main__':
    test_assign_bikes()