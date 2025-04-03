def solve_problem(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    return max_profit

def run_tests():
    test_cases = [
        ([7,1,5,3,6,4], 7),
        ([1,2,3,4,5], 4),
        ([7,6,4,3,1], 0),
        ([2,1,2,0,1], 2),
        ([2,7,1,4,6], 11),
        ([1], 0),
        ([], 0),
        ([1,1,1,1,1], 0)
    ]
    correct_tests = 0
    total_tests = len(test_cases)

    for i, (prices, expected_output) in enumerate(test_cases):
        actual_output = solve_problem(prices)
        if actual_output == expected_output:
            print(f'Test {i+1}: True')
            correct_tests += 1
        else:
            print(f'Test {i+1}: False')
            print(f'  Input: {prices}')
            print(f'  Expected Output: {expected_output}')
            print(f'  Actual Output: {actual_output}')

    print(f"\n{correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()