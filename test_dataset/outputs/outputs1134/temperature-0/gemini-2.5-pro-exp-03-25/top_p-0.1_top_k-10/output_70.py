import sys
import io
import sqlite3
import pandas as pd # Using pandas for easier comparison, similar to SQL results

# --- Database Setup and Placeholder Logic ---
# In a real scenario, the solve function would likely interact with a database
# or process data structures representing tables.
# Since the specific SQL task isn't given, we'll create a placeholder
# that assumes some interaction based on input parameters.

# Let's define a placeholder function. It needs to be adapted based on the *actual* SQL problem.
# For demonstration, let's assume the task is to:
# 1. Create an in-memory SQLite database.
# 2. Execute a provided SQL query string on potentially provided data.
# 3. Return the result as a list of tuples.

def solve(db_schema_sql, data_dict, query_sql):
    """
    Executes an SQL query on an in-memory SQLite database populated with given data.

    Args:
        db_schema_sql (str): SQL string to create table(s).
                               Example: "CREATE TABLE Employees (id INT, name TEXT, salary INT);"
        data_dict (dict): A dictionary where keys are table names and values are
                          lists of tuples representing rows to insert.
                          Example: {'Employees': [(1, 'Alice', 70000), (2, 'Bob', 80000)]}
        query_sql (str): The SQL query to execute. Example: "SELECT name FROM Employees WHERE salary > 75000;"

    Returns:
        list: A list of tuples representing the query result, sorted for consistent comparison.
              Returns None or raises an exception on error.
    """
    conn = None
    try:
        # Create an in-memory database
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()

        # Create table(s)
        if db_schema_sql:
             # Allow multiple statements for schema creation if needed
            cursor.executescript(db_schema_sql)

        # Insert data
        if data_dict:
            for table_name, rows in data_dict.items():
                if rows:
                    # Assuming the number of columns matches the schema
                    num_columns = len(rows[0])
                    placeholders = ', '.join(['?'] * num_columns)
                    insert_sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
                    cursor.executemany(insert_sql, rows)

        # Execute the main query
        cursor.execute(query_sql)
        results = cursor.fetchall()

        # Sort results for consistent testing comparison
        # Convert rows to tuples (if not already) and sort
        results = sorted([tuple(row) for row in results])

        conn.commit()
        return results

    except sqlite3.Error as e:
        print(f"SQLite error: {e}", file=sys.stderr)
        # Optionally re-raise or return a specific error indicator
        # raise # Re-raise the exception
        return f"Error: {e}" # Return error message for testing comparison
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        # raise
        return f"Error: {e}"
    finally:
        if conn:
            conn.close()


# --- Testing Framework ---

