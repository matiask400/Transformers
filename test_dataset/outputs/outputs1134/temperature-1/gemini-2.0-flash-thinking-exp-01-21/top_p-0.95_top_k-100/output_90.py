def solve():
    def test_sql_query(sql_query, expected_output, actual_output):
        if expected_output == actual_output:
            print('True')
            return True
        else:
            print('False')
            return False

    # Test case 1
    sql_query_1 = "SELECT name FROM Employees WHERE department = 'Sales';"
    expected_output_1 = [('Alice',), ('Bob',)]
    actual_output_1 = [('Alice',), ('Bob',)]
    test_1_result = test_sql_query(sql_query_1, expected_output_1, actual_output_1)

    # Test case 2
    sql_query_2 = "SELECT name FROM Employees WHERE salary > 60000;"
    expected_output_2 = [('Bob',), ('Charlie',)]
    actual_output_2 = [('Bob',), ('Charlie',)]
    test_2_result = test_sql_query(sql_query_2, expected_output_2, actual_output_2)

    # Test case 3 (Incorrect expected output to simulate a failing test)
    sql_query_3 = "SELECT name FROM Employees WHERE department = 'Marketing';"
    expected_output_3 = [('Alice',), ('Bob',)] # Incorrect, should be [('Charlie',)]
    actual_output_3 = [('Charlie',)]
    test_3_result = test_sql_query(sql_query_3, expected_output_3, actual_output_3)

    # Test case 4
    sql_query_4 = "SELECT department, COUNT(*) FROM Employees GROUP BY department;"
    expected_output_4 = [('Sales', 2), ('Marketing', 1)]
    actual_output_4 = [('Sales', 2), ('Marketing', 1)]
    test_4_result = test_sql_query(sql_query_4, expected_output_4, actual_output_4)

    # Test case 5 (Empty result set)
    sql_query_5 = "SELECT name FROM Employees WHERE department = 'HR';"
    expected_output_5 = []
    actual_output_5 = []
    test_5_result = test_sql_query(sql_query_5, expected_output_5, actual_output_5)

    results = [test_1_result, test_2_result, test_3_result, test_4_result, test_5_result]
    correct_tests = sum(results)
    total_tests = len(results)

    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    solve()