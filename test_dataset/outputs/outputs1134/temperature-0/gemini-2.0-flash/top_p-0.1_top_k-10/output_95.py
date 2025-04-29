def assign_bikes(workers, bikes):
    """
    Assigns bikes to workers based on Manhattan distance.

    Args:
        workers: A list of worker coordinates.
        bikes: A list of bike coordinates.

    Returns:
        A list of bike indices assigned to each worker.
    """

    n = len(workers)
    m = len(bikes)
    ans = [0] * n
    worker_assigned = [False] * n
    bike_assigned = [False] * m

    while True:
        min_dist = float('inf')
        best_worker = -1
        best_bike = -1

        for i in range(n):
            if not worker_assigned[i]:
                for j in range(m):
                    if not bike_assigned[j]:
                        dist = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                        if dist < min_dist:
                            min_dist = dist
                            best_worker = i
                            best_bike = j
                        elif dist == min_dist:
                            if i < best_worker:
                                best_worker = i
                                best_bike = j
                            elif i == best_worker and j < best_bike:
                                best_bike = j

        if best_worker == -1:
            break

        ans[best_worker] = best_bike
        worker_assigned[best_worker] = True
        bike_assigned[best_bike] = True

    return ans


def test_assign_bikes():
    """
    Tests the assign_bikes function with multiple test cases.
    """

    test_cases = [
        {
            "workers": [[0, 0], [2, 1]],
            "bikes": [[1, 2], [3, 3]],
            "expected": [1, 0]
        },
        {
            "workers": [[0, 0], [1, 1], [2, 0]],
            "bikes": [[1, 0], [2, 2], [2, 1]],
            "expected": [0, 2, 1]
        },
        {
            "workers": [[0, 0]],
            "bikes": [[1, 0]],
            "expected": [0]
        },
        {
            "workers": [[0, 0], [0, 1]],
            "bikes": [[1, 0], [1, 1]],
            "expected": [0, 1]
        },
        {
            "workers": [[0, 0], [1, 0]],
            "bikes": [[0, 1], [1, 1]],
            "expected": [0, 1]
        }
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        workers = test_case["workers"]
        bikes = test_case["bikes"]
        expected = test_case["expected"]
        actual = assign_bikes(workers, bikes)

        if actual == expected:
            print(f"Test {i + 1}: True")
            num_correct += 1
        else:
            print(f"Test {i + 1}: False")
            print(f"  Input: workers={workers}, bikes={bikes}")
            print(f"  Expected: {expected}")
            print(f"  Actual: {actual}")

    print(f"\nCorrect: {num_correct}/{total_tests}")


if __name__ == "__main__":
    test_assign_bikes()