import math

def min_cost_to_hire_workers(quality, wage, k):
    n = len(quality)
    workers = []
    for i in range(n):
        ratio = wage[i] / quality[i]
        workers.append({'ratio': ratio, 'quality': quality[i], 'index': i})
    workers.sort(key=lambda x: x['ratio'])

    min_cost = float('inf')

    for i in range(n):
        current_worker = workers[i]
        current_ratio = current_worker['ratio']
        current_worker_index = current_worker['index']

        possible_workers = []
        for j in range(i):
            possible_workers.append({'quality': workers[j]['quality'], 'index': workers[j]['index']})

        if len(possible_workers) < k - 1:
            continue

        possible_workers.sort(key=lambda x: x['quality'])
        selected_qualities = [current_worker['quality']]
        selected_indices = [current_worker_index]

        for j in range(k - 1):
            selected_qualities.append(possible_workers[j]['quality'])
            selected_indices.append(possible_workers[j]['index'])

        current_cost = current_ratio * sum(selected_qualities)
        min_cost = min(min_cost, current_cost)

    return min_cost

def solve():
    test_cases = [
        {
            "quality": [10, 20, 5],
            "wage": [70, 50, 30],
            "k": 2,
            "expected": 105.00000
        },
        {
            "quality": [3, 1, 10, 10, 1],
            "wage": [4, 8, 2, 2, 7],
            "k": 3,
            "expected": 30.66667
        }
    ]

    for i, case in enumerate(test_cases):
        quality = case["quality"]
        wage = case["wage"]
        k = case["k"]
        expected = case["expected"]
        output = min_cost_to_hire_workers(quality, wage, k)
        if abs(output - expected) < 1e-5:
            print(True)
        else:
            print(False)

    correct_count = 0
    for i, case in enumerate(test_cases):
        quality = case["quality"]
        wage = case["wage"]
        k = case["k"]
        expected = case["expected"]
        output = min_cost_to_hire_workers(quality, wage, k)
        if abs(output - expected) < 1e-5:
            correct_count += 1
    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    solve()