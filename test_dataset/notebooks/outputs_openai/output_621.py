from collections import Counter

def leastInterval(tasks, n):
    task_counts = Counter(tasks)
    max_freq = max(task_counts.values())
    max_count = sum(1 for count in task_counts.values() if count == max_freq)
    intervals = max((max_freq - 1) * (n + 1) + max_count, len(tasks))
    return intervals

def run_tests():
    test_cases = [
        (["A","A","A","B","B","B"], 2, 8),
        (["A","A","A","B","B","B"], 0, 6),
        (["A","A","A","A","A","A","B","C","D","E","F","G"], 2, 16),
        (["A"], 0, 1),
        (["A","B","C","A","B","C"], 3, 6),
        (["A","A","A","B","B","B","C","C","D","D"], 2, 10),
        (["A","A","A","A","B","B","B","C","C","D","D"], 2, 11),
        (["A","A","A","B","B","B","C","C","D","D","E","E","F","F"], 2, 14),
        (["A","B","A"], 3, 5),
        (["A","A","A","B","B","B","C","D","E","F","G","H"], 2, 12)
    ]
    
    correct = 0
    total = len(test_cases)
    for idx, (tasks, n, expected) in enumerate(test_cases):
        result = leastInterval(tasks, n)
        if result == expected:
            print(True)
            correct += 1
        else:
            print(False)
    print(f"{correct} / {total}")

run_tests()