def least_interval(tasks, n):
    """
    Calculates the least number of units of times that the CPU will take to finish all the given tasks.

    Args:
        tasks: A characters array representing the tasks a CPU needs to do.
        n: A non-negative integer representing the cooldown period between two same tasks.

    Returns:
        The least number of units of times that the CPU will take to finish all the given tasks.
    """

    task_counts = {}
    for task in tasks:
        task_counts[task] = task_counts.get(task, 0) + 1

    max_count = 0
    max_count_tasks = 0
    for count in task_counts.values():
        if count > max_count:
            max_count = count
            max_count_tasks = 1
        elif count == max_count:
            max_count_tasks += 1

    result = max((max_count - 1) * (n + 1) + max_count_tasks, len(tasks))
    return result


def test_least_interval():
    """
    Tests the least_interval function with several test cases.
    """

    test_cases = [
        {
            "tasks": ["A", "A", "A", "B", "B", "B"],
            "n": 2,
            "expected": 8,
        },
        {
            "tasks": ["A", "A", "A", "B", "B", "B"],
            "n": 0,
            "expected": 6,
        },
        {
            "tasks": ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"],
            "n": 2,
            "expected": 16,
        },
        {
            "tasks": ["A", "A", "B", "B"],
            "n": 2,
            "expected": 4,
        },
        {
            "tasks": ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"],
            "n": 0,
            "expected": 12,
        },
        {
            "tasks": ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"],
            "n": 2,
            "expected": 12,
        },
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        tasks = test_case["tasks"]
        n = test_case["n"]
        expected = test_case["expected"]
        actual = least_interval(tasks, n)

        if actual == expected:
            print(f"Test {i + 1}: True")
            num_correct += 1
        else:
            print(f"Test {i + 1}: False (Expected: {expected}, Actual: {actual})")

    print(f"\n{num_correct}/{total_tests} correct")


if __name__ == "__main__":
    test_least_interval()