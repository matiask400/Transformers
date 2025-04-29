def max_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

def run_tests():
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
        ([2, 1, 2, 0, 1], 2),
        ([2], 0),
        ([1, 2], 1),
        ([2, 1], 0),
        ([1, 2, 3, 2, 4, 5], 7),
    ]
    correct_count = 0
    for i, (prices, expected_output) in enumerate(test_cases):
        output = max_profit(prices)
        if output == expected_output:
            print(True)
            correct_count += 1
        else:
            print(False)
    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()