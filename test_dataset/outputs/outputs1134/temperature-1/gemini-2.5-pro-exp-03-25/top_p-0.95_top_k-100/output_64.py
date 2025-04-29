import sys 
# Setting higher recursion depth for potentially deep calls if needed, 
# although this problem uses an iterative approach.
# sys.setrecursionlimit(2000) 

def solve():
    """
    Solves the Best Time to Buy and Sell Stock II problem and runs tests.
    """

    def maxProfit(prices: list[int]) -> int:
        """
        Calculates the maximum profit from buying and selling stock multiple times.

        You can buy and sell on the same day if needed implicitly by summing
        consecutive price increases.
        Example: [1, 5, 3, 6] -> (5-1) + (6-3) = 4 + 3 = 7
        This is equivalent to buy at 1, sell at 5, then buy at 3, sell at 6.

        Another perspective: We add profit whenever the price increases from one day
        to the next.
        Example: [1, 2, 3, 4, 5] -> (2-1) + (3-2) + (4-3) + (5-4) = 1+1+1+1 = 4
        This is equivalent to buying at 1 and selling at 5.

        Args:
            prices: A list of integers representing stock prices on consecutive days.

        Returns:
            The maximum achievable profit.
        """
        max_profit = 0
        
        # If we have less than 2 days, we cannot make any transaction.
        if len(prices) < 2:
            return 0

        # Iterate through the prices starting from the second day.
        for i in range(1, len(prices)):
            # If the current day's price is higher than the previous day's price,
            # we can achieve a profit by buying on the previous day and selling today.
            # Since we can do multiple transactions, we simply add this potential profit.
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
                
        return max_profit

    # Define test cases
    # Each test case is a dictionary with 'prices' and 'expected' output.
    test_cases = [
        {'prices': [7,1,5,3,6,4], 'expected': 7},
        {'prices': [1,2,3,4,5], 'expected': 4},
        {'prices': [7,6,4,3,1], 'expected': 0},
        {'prices': [1], 'expected': 0}, # Edge case: single day
        {'prices': [], 'expected': 0}, # Edge case: empty list
        {'prices': [5, 1], 'expected': 0}, # Decreasing prices
        {'prices': [1, 5], 'expected': 4}, # Increasing prices
        {'prices': [2, 1, 2, 0, 1, 2], 'expected': 3}, # Multiple ups and downs
        {'prices': [6,1,3,2,4,7], 'expected': 7}, # More complex ups and downs
        {'prices': [3,3,5,0,0,3,1,4], 'expected': 8}, # Includes plateaus and zeros
        {'prices': [0, 5, 0, 5], 'expected': 10}, # Buying/selling at zero
    ]

    correct_count = 0
    total_count = len(test_cases)

    # Run tests
    for i, test in enumerate(test_cases):
        prices_input = test['prices']
        expected_output = test['expected']
        
        try:
            # Make a copy if the function were to modify the input (not the case here)
            # prices_copy = prices_input[:] 
            actual_output = maxProfit(prices_input)
            
            # Compare actual output with expected output
            passed = actual_output == expected_output
            print(f"{passed}") # Print True or False directly
            if passed:
                correct_count += 1
            # Optional: Uncomment below to print details on failure
            # else:
            #     print(f"Test {i+1} Failed: Input={prices_input}, Expected={expected_output}, Got={actual_output}")

        except Exception as e:
             # If any error occurs during execution, the test fails
             print(f"False") 
             # Optional: Uncomment below to print error details
             # print(f"Test {i+1} Failed with error: {e} for Input={prices_input}")

    # Print the final summary
    print(f"{correct_count}/{total_count}")

# Execute the solve function which includes the tests
solve()