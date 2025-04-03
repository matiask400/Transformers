import sys
import io
import sqlite3
import pandas as pd
import traceback

# --- Database Schema (as inferred from common SQL problems) ---
# This section is usually provided by the problem description.
# Since it's missing, we'll assume a generic schema or create one
# based on the tests later. For now, let's leave it abstract.
# Example Schema (if needed for a specific problem):
# CREATE TABLE Customers (
#     id INT PRIMARY KEY,
#     name VARCHAR(255)
# );
# CREATE TABLE Orders (
#     id INT PRIMARY KEY,
#     customerId INT,
#     FOREIGN KEY (customerId) REFERENCES Customers(id)
# );

# --- Solution Function ---
# This function should implement the logic to solve the specific SQL problem.
# It will typically take database connection or dataframes as input
# and return the result of the query, usually as a pandas DataFrame or list of tuples/dicts.

def solve(db_connection):
    """
    Solves the specific SQL problem.
    Replace the content of this function with the actual SQL query execution
    and result fetching logic based on the problem description.

    Args:
        db_connection: An active sqlite3 connection object to the database.

    Returns:
        A pandas DataFrame or a list of tuples/dictionaries representing the query result.
        The exact format depends on how comparison is done in the tests.
        Using pandas DataFrame is common and convenient.
    """
    # Placeholder implementation: Replace with your actual SQL query
    # Example: Select all customers
    try:
        query = "SELECT 'Replace this query' AS result;" # Replace this with the actual query
        # Example: query = "SELECT name FROM Customers WHERE id IN (SELECT customerId FROM Orders);"
        result_df = pd.read_sql_query(query, db_connection)
        return result_df
    except Exception as e:
        print(f"Error executing query: {e}")
        traceback.print_exc()
        # Return an empty DataFrame or raise the exception, depending on desired handling
        return pd.DataFrame()


# --- Test Harness ---

