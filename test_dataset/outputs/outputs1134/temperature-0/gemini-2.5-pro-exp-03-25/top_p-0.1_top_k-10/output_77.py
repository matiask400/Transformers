import sys
import io

class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        """
        Finds all possible ways to insert binary operators (+, -, *) between the digits
        of num such that the expression evaluates to target.

        Args:
            num: A string containing only digits.
            target: The target integer value.

        Returns:
            A list of strings, where each string is a valid expression.
        """
        n = len(num)
        results = []

        def backtrack(index: int, path: str, current_value: int, last_term: int):
            """
            Recursive helper function for backtracking.

            Args:
                index: Current starting index in the num string.
                path: The expression string built so far.
                current_value: The evaluated value of the expression so far.
                last_term: The value of the last operand added/subtracted/multiplied.
                           Needed to handle multiplication precedence correctly.
            """
            # Base case: If we have processed all digits
            if index == n:
                if current_value == target:
                    results.append(path)
                return

            # Iterate through possible numbers starting from 'index'
            for j in range(index, n):
                # Extract the current number substring
                current_num_str = num[index : j + 1]

                # Handle leading zeros: numbers like "05", "00" are invalid unless it's just "0"
                if len(current_num_str) > 1 and current_num_str[0] == '0':
                    # If a number starts with '0' and has more than one digit,
                    # it's invalid. We can stop extending this number further.
                    break 
                
                current_num = int(current_num_str)

                if index == 0:
                    # If it's the first number in the expression
                    backtrack(j + 1, current_num_str, current_num, current_num)
                else:
                    # Try adding '+'
                    backtrack(j + 1, path + '+' + current_num_str, current_value + current_num, current_num)

                    # Try adding '-'
                    backtrack(j + 1, path + '-' + current_num_str, current_value - current_num, -current_num)

                    # Try adding '*'
                    # The value update handles precedence:
                    # (current_value - last_term) effectively removes the last operation's effect.
                    # Then, we add the result of the multiplication (last_term * current_num).
                    new_value_mult = (current_value - last_term) + (last_term * current_num)
                    new_last_term_mult = last_term * current_num
                    backtrack(j + 1, path + '*' + current_num_str, new_value_mult, new_last_term_mult)

        # Start the backtracking process from the beginning of the string
        backtrack(0, "", 0, 0)
        return results

# --- Testing Framework ---

def run_test(test_id, num, target, expected_output):
    """
    Runs a single test case.

    Args:
        test_id: An identifier for the test.
        num: Input string 'num'.
        target: Input integer 'target'.
        expected_output: The expected list of expression strings.

    Returns:
        True if the test passes, False otherwise.
    """
    solver = Solution()
    actual_output = solver.addOperators(num, target)
    
    # Sort both lists to compare them regardless of order
    actual_output.sort()
    expected_output.sort()

    result = actual_output == expected_output
    print(f"{result}")
    # Optional: Print details on failure
    # if not result:
    #     print(f"Test {test_id} Failed:")
    #     print(f"  Input: num='{num}', target={target}")
    #     print(f"  Expected: {expected_output}")
    #     print(f"  Actual:   {actual_output}")
    return result

def solve():
    """
    Runs all predefined test cases.
    """
    test_cases = [
        (1, "123", 6, ["1*2*3", "1+2+3"]),
        (2, "232", 8, ["2*3+2", "2+3*2"]),
        (3, "105", 5, ["1*0+5", "10-5"]),
        (4, "00", 0, ["0*0", "0+0", "0-0"]),
        (5, "3456237490", 9191, []),
        (6, "1", 1, ["1"]),
        (7, "10", 1, ["1*0"]), # Test case with multiplication by zero
        (8, "10", 10, ["10"]), # Test case with multi-digit number only
        (9, "100", 0, ["1*0*0", "1*0+0", "1*0-0", "10*0"]), # More zero cases
        (10, "2147483648", -2147483648, []), # Edge case near integer limits (target unreachable)
        (11, "2147483647", 2147483647, ["2147483647"]), # Max int value
        (12, "11", 1, ["1*1"]),
        (13, "11", 2, ["1+1"]),
        (14, "11", 0, ["1-1"]),
        (15, "11", 11, ["11"]),
        (16, "543", 23, ["5*4+3"]),
        (17, "543", 17, ["5+4*3"]),
        (18, "543", 7, ["5-4+3", "5+4-3"]), # Check multiple solutions
        (19, "0", 0, ["0"]), # Single digit zero
    ]

    correct_count = 0
    total_tests = len(test_cases)

    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    for i, (test_id, num, target, expected) in enumerate(test_cases):
        if run_test(test_id, num, target, expected):
            correct_count += 1

    # Restore stdout
    sys.stdout = old_stdout
    output_str = captured_output.getvalue()
    
    # Print the captured output
    print(output_str, end="")

    # Print the final summary
    print(f"{correct_count}/{total_tests}")

# Execute the tests
if __name__ == "__main__":
    solve()