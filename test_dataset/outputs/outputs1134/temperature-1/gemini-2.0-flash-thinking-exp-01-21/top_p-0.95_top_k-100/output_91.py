def solve():
    def test_sql_query(schema, query, expected_output):
        def simulate_query(schema, query):
            query = query.strip().lower()
            if query.startswith("select"):
                parts = query.split(" from ")
                select_clause = parts[0].split("select ")[1].strip()
                from_clause_parts = parts[1].split(" where ")
                table_name = from_clause_parts[0].strip()
                where_clause = from_clause_parts[1].strip() if len(from_clause_parts) > 1 else None

                if table_name not in schema:
                    return "Error: Table not found"

                table_data = schema[table_name]['data']
                columns = schema[table_name]['columns']

                selected_indices = []
                if select_clause == "*":
                    selected_indices = list(range(len(columns)))
                else:
                    select_cols = [col.strip() for col in select_clause.split(',')]
                    for col in select_cols:
                        if col not in columns:
                            return "Error: Column not found"
                        selected_indices.append(columns.index(col))

                filtered_data = table_data
                if where_clause:
                    condition_parts = where_clause.split("=")
                    where_col = condition_parts[0].strip()
                    where_value = condition_parts[1].strip().replace("'", "")

                    if where_col not in columns:
                        return "Error: Where column not found"
                    where_col_index = columns.index(where_col)

                    filtered_data = []
                    for row in table_data:
                        if str(row[where_col_index]) == where_value: # Simple string comparison
                            filtered_data.append(row)

                result = []
                for row in filtered_data:
                    selected_row = tuple(row[i] for i in selected_indices)
                    result.append(selected_row)
                return result
            else:
                return "Error: Unsupported query type"

        actual_output = simulate_query(schema, query)

        if actual_output == expected_output:
            print("True")
            return True
        else:
            print("False")
            print(f"  Expected: {expected_output}")
            print(f"  Actual:   {actual_output}")
            return False

    schema = {
        "Employees": {
            "columns": ["emp_id", "emp_name", "salary", "dept_id"],
            "data": [
                (1, 'Alice', 60000, 1),
                (2, 'Bob', 55000, 1),
                (3, 'Charlie', 70000, 2),
                (4, 'David', 65000, 2)
            ]
        },
        "Departments": {
            "columns": ["dept_id", "dept_name"],
            "data": [
                (1, 'Sales'),
                (2, 'Marketing')
            ]
        }
    }

    test_cases = [
        {
            "query": "SELECT emp_name FROM Employees WHERE dept_id = 1",
            "expected_output": [('Alice',), ('Bob',)]
        },
        {
            "query": "SELECT emp_name FROM Employees WHERE dept_id = 2",
            "expected_output": [('Charlie',), ('David',)]
        },
        {
            "query": "SELECT dept_name FROM Departments WHERE dept_id = 1",
            "expected_output": [('Sales',)]
        },
        {
            "query": "SELECT dept_name FROM Departments WHERE dept_id = 2",
            "expected_output": [('Marketing',)]
        },
        {
            "query": "SELECT emp_name, salary FROM Employees WHERE dept_id = 1",
            "expected_output": [('Alice', 60000), ('Bob', 55000)]
        },
        {
            "query": "SELECT * FROM Employees WHERE dept_id = 2",
            "expected_output": [(3, 'Charlie', 70000, 2), (4, 'David', 65000, 2)]
        },
        {
            "query": "SELECT * FROM Departments WHERE dept_id = 1",
            "expected_output": [(1, 'Sales')]
        },
        {
            "query": "SELECT emp_id FROM Employees WHERE dept_id = 3",
            "expected_output": []
        }

    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for test_case in test_cases:
        if test_sql_query(schema, test_case["query"], test_case["expected_output"]):
            correct_tests += 1

    print(f"Correct tests: {correct_tests}/{total_tests}")

solve()