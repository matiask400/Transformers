def solve():
    def get_employee_department_names(employees_data, departments_data):
        department_map = {dept['deptId']: dept['name'] for dept in departments_data}
        employee_department_list = []
        for emp in employees_data:
            if emp['deptId'] in department_map:
                employee_department_list.append((emp['name'], department_map[emp['deptId']]))
        return employee_department_list

    employees_table_data = [
        {'empId': 1, 'name': 'Alice', 'deptId': 1},
        {'empId': 2, 'name': 'Bob', 'deptId': 1},
        {'empId': 3, 'name': 'Charlie', 'deptId': 2},
        {'empId': 4, 'name': 'David', 'deptId': 2},
        {'empId': 5, 'name': 'Eve', 'deptId': 3}
    ]

    departments_table_data = [
        {'deptId': 1, 'name': 'HR'},
        {'deptId': 2, 'name': 'Engineering'},
        {'deptId': 3, 'name': 'Sales'},
        {'deptId': 4, 'name': 'Marketing'}
    ]

    test_cases = [
        {
            'input_employees': employees_table_data,
            'input_departments': departments_table_data,
            'expected_output': [
                ('Alice', 'HR'),
                ('Bob', 'HR'),
                ('Charlie', 'Engineering'),
                ('David', 'Engineering'),
                ('Eve', 'Sales')
            ],
            'test_name': 'Test Case 1: Basic Join'
        },
        {
            'input_employees': employees_table_data[:2],
            'input_departments': departments_table_data[:2],
            'expected_output': [
                ('Alice', 'HR'),
                ('Bob', 'HR'),
            ],
            'test_name': 'Test Case 2: Subset of Employees and Departments'
        },
         {
            'input_employees': [],
            'input_departments': departments_table_data,
            'expected_output': [],
            'test_name': 'Test Case 3: No Employees'
        },
        {
            'input_employees': employees_table_data,
            'input_departments': [],
            'expected_output': [],
            'test_name': 'Test Case 4: No Departments'
        },
        {
            'input_employees': [{'empId': 6, 'name': 'Frank', 'deptId': 5}],
            'input_departments': departments_table_data,
            'expected_output': [],
            'test_name': 'Test Case 5: Employee with non-existent deptId'
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for test_case in test_cases:
        actual_output = get_employee_department_names(test_case['input_employees'], test_case['input_departments'])
        if actual_output == test_case['expected_output']:
            print('True')
            correct_tests += 1
        else:
            print('False')
        # For debugging purposes (optional):
        # print(f"Test: {test_case['test_name']}")
        # print(f"Expected: {test_case['expected_output']}")
        # print(f"Actual:   {actual_output}")
        # print("-" * 20)

    print(f"{correct_tests}/{total_tests}")

solve()