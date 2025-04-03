def solve():
    def count_employees_earning_more_than_average(employee_salaries):
        """
        Calculates the number of employees earning more than the average salary.

        Args:
            employee_salaries: A list of dictionaries, where each dictionary
                               represents an employee with keys 'employee_id' and 'salary'.

        Returns:
            The number of employees earning more than the average salary.
        """
        if not employee_salaries:
            return 0

        total_salary = sum(employee['salary'] for employee in employee_salaries)
        average_salary = total_salary / len(employee_salaries)

        count_above_average = 0
        for employee in employee_salaries:
            if employee['salary'] > average_salary:
                count_above_average += 1

        return count_above_average

    test_cases = [
        {
            "input": [
                {'employee_id': 1, 'salary': 50000},
                {'employee_id': 2, 'salary': 60000},
                {'employee_id': 3, 'salary': 40000}
            ],
            "expected_output": 1
        },
        {
            "input": [
                {'employee_id': 1, 'salary': 70000},
                {'employee_id': 2, 'salary': 80000},
                {'employee_id': 3, 'salary': 90000}
            ],
            "expected_output": 0
        },
        {
            "input": [
                {'employee_id': 1, 'salary': 40000},
                {'employee_id': 2, 'salary': 40000},
                {'employee_id': 3, 'salary': 40000}
            ],
            "expected_output": 0
        },
        {
            "input": [
                {'employee_id': 1, 'salary': 60000},
                {'employee_id': 2, 'salary': 50000},
                {'employee_id': 3, 'salary': 70000},
                {'employee_id': 4, 'salary': 40000}
            ],
            "expected_output": 2
        },
        {
            "input": [],
            "expected_output": 0
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]

        actual_output = count_employees_earning_more_than_average(input_data)

        if actual_output == expected_output:
            print(f'Test {i+1}: True')
            correct_tests += 1
        else:
            print(f'Test {i+1}: False')

    print(f'\nCorrect tests: {correct_tests}/{total_tests}')

solve()