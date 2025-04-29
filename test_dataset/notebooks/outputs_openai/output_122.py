def max_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit

test_cases = [
    ([7,1,5,3,6,4], 7),
    ([1,2,3,4,5], 4),
    ([7,6,4,3,1], 0),
]

correct = 0
total = len(test_cases)

for prices, expected in test_cases:
    result = max_profit(prices)
    is_correct = result == expected
    print(is_correct)
    if is_correct:
        correct += 1

print(f"{correct}/{total}")