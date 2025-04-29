import collections
from typing import List

class Solution:
    """
    Solves the Expression Add Operators problem using backtracking.
    """
    def addOperators(self, num: str, target: int) -> List[str]:
        """
        Finds all possible ways to insert binary operators (+, -, *) between
        the digits of num such that the expression evaluates to target.

        Args:
            num: A string containing only digits.
            target: The target integer value.

        Returns:
            A list of all valid expression strings.
        """
        results = []
        n = len(num)

        # Handle empty input string edge case, although constraints state len >= 1
        if not num:
            return []

        def backtrack(index: int, path: str, current_value: int, prev_operand: int):
            """
            Recursive helper function for backtracking.

            Args:
                index: Current starting index in the num string to form the next operand.
                path: The expression string built so far.
                current_value: The evaluated value of the expression constructed by 'path'.
                prev_operand: The value of the last operand added/subtracted/multiplied.
                              This is crucial for handling multiplication precedence correctly.
                              For example, in "1+2*3", when processing "*3", we need to know
                              the previous operand was 2 to calculate 1 + (2*3).
                              The state tracks this as: current_value = 1+2=3, prev_operand = 2.
                              New value = (current_value - prev_operand) + (prev_operand * current_num)
                                        = (3 - 2) + (2 * 3) = 1 + 6 = 7.
                              New prev_operand = prev_operand * current_num = 2 * 3 = 6.
            """
            # Base case: If we have processed all digits in the num string
            if index == n:
                # Check if the evaluated value matches the target
                if current_value == target:
                    results.append(path)
                return

            # Explore potential numbers starting from the current index
            for i in range(index, n):
                # Extract the substring for the current number operand
                current_num_str = num[index : i + 1]

                # Handle leading zeros: A number like "05" is invalid, but "0" itself is valid.
                # If the substring has more than one digit and starts with '0',
                # it's an invalid number representation. We can stop exploring
                # longer numbers starting from this '0' at the current 'index'.
                if len(current_num_str) > 1 and current_num_str[0] == '0':
                    break # Pruning: No valid number can be formed further from this path

                current_num = int(current_num_str)

                if index == 0:
                    # This is the first number in the expression, no operator precedes it.
                    # Initialize the path and values.
                    backtrack(i + 1, current_num_str, current_num, current_num)
                else:
                    # Not the first number, so we need to add an operator before it.

                    # --- Addition (+) ---
                    # New path includes "+ current_num_str"
                    # New value is simply current_value + current_num
                    # New prev_operand for the *next* step is +current_num
                    backtrack(i + 1, path + "+" +