def solve_problem(input_data, expected_output):
    """
    Solves the problem given the input data and compares the output with the expected output.
    Prints 'True' for each test passed and 'False' for each test failed, and finally prints the number of correct tests over the total.

    Args:
        input_data: The input data for the problem. This should be a dictionary where keys represent input names.
        expected_output: The expected output for the given input data.

    Returns:
        None
    """

    num_correct = 0
    total_tests = len(input_data)

    for i, (input_name, input_value) in enumerate(input_data.items()):
        try:
            actual_output = process_input(input_value)

            if actual_output == expected_output[input_name]:
                print(f"Test {i+1}: True")
                num_correct += 1
            else:
                print(f"Test {i+1}: False")
                print(f"  Expected: {expected_output[input_name]}")
                print(f"  Actual:   {actual_output}")
        except Exception as e:
            print(f"Test {i+1}: False")
            print(f"  Error: {e}")

    print(f"{num_correct}/{total_tests}")


def process_input(input_value):
    """
    This function is a placeholder for the actual logic to process the input data
    and return the output. You need to replace this with the specific code for
    the given problem.

    Args:
        input_value: The input data for the problem.

    Returns:
        The output of the processing logic.  Return type must match the expected output type.
    """
    # Replace this with your actual problem-solving logic
    # For demonstration, simply reverse the input string if it's a string,
    # otherwise return the input as is.
    if isinstance(input_value, str):
        return input_value[::-1]
    else:
        return input_value


if __name__ == '__main__':
    # Example usage:

    input_data = {
        "test1": "hello",
        "test2": 123,
        "test3": "world",
        "test4": [1, 2, 3]
    }

    expected_output = {
        "test1": "olleh",
        "test2": 123,
        "test3": "dlrow",
        "test4": [1, 2, 3]
    }

    solve_problem(input_data, expected_output)