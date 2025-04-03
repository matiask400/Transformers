import sys

# Set default encoding to UTF-8 for compatibility, especially in environments
# where the default might not be UTF-8 (e.g., some Windows configurations).
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8')

def format_number(n: int) -> str:
    """
    Adds a dot (".") as the thousands separator to a non-negative integer.

    Args:
        n: The integer to format (0 <= n < 2^31).

    Returns:
        The formatted string with dots as thousands separators.
    """
    # Handle the edge case of 0 separately if needed, although f-string handles it.
    if n == 0:
        return "0"

    # Method 1: Using f-string formatting (most Pythonic)
    # The f-string format specifier ',' adds a comma as a thousands separator
    # based on locale settings (which usually defaults to comma for US English).
    # We then replace the comma with a dot.
    formatted_with_comma = f"{n:,}"
    formatted_with_dot = formatted_with_comma.replace(",", ".")
    return formatted_with_dot

    # # Method 2: Manual iteration (right-to-left)
    # s = str(n)
    # result = ""
    # count = 0
    # # Iterate through the string representation of n from right to left
    # for i in range(len(s) - 1, -1, -1):
    #     result = s[i] + result # Prepend the current digit
    #     count += 1
    #     # If we've added 3 digits and it's not the very first digit of the number
    #     if count == 3 and i != 0:
    #         result = "." + result # Prepend a dot
    #         count = 0 # Reset the counter
    # return result

    # # Method 3: Slicing and Joining
    # s = str(n)
    # length = len(s)
    # if length <= 3:
    #     return s # No separator needed for numbers <= 999
    #
    # # Calculate the length of the first group (1, 2, or 3 digits)
    # first_group_len = length % 3
    # if first_group_len == 0:
    #     first_group_len = 3
    #
    # parts = [s[:first_group_len]] # Add the first part
    #
    # # Add the remaining parts in chunks of 3
    # for i in range(first_group_len, length, 3):
    #     parts.append(s[i:i+3])
    #
    # return ".".join(parts)


def run_tests():
    """
    Runs predefined test cases against the format_number function and prints results.
    """
    test_cases = [
        # Input (n), Expected Output
        (987, "987"),
        (1234, "1.234"),
        (123456789, "123.456.789"),
        (0, "0"),
        (1000, "1.000"),
        (9999, "9.999"),
        (10000, "10.000"),
        (123, "123"),
        (12345, "12.345"),
        (123456, "123.456"),
        (1000000, "1.000.000"),
        (2147483647, "2.147.483.647"), # Max value for 2^31 - 1
        (1000000000, "1.000.000.000"),
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (input_val, expected_output) in enumerate(test_cases):
        result = format_number(input_val)
        is_correct = (result == expected_output)
        print(f"{is_correct}") # Print True or False for each test
        if is_correct:
            correct_count += 1
        # Optional: Print details on failure
        # else:
        #     print(f"Test {i+1} Failed: Input={input_val}, Expected='{expected_output}', Got='{result}'")


    print(f"\n{correct_count}/{total_tests}") # Print final score

# Main execution block to run the tests when the script is executed
if __name__ == "__main__":
    run_tests()