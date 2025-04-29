import sys 
# sys module is not strictly needed for this problem but included for potential future use
# if interaction with system arguments or standard I/O streams were required beyond basic print.
# For this specific problem, it could be omitted.
import io 
# io module is also not strictly needed here as we are not capturing stdout, 
# but included for completeness if such functionality were desired. It can be omitted.

# --- Solution Function ---
def maxProfit(prices: list[int]) -> int:
    """
    Calculates the maximum profit from buying and selling stocks multiple times.

    You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.
    Find the maximum profit you can achieve. You may complete as many transactions as you like 
    (i.e., buy one and sell one share of the stock multiple times).

    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the 
    stock before you buy again).

    The strategy is to accumulate profit whenever the price increases from one day to the next.
    This is equivalent to buying at the start of every upward trend and selling at the end.

    Args:
        prices: A list of integers representing stock prices on consecutive days. 
                Constraints: 1 <= prices.length <= 3 * 10^4, 0 <= prices[i] <= 10^4

    Returns:
        The maximum achievable profit.
    """
    max_profit = 0
    # Iterate through the prices starting from the second day (index 1)
    for i in range(1, len(prices)):
        # If the price on the current day is greater than the price on the previous day
        if prices[i] > prices[i-1]:
            # Add the difference (profit from this one-day rise) to the total profit
            max_profit += prices[i] - prices[i-1]
            
    # The accumulated profit represents the maximum possible profit with multiple transactions
    return max_profit

# --- Test Runner ---
def run_tests():
    """
    Runs predefined test cases against the maxProfit function and prints the results
    in the specified format: 'True' or 'False' for each test, followed by a summary line
    'correct_count/total_tests'.
    """
    test_cases = [
        # Tuple format: (input_prices, expected_output)
        # Provided examples
        ([7, 1, 5, 3, 6, 4], 7),  # Example 1: Buy at 1, sell at 5 (profit 4). Buy at 3, sell at 6 (profit 3). Total = 7.
        ([1, 2, 3, 4, 5], 4),    # Example 2: Buy at 1, sell at 5 (profit 4). Or (2-1)+(3-2)+(4-3)+(5-4) = 1+1+1+1 = 4.
        ([7, 6, 4, 3, 1], 0),    # Example 3: Prices always decrease, no profit possible.
        
        # Edge cases
        ([1], 0),                 # Single element array: No transactions possible.
        ([5, 5, 5, 5], 0),        # Constant price: No profit possible.
        
        # Additional test cases
        ([3, 3, 5, 0, 0, 3, 1, 4], 8), # Complex sequence: (5-3) + (3-0) + (4-1) = 2 + 3 + 3 = 8
        ([2, 1, 2, 0, 1], 2),    # Sequence with dips: (2-1) + (1-0) = 1 + 1 = 2
        ([6, 1, 3, 2, 4, 7], 7)  # Sequence with multiple peaks/troughs: (3-1) + (4-2) + (7-4) = 2 + 2 + 3 = 7
    ]

    correct_count = 0
    total_tests = len(test_cases)

    # Iterate through each test case
    for i, (prices, expected) in enumerate(test_cases):
        # Execute the solution function with the test input
        result = maxProfit(prices)

        # Compare the actual result with the expected result
        passed = (result == expected)
        
        # Print 'True' if the test passed, 'False' otherwise
        print(f"{passed}") 
        
        # Increment the count of correct tests if passed
        if passed:
            correct_count += 1

    # After all tests are run, print the final summary
    # The summary format is "correct_count/total_tests"
    # A newline is added before the summary for better readability in the console output.
    print(f"\n{correct_count}/{total_tests}") 

# --- Main execution block ---
if __name__ == '__main__':
    # Run the tests when the script is executed directly
    run_tests()