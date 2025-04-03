def solve():
    def task_scheduler(tasks, n):
        if n == 0:
            return len(tasks)

        task_counts = {}
        for task in tasks:
            task_counts[task] = task_counts.get(task, 0) + 1

        max_freq = 0
        for task in task_counts:
            max_freq = max(max_freq, task_counts[task])

        max_freq_count = 0
        for task in task_counts:
            if task_counts[task] == max_freq:
                max_freq_count += 1

        return (max_freq - 1) * (n + 1) + max_freq_count

    def run_test(tasks, n, expected_output):
        output = task_scheduler(tasks, n)
        if output == expected_output:
            print('True')
            return True
        else:
            print('False')
            return False

    test_cases = [
        {
            "tasks": ["A","A","A","B","B","B"],
            "n": 2,
            "expected_output": 8
        },
        {
            "tasks": ["A","A","A","B","B","B"],
            "n": 0,
            "expected_output": 6
        },
        {
            "tasks": ["A","A","A","A","A","A","B","C","D","E","F","G"],
            "n": 2,
            "expected_output": 16
        },
        {
            "tasks": ["A","B","C","D","E","A","B","C","D","E"],
            "n": 2,
            "expected_output": 10
        },
        {
            "tasks": ["A","A","A","A","B","B","B","C","C"],
            "n": 2,
            "expected_output": 11
        },
        {
            "tasks": ["A","A","A","A","A","A","B","C","D","E","F","G"],
            "n": 0,
            "expected_output": 12
        },
        {
            "tasks": ["A","A","A","B","B","B", "C","C","C", "D","D","D"],
            "n": 2,
            "expected_output": 12
        },
        {
            "tasks": ["A","A","A","B","B","B", "C","C","C", "D","D","D"],
            "n": 3,
            "expected_output": 16
        },
        {
            "tasks": ["A","A","A","B","B","B", "C","C","C", "D","D","D"],
            "n": 4,
            "expected_output": 20
        },
        {
            "tasks": ["A","A","A","A","A","A","A","A","A","A","A","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],
            "n": 2,
            "expected_output": 38
        }
    ]

    correct_count = 0
    for test_case in test_cases:
        if run_test(test_case["tasks"], test_case["n"], test_case["expected_output"]):
            correct_count += 1

    print(f"{correct_count}/{len(test_cases)}")

solve()