import itertools

def min_cost_to_hire_workers(quality, wage, k):
    n = len(quality)
    min_total_wage = float('inf')

    worker_indices = list(range(n))
    combinations = itertools.combinations(worker_indices, k)

    for combo in combinations:
        current_quality = []
        current_wage = []
        current_ratios = []
        for index in combo:
            current_quality.append(quality[index])
            current_wage.append(wage[index])
            current_ratios.append(wage[index] / quality[index])
        
        max_ratio = 0
        for ratio in current_ratios:
            max_ratio = max(max_ratio, ratio)
            
        current_total_wage = max_ratio * sum(current_quality)
        min_total_wage = min(min_total_wage, current_total_wage)
        
    return min_total_wage

def test_min_cost_to_hire_workers():
    test_cases = [
        {
            "quality": [10, 20, 5],
            "wage": [70, 50, 30],
            "k": 2,
            "expected_output": 105.00000
        },
        {
            "quality": [3, 1, 10, 10, 1],
            "wage": [4, 8, 2, 2, 7],
            "k": 3,
            "expected_output": 30.66667
        },
        {
            "quality": [25,68,35,20,70,75,50,65,22,90],
            "wage": [72,78,92,52,62,79,78,96,79,85],
            "k": 7,
            "expected_output": 543.47826
        },
        {
            "quality": [60,54,86,91,31,45,82,87,94,29],
            "wage": [88,55,77,63,88,56,69,42,77,88],
            "k": 4,
            "expected_output": 241.03448
        }
    ]
    
    num_tests = len(test_cases)
    correct_tests = 0
    for i, case in enumerate(test_cases):
        quality = case["quality"]
        wage = case["wage"]
        k = case["k"]
        expected_output = case["expected_output"]
        
        actual_output = min_cost_to_hire_workers(quality, wage, k)
        
        if abs(actual_output - expected_output) < 1e-5:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
            
    print(f"{correct_tests}/{num_tests}")

if __name__ == '__main__':
    test_min_cost_to_hire_workers()