def run_tests(test_cases):
    """Runs the test cases against the solve function."""
    correct_count = 0
    total_count = len(test_cases)

    for i, test_case in enumerate(test_cases):
        # Extract inputs for the solve function
        schema = test_case["input"].get("db_schema_sql", "")
        data = test_case["input"].get("data_dict", {})
        query = test_case["input"].get("query_sql", "")
        expected = test_case.get("expected")

        # Ensure expected is always a list of tuples and sorted for comparison
        if isinstance(expected, list):
             expected = sorted([tuple(row) for row in expected])
        # Handle cases where expected might be an error string
        elif isinstance(expected, str) and expected.startswith("Error:"):
             pass # Keep as string for comparison
        else: # Default if expected format is wrong
             expected = []


        print(f"--- Test {i+1} ---")
        print(f"Schema: {schema}")
        print(f"Data: {data}")
        print(f"Query: {query}")
        print(f"Expected: {expected}")

        actual = "Execution Error" # Default message if solve fails badly
        result = False
        try:
            # Call the function with unpacked arguments
            actual = solve(schema, data, query)

            # If actual is an error string, compare directly
            if isinstance(actual, str) and actual.startswith("Error:"):
                # Basic check if expected is also an error string (might need refinement)
                result = isinstance(expected, str) and expected.startswith("Error:")
                # More specific error checking could be added here if needed
            elif isinstance(actual, list):
                 # Ensure actual is sorted list of tuples before comparison
                 actual = sorted([tuple(row) for row in actual])
                 result = (actual == expected)
            else:
                 # Handle unexpected return types from solve()
                 print(f"Warning: Unexpected return type from solve(): {type(actual)}", file=sys.stderr)
                 result = (actual == expected) # Attempt comparison anyway

        except Exception as e:
            print(f"\nError during Test {i+1} execution: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc()
            result = False # Ensure test fails on exception
            actual = f"Execution Error: {e}"

        print(f"Actual: {actual}")
        print(f"Result: {result}")

        if result:
            correct_count += 1

    print(f"\n--- Summary ---")
    print(f"Total Correct: {correct_count} / {total_count}")
    return correct_count, total_count

# --- Test Cases ---
# Define test cases based on the expected behavior of the 'solve' function.
# Since 'solve' now executes SQL, tests involve schema, data, query, and expected results.

test_cases = [
    {
        "input": {
            "db_schema_sql": "CREATE TABLE Employees (id INT, name TEXT, salary INT);",
            "data_dict": {'Employees': [(1, 'Alice', 70000), (2, 'Bob', 80000), (3, 'Charlie', 60000)]},
            "query_sql": "SELECT name, salary FROM Employees WHERE salary > 65000 ORDER BY name;"
        },
        "expected": [('Alice', 70000), ('Bob', 80000)]
        # Note: solve() sorts the final result list, so ORDER BY in SQL affects intermediate steps,
        # but final comparison uses Python's sort on the tuples.
    },
    {
        "input": {
            "db_schema_sql": "CREATE TABLE Products (pid INT, pname TEXT, price REAL);",
            "data_dict": {'Products': [(101, 'Laptop', 1200.50), (102, 'Mouse', 25.00), (103, 'Keyboard', 75.75)]},
            "query_sql": "SELECT pname FROM Products WHERE price < 100.00;"
        },
        "expected": [('Keyboard',), ('Mouse',)] # Expecting tuples even for single column results
    },
    {
        "input": {
            "db_schema_sql": "CREATE TABLE Students (sid INT PRIMARY KEY, sname TEXT); CREATE TABLE Courses (cid TEXT, cname TEXT); CREATE TABLE Enrollments (sid INT, cid TEXT);",
            "data_dict": {
                'Students': [(1, 'Eve'), (2, 'Frank')],
                'Courses': [('CS101', 'Intro CS'), ('MA101', 'Calculus')],
                'Enrollments': [(1, 'CS101'), (1, 'MA101'), (2, 'CS101')]
            },
            "query_sql": """
                SELECT s.sname, c.cname
                FROM Students s
                JOIN Enrollments e ON s.sid = e.sid
                JOIN Courses c ON e.cid = c.cid
                WHERE s.sname = 'Eve';
            """
        },
        "expected": [('Eve', 'Intro CS'), ('Eve', 'Calculus')]
    },
    {
        "input": {
            "db_schema_sql": "CREATE TABLE EmptyTable (colA INT);",
            "data_dict": {'EmptyTable': []},
            "query_sql": "SELECT colA FROM EmptyTable;"
        },
        "expected": []
    },
    {
        "input": {
            "db_schema_sql": "CREATE TABLE Numbers (val INT);",
            "data_dict": {'Numbers': [(1,), (2,), (3,), (2,)]},
            "query_sql": "SELECT DISTINCT val FROM Numbers;"
        },
        "expected": [(1,), (2,), (3,)]
    },
     { # Test case expecting an error (e.g., query syntax error)
        "input": {
            "db_schema_sql": "CREATE TABLE Test (id INT);",
            "data_dict": {'Test': [(1,)]},
            "query_sql": "SELEC * FROM Test;" # Intentional typo "SELEC"
        },
        "expected": "Error: near \"SELEC\": syntax error" # Expecting an error message string
    },
     { # Test case expecting an error (e.g., table not found)
        "input": {
            "db_schema_sql": "CREATE TABLE Test (id INT);",
            "data_dict": {'Test': [(1,)]},
            "query_sql": "SELECT id FROM NonExistentTable;"
        },
        "expected": "Error: no such table: NonExistentTable"
    },

]

# --- Main Execution ---
if __name__ == "__main__":
    print("Starting SQL Problem Test Runner...")
    run_tests(test_cases)
    print("\nTesting finished.")