import sqlite3
import sys
import io

# Define the SQL schema and initial data
# NOTE: No schema was provided in the prompt. Using a placeholder schema (Employees, Departments)
#       for demonstration purposes. Replace this with the actual schema if provided.
SCHEMA_AND_DATA = """
DROP TABLE IF EXISTS Departments;
DROP TABLE IF EXISTS Employees;

CREATE TABLE Departments (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE Employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary INTEGER,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES Departments(id)
);

INSERT INTO Departments (id, name) VALUES
(1, 'HR'),
(2, 'Engineering'),
(3, 'Sales'),
(4, 'Marketing');

INSERT INTO Employees (id, name, salary, department_id) VALUES
(101, 'Alice', 70000, 2),
(102, 'Bob', 55000, 1),
(103, 'Charlie', 80000, 2),
(104, 'David', 60000, 3),
(105, 'Eve', 75000, 2),
(106, 'Frank', 50000, 1),
(107, 'Grace', 65000, 3),
(108, 'Heidi', 90000, 4); 
"""

def run_sql_test(query: str, expected_result: list) -> bool:
    """
    Runs a given SQL query against an in-memory SQLite database populated
    with the predefined schema and data, and compares the result.

    Args:
        query: The SQL query string to execute.
        expected_result: A list of tuples representing the expected rows.

    Returns:
        True if the actual result matches the expected result (order insensitive),
        False otherwise.
    """
    # Redirect stdout to capture potential print statements from within the function
    # (although good practice is to avoid them in library-like functions)
    # This is mainly to ensure only 'True'/'False' are printed by the runner.
    original_stdout = sys.stdout
    sys.stdout = io.StringIO() # Capture stdout

    conn = None # Initialize conn to None
    passed = False
    try:
        # Create an in-memory database
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()

        # Apply the schema and insert data
        cursor.executescript(SCHEMA_AND_DATA)
        conn.commit()

        # Execute the provided query
        cursor.execute(query)
        actual_result = cursor.fetchall()

        # Sort both actual and expected results for order-insensitive comparison
        # Convert results to sets of tuples for robust comparison if duplicates are not expected
        # or sort if duplicates/order might matter conceptually but not for the specific test comparison logic
        # Here we sort, which handles duplicates correctly.
        actual_result_sorted = sorted(actual_result)
        expected_result_sorted = sorted(expected_result)

        # Compare the results
        if actual_result_sorted == expected_result_sorted:
            passed = True
        else:
            # Optional: Print detailed differences for debugging
            # print(f"\nQuery: {query}")
            # print(f"Expected: {expected_result_sorted}")
            # print(f"Actual:   {actual_result_sorted}")
            passed = False

    except sqlite3.Error as e:
        # Restore stdout before printing error
        sys.stdout = original_stdout
        print(f"SQL Error executing query:\n{query}\nError: {e}", file=sys.stderr)
        passed = False
    except Exception as e:
         # Restore stdout before printing error
        sys.stdout = original_stdout
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        passed = False
    finally:
        if conn:
            conn.close()
        # Restore stdout and print result
        sys.stdout = original_stdout
        print(str(passed)) # Print 'True' or 'False'

    return passed

def run_tests(test_cases: list):
    """
    Runs a series of SQL tests.

    Args:
        test_cases: A list of tuples, where each tuple contains:
                    (test_name: str, query: str, expected_result: list)
    """
    correct_count = 0
    total_tests = len(test_cases)

    for i, (test_name, query, expected_result) in enumerate(test_cases):
        # print(f"--- Running Test {i+1}: {test_name} ---") # Optional: more verbose output
        if run_sql_test(query, expected_result):
            correct_count += 1
        # print("-" * (len(test_name) + 22)) # Optional: separator

    print(f"{correct_count}/{total_tests} correct tests.")

# --- Define Test Cases ---
# Each test case is a tuple: (test_name, sql_query, expected_result_list)
# expected_result_list should be a list of tuples, where each tuple represents a row.

TEST_CASES = [
    (
        "Select all employees",
        "SELECT id, name, salary, department_id FROM Employees ORDER BY id;",
        [
            (101, 'Alice', 70000, 2),
            (102, 'Bob', 55000, 1),
            (103, 'Charlie', 80000, 2),
            (104, 'David', 60000, 3),
            (105, 'Eve', 75000, 2),
            (106, 'Frank', 50000, 1),
            (107, 'Grace', 65000, 3),
            (108, 'Heidi', 90000, 4)
        ]
    ),
    (
        "Select employees with salary > 70000",
        "SELECT name, salary FROM Employees WHERE salary > 70000 ORDER BY name;",
        [
            ('Charlie', 80000),
            ('Eve', 75000),
            ('Heidi', 90000)
        ]
    ),
    (
        "Select employees in Engineering department",
        "SELECT E.name FROM Employees E JOIN Departments D ON E.department_id = D.id WHERE D.name = 'Engineering';",
        [('Alice',), ('Charlie',), ('Eve',)] # Order doesn't matter for correctness here, sorting handles it
    ),
    (
        "Count employees per department",
        """
        SELECT D.name, COUNT(E.id)
        FROM Departments D
        LEFT JOIN Employees E ON D.id = E.department_id
        GROUP BY D.name
        ORDER BY D.name;
        """,
        [
            ('Engineering', 3),
            ('HR', 2),
            ('Marketing', 1),
            ('Sales', 2)
        ]
    ),
    (
        "Find department with highest average salary",
        """
        SELECT D.name -- , AVG(E.salary) AS avg_sal -- Including avg_sal makes expected result clearer
        FROM Employees E
        JOIN Departments D ON E.department_id = D.id
        GROUP BY D.name
        ORDER BY AVG(E.salary) DESC
        LIMIT 1;
        """,
        [('Marketing',)] # Heidi is the only one in Marketing, avg is 90000
                         # Engineering avg: (70+80+75)/3 = 75000
                         # HR avg: (55+50)/2 = 52500
                         # Sales avg: (60+65)/2 = 62500
    ),
     (
        "Find employees not in HR",
        """
        SELECT E.name
        FROM Employees E
        JOIN Departments D ON E.department_id = D.id
        WHERE D.name != 'HR';
        """,
         [('Alice',), ('Charlie',), ('David',), ('Eve',), ('Grace',), ('Heidi',)]
     ),
     (
         "Empty result set test",
         "SELECT name FROM Employees WHERE salary > 100000;",
         []
     ),
     (
        "Simple Select from Departments",
        "SELECT name FROM Departments WHERE id = 3;",
        [('Sales',)]
     )
    # Add more test cases here if needed
]

# --- Main Execution ---
if __name__ == "__main__":
    # You can add command line argument parsing here if needed
    # For now, just run the predefined tests
    run_tests(TEST_CASES)