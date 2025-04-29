def max_profit(prices):
    """
    Calculates the maximum profit achievable by buying and selling stocks multiple times.

    Args:
      prices: A list of integers representing the price of a stock on each day.

    Returns:
      The maximum profit achievable.
    """
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit

def test_max_profit():
    """
    Tests the max_profit function with various test cases.
    """
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
        ([2, 1, 2, 0, 1], 2),
        ([1, 2], 1),
        ([2, 1], 0),
        ([2, 2], 0),
        ([1], 0),
        ([], 0),
        ([0, 1, 5, 2, 6, 0, 3], 10),
        ([3,2,6,5,0,3], 7)
    ]
    
    correct_count = 0
    total_count = len(test_cases)

    for prices, expected_profit in test_cases:
        actual_profit = max_profit(prices)
        if actual_profit == expected_profit:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Input: {prices}")
            print(f"Expected: {expected_profit}, Actual: {actual_profit}")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_max_profit()