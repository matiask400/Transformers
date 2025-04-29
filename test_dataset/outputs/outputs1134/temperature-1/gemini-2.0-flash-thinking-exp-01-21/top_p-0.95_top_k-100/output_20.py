def solve_query(employees_data):
    """
    Simulates a SQL query to find names of employees in the 'Sales' department.

    Args:
        employees_data: A list of dictionaries, where each dictionary represents a row in the Employees table.

    Returns:
        A list of strings, representing the names of employees in the 'Sales' department.
    """
    sales_employees = []
    for employee in employees_data:
        if employee['department'] == 'Sales':
            sales_employees.append(employee['name'])
    return sales_employees

def test_solution():
    """
    Tests the solve_query function with different test cases and compares the output with expected outputs.
    Prints 'True' for each test passed and 'False' for each test failed, and finally prints the test summary.
    """
    test_cases = [
        {
            "employees_data": [
                {'employee_id': 1, 'name': 'Alice', 'department': 'Sales', 'salary': 50000},
                {'employee_id': 2, 'name': 'Bob', 'department': 'Marketing', 'salary': 60000},
                {'employee_id': 3, 'name': 'Charlie', 'department': 'Sales', 'salary': 55000},
                {'employee_id': 4, 'name': 'David', 'department': 'Engineering', 'salary': 70000},
                {'employee_id': 5, 'name': 'Eve', 'department': 'Engineering', 'salary': 75000}
            ],
            "expected_output": ['Alice', 'Charlie'],
            "test_name": "Test Case 1: Basic Sales Employees"
        },
        {
            "employees_data": [
                {'employee_id': 2, 'name': 'Bob', 'department': 'Marketing', 'salary': 60000},
                {'employee_id': 4, 'name': 'David', 'department': 'Engineering', 'salary': 70000},
                {'employee_id': 5, 'name': 'Eve', 'department': 'Engineering', 'salary': 75000}
            ],
            "expected_output": [],
            "test_name": "Test Case 2: No Sales Employees"
        },
        {
            "employees_data": [],
            "expected_output": [],
            "test_name": "Test Case 3: Empty Employee Table"
        },
        {
            "employees_data": [
                {'employee_id': 1, 'name': 'Alice', 'department': 'Sales', 'salary': 50000},
                {'employee_id': 2, 'name': 'Bob', 'department': 'Marketing', 'salary': 60000},
                {'employee_id': 3, 'name': 'Charlie', 'department': 'Sales', 'salary': 55000},
                {'employee_id': 4, 'name': 'David', 'department': 'Engineering', 'salary': 70000},
                {'employee_id': 5, 'name': 'Eve', 'department': 'Sales', 'salary': 75000},
                {'employee_id': 6, 'name': 'Frank', 'department': 'Marketing', 'salary': 62000}
            ],
            "expected_output": ['Alice', 'Charlie', 'Eve'],
            "test_name": "Test Case 4: Multiple Sales Employees"
        },
        {
            "employees_data": [
                {'employee_id': 1, 'name': 'Alice', 'department': 'sales', 'salary': 50000}, # lowercase sales
                {'employee_id': 2, 'name': 'Bob', 'department': 'Marketing', 'salary': 60000},
            ],
            "expected_output": [], # Assuming case-sensitive comparison
            "test_name": "Test Case 5: Case Sensitivity - lowercase 'sales'"
        },
         {
            "employees_data": [
                {'employee_id': 1, 'name': 'Alice', 'department': 'Sales ', 'salary': 50000}, # Sales with space
                {'employee_id': 2, 'name': 'Bob', 'department': 'Marketing', 'salary': 60000},
            ],
            "expected_output": [], # Assuming exact string match
            "test_name": "Test Case 6: Department with trailing space"
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for test_case in test_cases:
        actual_output = solve_query(test_case["employees_data"])
        expected_output = test_case["expected_output"]

        test_passed = sorted(actual_output) == sorted(expected_output) # sort to compare lists irrespective of order

        if test_passed:
            print(f"True - {test_case['test_name']}")
            correct_tests += 1
        else:
            print(f"False - {test_case['test_name']}")
            print(f"  Expected: {expected_output}")
            print(f"  Actual:   {actual_output}")

    print(f"\n{correct_tests}/{total_tests} tests passed")

if __name__ == '__main__':
    test_solution()