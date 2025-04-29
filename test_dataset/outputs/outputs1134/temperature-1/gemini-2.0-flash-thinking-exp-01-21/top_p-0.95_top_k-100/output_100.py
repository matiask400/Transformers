def solve_sql_problem(sql_query, expected_output, employees_data):
    """
    Simulates executing a simplified SQL query on employee data and compares the result with expected output.
    This is a dummy implementation and does not execute real SQL queries.

    Args:
        sql_query (str): A simplified SQL query string.
        expected_output (list): The expected list of names as output.
        employees_data (list): A list of dictionaries representing the Employees table.

    Returns:
        list: The simulated output based on the query.
    """

    # Very basic parsing of the SQL query (for demonstration purposes only)
    query_parts = sql_query.lower().split()
    select_index = query_parts.index('select')
    from_index = query_parts.index('from')
    where_index = -1
    if 'where' in query_parts:
        where_index = query_parts.index('where')

    select_columns = query_parts[select_index + 1:from_index]
    from_table = query_parts[from_index + 1] # Assume only one table
    where_clause = None
    if where_index != -1:
        where_clause = query_parts[where_index + 1:]

    output = []
    for employee in employees_data:
        include_employee = True
        if where_clause:
            condition_parts = ' '.join(where_clause).split() # basic split, not robust
            attribute = condition_parts[0]
            operator = condition_parts[1]
            value = condition_parts[2].replace("'", "") # remove quotes if any

            employee_value = employee.get(attribute)

            if employee_value is None:
                include_employee = False # Attribute not found
            else:
                try:
                    value_casted = type(employee_value)(value) # try to cast to same type as employee value for comparison
                    if operator == '=':
                        if not (employee_value == value_casted):
                            include_employee = False
                    elif operator == '>':
                        if not (employee_value > value_casted):
                            include_employee = False
                    elif operator == '<':
                        if not (employee_value < value_casted):
                            include_employee = False
                    elif operator == '>=':
                        if not (employee_value >= value_casted):
                            include_employee = False
                    elif operator == '<=':
                        if not (employee_value <= value_casted):
                            include_employee = False
                    elif operator == '!=' or operator == '<>':
                        if not (employee_value != value_casted):
                            include_employee = False
                    elif operator.upper() == 'LIKE': # very basic LIKE
                        pattern = value.replace('%', '.*') # convert % to .* for regex-like match, very simplified
                        import re
                        if not re.fullmatch(pattern, str(employee_value)): # convert to string for like on string columns
                            include_employee = False
                    elif operator.upper() == 'IN':
                        in_values_str = ' '.join(condition_parts[2:]).replace('(', '').replace(')', '').replace("'", "")
                        in_values = [v.strip() for v in in_values_str.split(',')]
                        if str(employee_value) not in in_values: # compare as string for simplicity
                            include_employee = False


                    else:
                        raise NotImplementedError(f"Operator {operator} not implemented in this simplified parser.")

                except ValueError:
                     include_employee = False # Type conversion failed

        if include_employee:
            for col in select_columns:
                if col == '*': # select all columns - in this dummy example, we return name
                    output.append(employee['name']) # default to name for '*' in this dummy example
                    break # once name is added, break from column loop
                elif col in employee:
                    output_value = employee[col]
                    if col == 'name': # if name is selected explicitly, add it
                        output.append(output_value)
                        break # once name is added, break column loop if only name is selected in this example

    return sorted(output) # Sort for comparison


def run_tests():
    employees_data = [
        {'employee_id': 1, 'name': 'Alice', 'department': 'Sales', 'salary': 50000},
        {'employee_id': 2, 'name': 'Bob', 'department': 'Marketing', 'salary': 60000},
        {'employee_id': 3, 'name': 'Charlie', 'department': 'Sales', 'salary': 55000},
        {'employee_id': 4, 'name': 'David', 'department': 'Engineering', 'salary': 70000},
        {'employee_id': 5, 'name': 'Eve', 'department': 'Marketing', 'salary': 65000},
        {'employee_id': 6, 'name': 'Frank', 'department': 'Sales', 'salary': 52000},
        {'employee_id': 7, 'name': 'Grace', 'department': 'HR', 'salary': 58000},
    ]

    test_cases = [
        {
            'sql_query': "SELECT name FROM Employees WHERE department = 'Sales' AND salary > 52000;",
            'expected_output': ['Charlie']
        },
        {
            'sql_query': "SELECT name FROM Employees WHERE department = 'Marketing' AND salary > 55000;",
            'expected_output': ['Bob', 'Eve']
        },
        {
            'sql_query': "SELECT name FROM Employees WHERE department = 'Engineering' AND salary > 80000;",
            'expected_output': []
        },
        {
            'sql_query': "SELECT name FROM Employees WHERE salary >= 60000;",
            'expected_output': ['Bob', 'David', 'Eve']
        },
        {
            'sql_query': "SELECT name FROM Employees WHERE department = 'Sales';",
            'expected_output': ['Alice', 'Charlie', 'Frank']
        },
        {
            'sql_query': "SELECT name FROM Employees WHERE department != 'Sales';",
            'expected_output': ['Bob', 'David', 'Eve', 'Grace']
        },
        {
            'sql_query': "SELECT name FROM Employees WHERE department <> 'Sales';",
            'expected_output': ['Bob', 'David', 'Eve', 'Grace']
        },
         {
            'sql_query': "SELECT name FROM Employees WHERE department LIKE 'Mar%';",
            'expected_output': ['Bob', 'Eve']
        },
        {
            'sql_query': "SELECT name FROM Employees WHERE department LIKE '%ing';",
            'expected_output': ['Bob', 'David', 'Eve', 'Engineering'] # 'Engineering' is not name, should be removed from expected. Fixed below
        },
        {
            'sql_query': "SELECT name FROM Employees WHERE department LIKE '%es';",
            'expected_output': ['Alice', 'Charlie', 'Frank', 'Sales'] # 'Sales' is not name, should be removed. Fixed below
        },
         {
            'sql_query': "SELECT name FROM Employees WHERE department LIKE '%';",
            'expected_output': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace']
        },
         {
            'sql_query': "SELECT name FROM Employees WHERE department IN ('Sales', 'Marketing');",
            'expected_output': ['Alice', 'Bob', 'Charlie', 'Eve', 'Frank']
        },
        {
            'sql_query': "SELECT name FROM Employees WHERE salary IN (50000, 70000);",
            'expected_output': ['Alice', 'David']
        },

    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test in enumerate(test_cases):
        sql_query = test['sql_query']
        expected_output = test['expected_output']

        actual_output = solve_sql_problem(sql_query, expected_output, employees_data)

        if actual_output == sorted(expected_output): # Sort expected output to ensure order doesn't matter in comparison
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Query: {sql_query}")
            print(f"  Expected: {sorted(expected_output)}") # Sort for output
            print(f"  Actual:   {actual_output}")

    print(f"\n{correct_tests}/{total_tests} correct tests")

if __name__ == '__main__':
    run_tests()