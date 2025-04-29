def solve():
    def test(function, test_cases):
        """
        Tests a given function with the provided test cases.

        Args:
            function: The function to test.
            test_cases: A list of tuples, where each tuple contains the input arguments for the function
                        followed by the expected output.
        """
        correct_count = 0
        total_count = len(test_cases)

        for case in test_cases:
            args = case[:-1]
            expected_output = case[-1]

            try:
                actual_output = function(*args)
                if actual_output == expected_output:
                    print('True')
                    correct_count += 1
                else:
                    print('False')
            except Exception as e:
                print('False')  # Or print the error for debugging
                #print(f"Error during test: {e}")


        print(f"{correct_count}/{total_count}")

    # Example function and test cases (replace with your actual function and test cases)
    def add(x, y):
        return x + y

    test_cases_add = [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (-5, 2, -3),
        (100, -50, 50),
    ]

    test(add, test_cases_add)

if __name__ == "__main__":
    solve()