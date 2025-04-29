def solve():
    """
    This function executes a series of test cases and compares the results against expected values.
    It prints 'True' if a test case passes and 'False' if it fails.
    Finally, it prints the number of correct tests over the total.
    """

    test_cases = [
        {
            "input": 1,
            "expected_output": 1
        },
        {
            "input": 2,
            "expected_output": 2
        },
        {
            "input": 3,
            "expected_output": 3
        },
        {
            "input": 4,
            "expected_output": 4
        },
        {
            "input": 5,
            "expected_output": 5
        }
    ]
    
    def simple_function(x):
        return x
    
    num_correct = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        
        try:
            actual_output = simple_function(input_data) 
            if actual_output == expected_output:
                print("True")
                num_correct += 1
            else:
                print("False")
        except Exception as e:
            print("False")
            print(f"Error during test case {i+1}: {e}")

    print(f"{num_correct}/{total_tests}")
    
solve()