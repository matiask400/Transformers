import sys
import io

# Define the function to solve the problem
def add_thousand_separator(n: int) -> str:
    """
    Given an integer n, add a dot (".") as the thousands separator 
    and return it in string format.
    Constraints: 0 <= n < 2^31
    
    Args:
        n: A non-negative integer.
        
    Returns:
        A string representation of n with dots as thousands separators.
    """
    # Python's f-string formatting provides a convenient way to add 
    # thousands separators. By default, it uses a comma (,) based on locale,
    # but typically defaults to comma in standard environments.
    # We can format with commas and then replace them with dots.
    
    # Format the number with commas as thousands separators
    formatted_with_commas = f"{n:,}"
    
    # Replace the commas with the desired dot separator
    result_with_dots = formatted_with_commas.replace(",", ".")
    
    return result_with_dots

# Define the test runner function
def run_tests():
    """
    Runs predefined test cases against the add_thousand_separator function.
    Prints True/False for each test and a final summary as requested.
    """
    test_cases = [
        # Provided Examples
        (987, "987"),
        (1234, "1.234"),
        (123456789, "123.456.789"),
        (0, "0"),

        # Additional Cases
        (1000, "1.000"),
        (999999, "999.999"),
        (1000000, "1.000.000"),
        (2147483647, "2.147.483.647"), # Max value example (2**31 - 1)
        (12, "12"),
        (123, "123"),
        (12345, "12.345"),
        (123456, "123.456"),
        (1234567, "1.234.567"),
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for n_input, expected_output in test_cases:
        # Execute the function with the test input
        result = add_thousand_separator(n_input)
        
        # Compare the result with the expected output
        is_correct = (result == expected_output)
        
        # Print True or False for the current test
        print(is_correct) 
        
        # Increment the counter if the test passed
        if is_correct:
            correct_count += 1

    # Print the final summary line: number of correct tests / total tests
    print(f"{correct_count}/{total_tests}")

# Execute the test runner when the script is run
if __name__ == "__main__":
    run_tests()