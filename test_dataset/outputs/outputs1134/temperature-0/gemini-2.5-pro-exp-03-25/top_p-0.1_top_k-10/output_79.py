import sys 

# Function definition as required
def solve():
    """
    Solves the problem of finding the lexicographically smallest string of length n and numeric value k.
    Includes the core logic function and test execution framework.
    Prints 'True' for each passed test, 'False' for each failed test, and a summary at the end.
    """

    # The core logic function
    def getSmallestString(n: int, k: int) -> str:
        """
        Generates the lexicographically smallest string of length n and numeric value k.

        The numeric value of a character is its 1-indexed position in the alphabet ('a'=1, 'z'=26).
        The numeric value of a string is the sum of its characters' numeric values.

        Args:
            n: The length of the string.
            k: The target numeric value of the string.

        Returns:
            The lexicographically smallest string satisfying the conditions.
        
        Constraints:
            1 <= n <= 10^5
            n <= k <= 26 * n
        """
        # Initialize the result as a list of 'a' characters. Using a list for mutability.
        # A string of n 'a's has the minimum possible numeric value for length n, which is n * 1 = n.
        result_list = ['a'] * n
        
        # Calculate the remaining value that needs to be added to the base value 'n' to reach the target 'k'.
        remaining_value = k - n

        # Iterate through the character positions from right to left (index n-1 down to 0).
        # To get the lexicographically smallest string, we want to keep characters at the beginning
        # as small as possible ('a'). This means we should make characters at the end as large as needed.
        # By filling the required value from right to left, we ensure larger characters are placed towards the end.
        for i in range(n - 1, -1, -1):
            
            # If the remaining value is 0 or less, it means we have reached the target sum 'k'.
            # No more modifications are needed.
            if remaining_value <= 0: 
                break

            # Determine the maximum possible increase in value for the character at the current position 'i'.
            # The character starts as 'a' (value 1). The maximum value is 'z' (value 26).
            # Therefore, the maximum increase in value for a single character is 26 - 1 = 25.
            increase = min(remaining_value, 25)

            # Update the character at the current position 'i'.
            # `ord('a')` gives the ASCII value of 'a'.
            # Adding `increase` (which is between 0 and 25) gives the ASCII value of the target character.
            # For example, if increase is 0, `ord('a') + 0` gives ASCII of 'a'.
            # If increase is 25, `