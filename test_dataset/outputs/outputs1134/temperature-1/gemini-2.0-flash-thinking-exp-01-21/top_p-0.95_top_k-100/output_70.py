import sqlite3

def solve_sql_problem(sql_query, expected_output):
    """
    Executes the given SQL query against an in-memory database with a predefined schema and data,
    compares the result with the expected output, and returns True if they match, False otherwise.

    Args:
        sql_query (str): The SQL query to execute.
        expected_output (list of tuples): The expected output of the SQL query as a list of tuples.

    Returns:
        bool: True if the query output matches the expected output, False otherwise.
    """
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Create a sample table (assuming a simple schema for demonstration)
    cursor.execute('''
        CREATE TABLE Employees (
            EmployeeID INTEGER PRIMARY KEY,
            FirstName VARCHAR(255),
            LastName VARCHAR(255),
            Department VARCHAR(255)
        )
    ''')

    # Insert sample data
    cursor.execute("INSERT INTO Employees (EmployeeID, FirstName, LastName, Department) VALUES (1, 'John', 'Doe', 'Sales')")
    cursor.execute("INSERT INTO Employees (EmployeeID, FirstName, LastName, Department) VALUES (2, 'Jane', 'Smith', 'Marketing')")
    cursor.execute("INSERT INTO Employees (EmployeeID, FirstName, LastName, Department) VALUES (3, 'Robert', 'Jones', 'Sales')")
    cursor.execute("INSERT INTO Employees (EmployeeID, FirstName, LastName, Department) VALUES (4, 'Linda', 'Williams', 'Engineering')")
    conn.commit()

    try:
        cursor.execute(sql_query)
        query_result = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"SQL query error: {e}")
        return False
    finally:
        conn.close()

    return query_result == expected_output

def run_tests():
    """
    Runs a series of test cases for the solve_sql_problem function and prints the results.
    """
    test_cases = [
        {
            'query': "SELECT FirstName, LastName FROM Employees WHERE Department = 'Sales'",
            'expected_output': [('John', 'Doe'), ('Robert', 'Jones')]
        },
        {
            'query': "SELECT COUNT(*) FROM Employees WHERE Department = 'Marketing'",
            'expected_output': [(1,)]
        },
        {
            'query': "SELECT Department FROM Employees GROUP BY Department",
            'expected_output': [('Engineering',), ('Marketing',), ('Sales',)]
        },
        {
            'query': "SELECT FirstName FROM Employees WHERE EmployeeID = 5", # EmployeeID 5 does not exist
            'expected_output': []
        },
        {
            'query': "SELECT * FROM Employees ORDER BY LastName",
            'expected_output': [(1, 'John', 'Doe', 'Sales'), (2, 'Jane', 'Smith', 'Marketing'), (4, 'Linda', 'Williams', 'Engineering'), (3, 'Robert', 'Jones', 'Sales')]
        },
         {
            'query': "SELECT EmployeeID, FirstName FROM Employees WHERE Department = 'Sales' ORDER BY FirstName DESC",
            'expected_output': [(3, 'Robert'), (1, 'John')]
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        query = test_case['query']
        expected = test_case['expected_output']
        result = solve_sql_problem(query, expected)
        if result:
            print(f'Test {i+1}: True')
            correct_tests += 1
        else:
            print(f'Test {i+1}: False')
            print(f"  Query: {query}")
            print(f"  Expected: {expected}")
            # Optionally print the actual output for debugging if needed
            conn = sqlite3.connect(':memory:')
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE Employees (
                    EmployeeID INTEGER PRIMARY KEY,
                    FirstName VARCHAR(255),
                    LastName VARCHAR(255),
                    Department VARCHAR(255)
                )
            ''')
            cursor.execute("INSERT INTO Employees (EmployeeID, FirstName, LastName, Department) VALUES (1, 'John', 'Doe', 'Sales')")
            cursor.execute("INSERT INTO Employees (EmployeeID, FirstName, LastName, Department) VALUES (2, 'Jane', 'Smith', 'Marketing')")
            cursor.execute("INSERT INTO Employees (EmployeeID, FirstName, LastName, Department) VALUES (3, 'Robert', 'Jones', 'Sales')")
            cursor.execute("INSERT INTO Employees (EmployeeID, FirstName, LastName, Department) VALUES (4, 'Linda', 'Williams', 'Engineering')")
            conn.commit()
            cursor.execute(query)
            actual_output = cursor.fetchall()
            conn.close()

            print(f"  Actual: {actual_output}")


    print(f"\n{correct_tests} correct tests over {total_tests}")

if __name__ == '__main__':
    run_tests()