import sys
import io
import unittest
from unittest.mock import patch

# Since no specific SQL problem or schema details were provided beyond "SQL Schema",
# we will invent a simple, common SQL problem and schema to demonstrate the requested structure.
# Problem: Given tables 'Employees' and 'Departments', find the names of all employees
#          in a specific department, ordered alphabetically.
#
# Schema:
# Employees(id INT PRIMARY KEY, name VARCHAR, department_id INT, salary INT)
# Departments(id INT PRIMARY KEY, name VARCHAR)

# Function to simulate the SQL query execution
def solve_sql_problem(employees_data, departments_data, target_department_name):
    """
    Simulates an SQL query to find employee names in a specific department.

    Args:
        employees_data: A list of tuples representing employee rows (id, name, dept_id, salary).
        departments_data: A list of tuples representing department rows (id, name).
        target_department_name: The name of the department to query.

    Returns:
        A sorted list of employee names belonging to the target department.
        Returns an empty list if the department doesn't exist or has no employees.
    """
    target_dept_id = None
    # Find the department ID for the target department name
    # Equivalent to: SELECT id FROM Departments WHERE name = target_department_name
    for dept_id, dept_name in departments_data:
        if dept_name == target_department_name:
            target_dept_id = dept_id
            break

    if target_dept_id is None:
        return [] # Department not found

    employee_names = []
    # Find employees belonging to the target department ID
    # Equivalent to: SELECT name FROM Employees WHERE department_id = target_dept_id
    for emp_id, emp_name, emp_dept_id, emp_salary in employees_data:
        if emp_dept_id == target_dept_id:
            employee_names.append(emp_name)

    # Order the results
    # Equivalent to: ORDER BY name ASC
    return sorted(employee_names)

# Define test cases
# Each test case includes input data (simulating tables) and the expected output list
test_cases = [
    {
        'name': 'Test Case 1: Basic Join and Filter',
        'input': {
            'employees': [
                (1, 'Alice', 101, 70000),
                (2, 'Bob', 102, 80000),
                (3, 'Charlie', 101, 60000),
                (4, 'David', 103, 90000),
            ],
            'departments': [
                (101, 'Engineering'),
                (102, 'Sales'),
                (103, 'Marketing'),
            ],
            'target_department': 'Engineering'
        },
        'expected_output': ['Alice', 'Charlie']
    },
    {
        'name': 'Test Case 2: Different Department',
        'input': {
            'employees': [
                (1, 'Alice', 101, 70000),
                (2, 'Bob', 102, 80000),
                (3, 'Charlie', 101, 60000),
                (4, 'David', 103, 90000),
            ],
            'departments': [
                (101, 'Engineering'),
                (102, 'Sales'),
                (103, 'Marketing'),
            ],
            'target_department': 'Sales'
        },
        'expected_output': ['Bob']
    },
    {
        'name': 'Test Case 3: Department Not Found',
        'input': {
            'employees': [
                (1, 'Alice', 101, 70000),
            ],
            'departments': [
                (101, 'Engineering'),
            ],
            'target_department': 'HR' # Department 'HR' does not exist
        },
        'expected_output': []
    },
    {
        'name': 'Test Case 4: No Employees in Department',
        'input': {
            'employees': [
                (1, 'Alice', 101, 70000),
                (2, 'Bob', 102, 80000),
            ],
            'departments': [
                (101, 'Engineering'),
                (102, 'Sales'),
                (103, 'Marketing'), # Exists but no employees assigned
            ],
            'target_department': 'Marketing'
        },
        'expected_output': []
    },
    {
        'name': 'Test Case 5: Empty Employees Table',
        'input': {
            'employees': [],
            'departments': [
                (101, 'Engineering'),
            ],
            'target_department': 'Engineering'
        },
        'expected_output': []
    },
    {
        'name': 'Test Case 6: Empty Departments Table',
        'input': {
            'employees': [
                 (1, 'Alice', 101, 70000),
            ],
            'departments': [],
            'target_department': 'Engineering' # Cannot find department ID
        },
        'expected_output': []
    },
     {
        'name': 'Test Case 7: Multiple employees in target department',
        'input': {
            'employees': [
                (1, 'Eve', 104, 55000),
                (5, 'Frank', 104, 65000),
                (6, 'Grace', 104, 75000),
                 (2, 'Bob', 102, 80000),
            ],
            'departments': [
                (104, 'Support'),
                (102, 'Sales'),
            ],
            'target_department': 'Support'
        },
        'expected_output': ['Eve', 'Frank', 'Grace'] # Should be sorted
    },
]

# Runner function to execute tests
def run_tests(test_cases):
    correct_count = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        inputs = test_case['input']
        expected = test_case['expected_output']

        # Call the function under test
        actual = solve_sql_problem(
            inputs['employees'],
            inputs['departments'],
            inputs['target_department']
        )

        # The function guarantees sorted output, and expected is sorted too.
        if actual == expected:
            print(f"True")
            correct_count += 1
        else:
            # Detailed failure output (optional, normally just print False)
            # print(f"Test Case {i+1} ({test_case['name']}) Failed:")
            # print(f"  Input: {inputs}")
            # print(f"  Expected: {expected}")
            # print(f"  Actual: {actual}")
            print(f"False")

    print(f"{correct_count}/{total_tests}")

# Execute the tests
if __name__ == "__main__":
    run_tests(test_cases)