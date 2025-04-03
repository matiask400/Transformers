def least_interval(tasks, n):
    """
    Calculates the least number of units of times that the CPU will take to finish all the given tasks.

    Args:
        tasks (list[str]): A characters array representing the tasks a CPU needs to do.
        n (int): A non-negative integer representing the cooldown period between two same tasks.

    Returns:
        int: The least number of units of times that the CPU will take to finish all the given tasks.
    """
    from collections import Counter
    task_counts = Counter(tasks)
    max_count = max(task_counts.values())
    max_count_tasks = sum(1 for count in task_counts.values() if count == max_count)
    result = max((max_count - 1) * (n + 1) + max_count_tasks, len(tasks))
    return result

def test_least_interval():
    """
    Tests the least_interval function with different test cases.
    """
    test_cases = [
        {
            "tasks": ["A", "A", "A", "B", "B", "B"],
            "n": 2,
            "expected": 8
        },
        {
            "tasks": ["A", "A", "A", "B", "B", "B"],
            "n": 0,
            "expected": 6
        },
        {
            "tasks": ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"],
            "n": 2,
            "expected": 16
        },
        {
            "tasks": ["A","A","A","B","B","B","C","C","C","D","D","D","E","E","E"],
            "n": 2,
            "expected": 15
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        tasks = test_case["tasks"]
        n = test_case["n"]
        expected = test_case["expected"]
        actual = least_interval(tasks, n)
        if actual == expected:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Actual: {actual})")

    print(f"Correct tests: {correct_tests}/{total_tests}")

if __name__ == "__main__":
    test_least_interval()