import sqlite3
import sys
import os

def run_sql_tests(db_name, setup_sqls, test_cases):
    """
    Connects to an SQLite database, sets up the schema, runs SQL test queries,
    and compares the results against expected outputs.

    Args:
        db_name (str): The name of the SQLite database file (e.g., ':memory:' for
                       in-memory, or 'mydatabase.db' for a file).
                       If a file exists, it will be overwritten.
        setup_sqls (list): A list of SQL strings to execute for creating tables
                           and inserting initial data.
        test_cases (list): A list of dictionaries, where each dictionary represents
                           a test case and contains:
                           - 'description' (str): A brief description of the test.
                           - 'query' (str): The SQL query to execute.
                           - 'expected' (list): A list of tuples representing the
                                                expected rows in the result set.
                                                Order might matter depending on the query
                                                (e.g., if ORDER BY is used).
    """
    passed_count = 0
    total_count = len(test_cases)
    conn = None  # Initialize connection variable

    # Ensure a clean slate if using a file-based database
    if db_name != ':memory:' and os.path.exists(db_name):
        try:
            os.remove(db_name)
        except OSError as e:
            print(f"Error removing existing database file {db_name}: {e}", file=sys.stderr)
            # Decide if this is fatal or not. For testing, usually want a clean start.
            return # Exit if we can't ensure a clean DB file

    try:
        # Connect to the database (in-memory or file)
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # --- Setup Phase ---
        print("--- Setting up database schema and data ---")
        try:
            # Use executescript for potentially multiple statements in one string,
            # or iterate if setup_sqls contains separate statements.
            # Iterating is generally safer.
            for sql in setup_sqls:
                 # Allow multiple statements separated by ';' within one string if needed
                cursor.executescript(sql)
            conn.commit() # Commit setup changes
            print("--- Database setup complete ---")
        except sqlite3.Error as e:
            print(f"!!! Database setup failed: {e}", file=sys.stderr)
            print("!!! Aborting tests.", file=sys.stderr)
            if conn:
                conn.close()
            return # Exit the function if setup fails

        # --- Testing Phase ---
        print("\n--- Running Tests ---")
        for i, test in enumerate(test_cases):
            description = test.get('description', f'Test {i+1}')
            query = test.get('query', None)
            expected_raw = test.get('expected', None)

            print(f"\n--- {description} ---")

            if query is None or expected_raw is None:
                 print(f"Error: Test case missing 'query' or 'expected' key.")
                 print("False")
                 continue # Skip to next test

            if not isinstance(expected_raw, list):
                 print(f"Error: Expected output must be a list of tuples. Found type: {type(expected_raw)}")
                 print("False")
                 continue # Skip to next test

            # Ensure expected is a list of tuples for consistent comparison
            try:
                expected = [tuple(row) for row in expected_raw]
            except TypeError:
                 print(f"Error: Elements within the 'expected' list could not be converted to tuples.")
                 print("False")
                 continue # Skip to next test

            print(f"Query:\n{query.strip()}")

            try:
                cursor.execute(query)
                # Fetch results - fetchall() returns list of tuples
                actual_results_raw = cursor.fetchall()

                # Convert actual results to list of tuples (usually already is, but ensures consistency)
                actual_results = [tuple(row) for row in actual_results_raw]

                # --- Comparison ---
                # We will perform two types of comparisons:
                # 1. Direct comparison (order matters)
                # 2. Sorted comparison (order doesn't matter)
                # A test passes if EITHER the direct comparison passes OR the sorted comparison passes.
                # This handles cases with and without ORDER BY clauses appropriately in most scenarios.
                # More sophisticated logic could inspect the query for ORDER BY.

                direct_match = actual_results == expected
                # Sort both lists only if they are non-empty and comparable
                # (avoid sorting lists containing types that cannot be compared, though unlikely with SQL results)
                sorted_match = False
                try:
                     # Check if both lists contain tuples before attempting sort + compare
                     # all() handles empty lists correctly (returns True)
                     can_sort_actual = all(isinstance(item, tuple) for item in actual_results)
                     can_sort_expected = all(isinstance(item, tuple) for item in expected)

                     if can_sort_actual and can_sort_expected:
                          sorted_match = sorted(actual_results) == sorted(expected)
                     elif len(actual_results) == 0 and len(expected) == 0:
                          # Handle empty lists explicitly if sorting approach had issues
                           sorted_match = True


                except TypeError as te:
                    # This might happen if rows contain complex types that are not comparable
                    print(f"  Warning: Could not sort results for comparison: {te}")
                    sorted_match = False # Cannot rely on sorted comparison

                # Test passes if either direct or sorted comparison is true
                comparison_passed = direct_match or sorted_match

                if comparison_passed:
                    print("True")
                    passed_count += 1
                else:
                    print("False")
                    print(f"  Expected: {expected}")
                    print(f"  Actual:   {actual_results}")
                    # Optionally show why it failed (direct vs sorted)
                    if not direct_match and sorted_match:
                        print("  (Note: Passed only with sorted comparison - order difference)")
                    elif not direct_match and not sorted_match:
                         print("  (Note: Failed both direct and sorted comparison - content difference)")


            except sqlite3.Error as e:
                # Errors during query execution (syntax, runtime like constraint violation)
                print("False")
                print(f"  SQL Error: {e}")
            except Exception as e:
                # Catch other potential Python errors during processing/comparison
                print("False")
                print(f"  Python Error: {e}")

    except sqlite3.Error as e:
        # Error during connection or initial cursor creation
        print(f"!!! Database connection/cursor error: {e}", file=sys.stderr)
    finally:
        # --- Cleanup Phase ---
        if conn:
            conn.close()
            # print("\n--- Database connection closed ---")
            # Clean up the database file if it wasn't in-memory
            # if db_name != ':memory:' and os.path.exists(db_name):
            #     try:
            #         # Uncomment below if you want the db file deleted after tests
            #         # os.remove(db_name)
            #         # print(f"--- Database file {db_name} removed ---")
            #         pass
            #     except OSError as e:
            #         print(f"Warning: Could not remove database file {db_name}: {e}", file=sys.stderr)


    # --- Summary ---
    print("\n" + "=" * 30)
    print(f" Test Execution Summary")
    print("-" * 30)
    print(f" Passed: {passed_count}")
    print(f" Failed: {total_count - passed_count}")
    print(f" Total:  {total_count}")
    print(f" Score:  {passed_count} / {total_count}")
    print("=" * 30)

