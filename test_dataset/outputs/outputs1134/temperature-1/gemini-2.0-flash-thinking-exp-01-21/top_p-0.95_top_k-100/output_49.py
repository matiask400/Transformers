from collections import Counter

def least_interval(tasks, n):
    task_counts = Counter(tasks)
    remaining_counts = dict(task_counts)
    next_available_time = {task: 0 for task in task_counts}
    current_time = 0
    schedule = []
    while sum(remaining_counts.values()) > 0:
        available_tasks = []
        for task in remaining_counts:
            if remaining_counts[task] > 0 and next_available_time[task] <= current_time:
                available_tasks.append(task)
        if available_tasks:
            best_task = None
            max_remaining_count = -1
            for task in available_tasks:
                if remaining_counts[task] > max_remaining_count:
                    max_remaining_count = remaining_counts[task]
                    best_task = task
            schedule.append(best_task)
            remaining_counts[best_task] -= 1
            next_available_time[best_task] = current_time + n + 1
        else:
            schedule.append('idle')
        current_time += 1
    return len(schedule)

def run_tests():
    test_cases = [
        {"tasks": ["A","A","A","B","B","B"], "n": 2, "expected": 8},
        {"tasks": ["A","A","A","B","B","B"], "n": 0, "expected": 6},
        {"tasks": ["A","A","A","A","A","A","B","C","D","E","F","G"], "n": 2, "expected": 16},
        {"tasks": ["A","A","A","A","A","A","B","C","D","E","F","G"], "n": 0, "expected": 12},
        {"tasks": ["A","A","A","A","A","A","B","C","D","E","F","G"], "n": 1, "expected": 14},
        {"tasks": ["A","B","C","D","E","F","G","A","A","A","A","A","A"], "n": 2, "expected": 16},
        {"tasks": ["A","B","C","D","E","F","G","A","A","A","A","A","A"], "n": 1, "expected": 14},
        {"tasks": ["A","B","C","D","E","F","G","A","A","A","A","A","A"], "n": 0, "expected": 13},
        {"tasks": ["A","A","B","B"], "n": 2, "expected": 4},
        {"tasks": ["A","A","B","B"], "n": 0, "expected": 4},
        {"tasks": ["A","A","A","B","B","C"], "n": 2, "expected": 7},
        {"tasks": ["A","A","A","B","B","C"], "n": 0, "expected": 6},
    ]
    
    correct_count = 0
    for i, case in enumerate(test_cases):
        result = least_interval(case["tasks"], case["n"])
        if result == case["expected"]:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Expected: {case['expected']}, Got: {result})")
            
    print(f"\n{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()