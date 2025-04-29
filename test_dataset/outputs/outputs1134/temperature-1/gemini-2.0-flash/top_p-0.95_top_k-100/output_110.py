def solve():
    test_cases = [
        {
            "input": "SELECT * FROM employees WHERE department = 'Sales' AND salary > 60000;",
            "expected_output": "SELECT * FROM employees WHERE department = 'Sales' AND salary > 60000;"
        },
        {
            "input": "SELECT name, age FROM students WHERE major = 'Computer Science' ORDER BY age DESC;",
            "expected_output": "SELECT name, age FROM students WHERE major = 'Computer Science' ORDER BY age DESC;"
        },
        {
            "input": "SELECT COUNT(*) FROM orders WHERE order_date BETWEEN '2023-01-01' AND '2023-01-31';",
            "expected_output": "SELECT COUNT(*) FROM orders WHERE order_date BETWEEN '2023-01-01' AND '2023-01-31';"
        },
        {
            "input": "SELECT product_name, AVG(price) FROM products GROUP BY product_name HAVING AVG(price) > 50;",
            "expected_output": "SELECT product_name, AVG(price) FROM products GROUP BY product_name HAVING AVG(price) > 50;"
        },
        {
            "input": "SELECT e.employee_id, e.name, d.department_name FROM employees e JOIN departments d ON e.department_id = d.department_id WHERE d.location = 'New York';",
            "expected_output": "SELECT e.employee_id, e.name, d.department_name FROM employees e JOIN departments d ON e.department_id = d.department_id WHERE d.location = 'New York';"
        }
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, test_case in enumerate(test_cases):
        input_sql = test_case["input"]
        expected_output = test_case["expected_output"]

        # In this simplified example, the solution just returns the input
        actual_output = input_sql 

        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")

    print(f"{correct_count}/{total_count}")

solve()