# ==============================================================================
# EXAMPLE USAGE: Define Schema and Tests
# ==============================================================================

# --- Define Schema Setup SQL ---
# NOTE: The original prompt did not provide a schema, so we use a sample one.
#       Replace this with the actual schema provided by the specific problem.
schema_definition_sql = [
    """
    -- Create Employees Table
    CREATE TABLE Employees (
        employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        department_id INTEGER,
        salary REAL CHECK(salary > 0),
        hire_date DATE
    );
    """,
    """
    -- Create Departments Table
    CREATE TABLE Departments (
        department_id INTEGER PRIMARY KEY,
        department_name TEXT NOT NULL UNIQUE
    );
    """,
    """
    -- Create Projects Table
    CREATE TABLE Projects (
        project_id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_name TEXT NOT NULL,
        start_date DATE,
        budget REAL
    );
    """,
    """
    -- Create EmployeeProjects Table (Many-to-Many relationship)
    CREATE TABLE EmployeeProjects (
        assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER,
        project_id INTEGER,
        role TEXT,
        FOREIGN KEY (employee_id) REFERENCES Employees (employee_id),
        FOREIGN KEY (project_id) REFERENCES Projects (project_id),
        UNIQUE (employee_id, project_id) -- An employee has one role per project
    );
    """,
    # --- Insert Sample Data ---
    """
    INSERT INTO Departments (department_id, department_name) VALUES
    (1, 'Engineering'),
    (2, 'Human Resources'),
    (3, 'Sales'),
    (4, 'Marketing');
    """,
    """
    INSERT INTO Employees (first_name, last_name, department_id, salary, hire_date) VALUES
    ('Alice', 'Smith', 1, 75000.0, '2020-05-15'),
    ('Bob', 'Johnson', 1, 80000.0, '2019-08-01'),
    ('Charlie', 'Williams', 2, 60000.0, '2021-01-20'),
    ('David', 'Brown', 3, 65000.0, '2020-11-01'),
    ('Eve', 'Davis', 1, 90000.0, '2018-03-12'),
    ('Frank', 'Miller', NULL, 50000.0, '2022-07-01'); -- No department yet
    """,
    """
    INSERT INTO Projects (project_name, start_date, budget) VALUES
    ('Alpha Project', '2023-01-10', 100000.0),
    ('Beta Initiative', '2023-06-15', 250000.0),
    ('Gamma Taskforce', '2022-11-01', 50000.0);
    """,
    """
    INSERT INTO EmployeeProjects (employee_id, project_id, role) VALUES
    (1, 1, 'Developer'),          -- Alice on Alpha
    (2, 1, 'Lead Developer'),     -- Bob on Alpha
    (5, 1, 'Architect'),          -- Eve on Alpha
    (1, 2, 'Developer'),          -- Alice on Beta
    (4, 2, 'Sales Lead'),         -- David on Beta
    (2, 3, 'Consultant');         -- Bob on Gamma
    """
]

# --- Define Test Cases ---
# Each test case is a dictionary with 'description', 'query', and 'expected' (list of tuples)
test_queries = [
    {
        "description": "Select all departments ordered by name",
        "query": "SELECT department_name FROM Departments ORDER BY department_name;",
        "expected": [
            ('Engineering',),
            ('Human Resources',),
            ('Marketing',),
            ('Sales',)
        ]
    },
    {
        "description": "Select employees in Engineering, ordered by salary desc",
        "query": """
            SELECT first_name, last_name, salary
            FROM Employees
            WHERE department_id = (SELECT department_id FROM Departments WHERE department_name = 'Engineering')
            ORDER BY salary DESC;
        """,
        "expected": [
            ('Eve', 'Davis', 90000.0),
            ('Bob', 'Johnson', 80000.0),
            ('Alice', 'Smith', 75000.0)
        ]
    },
    {
        "description": "Count employees per department (excluding NULL)",
        "query": """
            SELECT d.department_name, COUNT(e.employee_id)
            FROM Departments d
            JOIN Employees e ON d.department_id = e.department_id
            GROUP BY d.department_name
            ORDER BY d.department_name;
        """,
        "expected": [
            ('Engineering', 3),
            ('Human Resources', 1),
            ('Sales', 1)
        ]
    },
    {
        "description": "Find employees not assigned to any department",
        "query": "SELECT first_name, last_name FROM Employees WHERE department_id IS NULL;",
        "expected": [
            ('Frank', 'Miller')
        ]
    },
    {
       "description": "Calculate average salary for the entire company (approx)",
       "query": "SELECT ROUND(AVG(salary), 2) FROM Employees;",
       # Calculation: (75+80+60+65+90+50)/6 = 420/6 = 70000.00
       "expected": [(70000.0,)] # Using ROUND in query for stable float comparison
    },
    {
        "description": "List projects and the number of employees assigned (order doesn't matter)",
        "query": """
            SELECT p.project_name, COUNT(ep.employee_id)
            FROM Projects p