def setup_database(db_name=":memory:", schema_sql=None, data_sql=None):
    """Creates an in-memory SQLite database, executes schema and data scripts."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    if schema_sql:
        try:
            cursor.executescript(schema_sql)
        except sqlite3.Error as e:
            print(f"Error executing schema SQL: {e}")
            traceback.print_exc()
            conn.close()
            raise
    if data_sql:
        try:
            cursor.executescript(data_sql)
        except sqlite3.Error as e:
            print(f"Error executing data SQL: {e}")
            traceback.print_exc()
            conn.close()
            raise
    conn.commit()
    return conn

def compare_results(actual, expected):
    """
    Compares the actual result (DataFrame) with the expected result (DataFrame).
    Handles potential differences in row order and column order.
    """
    if not isinstance(actual, pd.DataFrame) or not isinstance(expected, pd.DataFrame):
        return actual == expected # Fallback for non-dataframe results

    if actual.empty and expected.empty:
        return True
    if actual.empty or expected.empty:
        return False

    # Sort columns
    actual_sorted_cols = actual.sort_index(axis=1)
    expected_sorted_cols = expected.sort_index(axis=1)

    if list(actual_sorted_cols.columns) != list(expected_sorted_cols.columns):
        print(f"Column mismatch: Actual={list(actual_sorted_cols.columns)}, Expected={list(expected_sorted_cols.columns)}")
        return False

    # Sort rows based on all columns
    try:
        actual_sorted = actual_sorted_cols.sort_values(by=list(actual_sorted_cols.columns)).reset_index(drop=True)
        expected_sorted = expected_sorted_cols.sort_values(by=list(expected_sorted_cols.columns)).reset_index(drop=True)
    except Exception as e:
        print(f"Could not sort DataFrames for comparison: {e}")
        # Fallback to comparing potentially unsorted frames if sorting fails
        return actual_sorted_cols.equals(expected_sorted_cols)


    # Compare sorted dataframes
    return actual_sorted.equals(expected_sorted)

def run_test(test_case):
    """Runs a single test case."""
    db_name = f":memory:" # Use unique in-memory db for each test if needed, or shared
    schema_sql = test_case.get("schema", "")
    data_sql = test_case.get("data", "")
    expected_output_data = test_case.get("expected_output", [])
    expected_columns = test_case.get("expected_columns", None)

    conn = None
    try:
        conn = setup_database(db_name, schema_sql, data_sql)

        # Convert expected output list of lists/dicts to DataFrame
        if expected_columns:
             expected_df = pd.DataFrame(expected_output_data, columns=expected_columns)
        elif expected_output_data and isinstance(expected_output_data[0], dict):
             expected_df = pd.DataFrame(expected_output_data)
        elif expected_output_data:
             # Try to infer columns if not dicts and columns not provided (less robust)
             # This part might need adjustment based on the specific problem's output format
             try:
                 # Attempt to get columns from the schema or a dummy query if possible
                 # For now, assume simple list of tuples/lists requires explicit columns
                 print("Warning: Expected output format requires 'expected_columns' for DataFrame conversion.")
                 # As a fallback, create a DataFrame with default column names
                 num_cols = len(expected_output_data[0]) if expected_output_data else 0
                 expected_df = pd.DataFrame(expected_output_data, columns=[f'col_{i}' for i in range(num_cols)])
             except:
                 expected_df = pd.DataFrame(expected_output_data) # Best effort
        else:
             expected_df = pd.DataFrame() # Empty expected result


        # Execute the solution function
        actual_output = solve(conn)

        # Compare results
        passed = compare_results(actual_output, expected_df)
        print(f"{passed}")
        return passed

    except Exception as e:
        print(f"False") # Test failed due to exception
        print(f"  Error during test execution: {e}")
        traceback.print_exc()
        return False
    finally:
        if conn:
            conn.close()

# --- Test Cases ---
# Define test cases as a list of dictionaries.
# Each dictionary should contain:
#   - 'name': A descriptive name for the test.
#   - 'schema': SQL string to create tables.
#   - 'data': SQL string to insert data.
#   - 'expected_output': A list of lists or list of dictionaries representing the expected result rows.
#   - 'expected_columns': (Optional but recommended) A list of column names for the expected output.

# ******************************************************************************
# * PROBLEM-SPECIFIC PART: Replace or add test cases based on the actual problem *
# ******************************************************************************
# Example Test Cases (assuming a simple problem: "Find customers with orders")
test_cases = [
    {
        "name": "Test 1: Basic Join",
        "schema": """
        CREATE TABLE Customers (id INT PRIMARY KEY, name VARCHAR(255));
        CREATE TABLE Orders (id INT PRIMARY KEY, customerId INT);
        """,
        "data": """
        INSERT INTO Customers (id, name) VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie');
        INSERT INTO Orders (id, customerId) VALUES (101, 1), (102, 3), (103, 1);
        """,
        # Replace the 'solve' function's query with:
        # "SELECT c.name FROM Customers c JOIN Orders o ON c.id = o.customerId GROUP BY c.name ORDER BY c.name;"
        # Or if solve should return DataFrame directly:
        # query = "SELECT c.name FROM Customers c JOIN Orders o ON c.id = o.customerId GROUP BY c.name ORDER BY c.name;"
        # return pd.read_sql_query(query, db_connection)
        "expected_columns": ["name"],
        "expected_output": [
            ["Alice"],
            ["Charlie"],
        ],
        # Note: If the 'solve' function is modified to produce this output, the test will pass.
        # Currently, the placeholder 'solve' will likely fail this test.
    },
    {
        "name": "Test 2: No Orders",
        "schema": """
        CREATE TABLE Customers (id INT PRIMARY KEY, name VARCHAR(255));
        CREATE TABLE Orders (id INT PRIMARY KEY, customerId INT);
        """,
        "data": """
        INSERT INTO Customers (id, name) VALUES (1, 'Alice'), (2, 'Bob');
        """,
        "expected_columns": ["name"],
        "expected_output": [],
    },
    {
        "name": "Test 3: Customer without Orders",
        "schema": """
        CREATE TABLE Customers (id INT PRIMARY KEY, name VARCHAR(255));
        CREATE TABLE Orders (id INT PRIMARY KEY, customerId INT);
        """,
        "data": """
        INSERT INTO Customers (id, name) VALUES (1, 'Alice'), (2, 'Bob');
        INSERT INTO Orders (id, customerId) VALUES (101, 1);
        """,
        "expected_columns": ["name"],
        "expected_output": [
            ["Alice"],
        ],
    },
    {
        "name": "Test 4: Empty Tables",
        "schema": """
        CREATE TABLE Customers (id INT PRIMARY KEY, name VARCHAR(255));
        CREATE TABLE Orders (id INT PRIMARY KEY, customerId INT);
        """,
        "data": "", # No data
        "expected_columns": ["name"],
        "expected_output": [],
    },
    # Add more test cases specific to the actual SQL problem here
]

# --- Main Execution Logic ---
if __name__ == "__main__":
    # --- !!! IMPORTANT !!! ---
    # --- Replace the placeholder query inside the 'solve' function ---
    # --- with the actual SQL query required by the problem description. ---
    print("Reminder: Ensure the 'solve' function contains the correct SQL query for the problem.")
    print("Running tests with the placeholder 'solve' function...\n")

    correct_tests = 0
    total_tests = len(test_cases)

    # Check if solve function still has the placeholder
    conn_check = setup_database()
    try:
        df_check = solve(conn_check)
        if not df_check.empty and 'result' in df_check.columns and df_check['result'].iloc[0] == 'Replace this query':
             print("WARNING: The 'solve' function still contains the placeholder query.")
             print("         Tests will likely fail unless the expected output matches the placeholder.\n")
    except Exception:
        pass # Ignore errors here, they'll be caught during tests
    finally:
        if conn_check:
            conn_check.close()


    for i, test_case in enumerate(test_cases):
        print(f"--- Running Test Case {i+1}: {test_case['name']} ---")
        passed = run_test(test_case)
        if passed:
            correct_tests += 1
        print(f"--- End Test Case {i+1} ---")
        print() # Add a newline for better separation


    print(f"\n--- Summary ---")
    print(f"{correct_tests}/{total_tests} tests passed.")
    print(f"---------------")

    # Optional: Exit with non-zero status if any test failed (useful for CI/CD)
    # if correct_tests != total_tests:
    #     sys.exit(1)