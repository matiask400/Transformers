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

    while not all(worker_assigned):
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

        ans[best_worker] = best_bike
        worker_assigned[best_worker] = True
        bike_assigned[best_bike] = True

    return ans


def manhattan_distance(p1, p2):
    """
    Calculates the Manhattan distance between two points.

    Args:
        p1: The coordinates of the first point.
        p2: The coordinates of the second point.

    Returns:
        The Manhattan distance between the two points.
    """

    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def test_assign_bikes():
    """
    Tests the assign_bikes function.
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
            "workers": [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]],
            "bikes": [[0, 999], [1, 999], [2, 999], [3, 999], [4, 999], [5, 999]],
            "expected": [0, 1, 2, 3, 4, 5]
        },
        {
            "workers": [[0, 0]],
            "bikes": [[1, 0]],
            "expected": [0]
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
            print("True")
            num_correct += 1
        else:
            print("False")
            print(f"Test case {i + 1} failed:")
            print(f"  Input: workers={workers}, bikes={bikes}")
            print(f"  Expected: {expected}")
            print(f"  Actual: {actual}")

    print(f"{num_correct}/{total_tests}")


if __name__ == "__main__":
    test_assign_bikes()