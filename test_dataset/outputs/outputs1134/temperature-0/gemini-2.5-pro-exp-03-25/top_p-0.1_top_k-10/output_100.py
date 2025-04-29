import sys
import io
import pandas as pd
import sqlite3

# -- PROBLEM DESCRIPTION (Assumed based on "SQL Schema" prompt) --
# Although no specific SQL query or task was provided, we'll assume a common task:
# Given two tables, Employees (id, name, departmentId) and Departments (id, name),
# find the names of employees belonging to a specific department (e.g., 'Sales').
#
# The Python function will simulate this query using pandas DataFrames as input,
# mimicking tables.

# -- SOLUTION FUNCTION --
def solve_sql_problem(employees_df, departments_df, target_dept_name):
    """
    Simulates an SQL query to find employee names in a specific department.

    Args:
        employees_df (pd.DataFrame): DataFrame representing the Employees table.
                                     Expected columns: 'id', 'name', 'departmentId'.
        departments_df (pd.DataFrame): DataFrame representing the Departments table.
                                       Expected columns: 'id', 'name'.
        target_dept_name (str): The name of the department to filter by.

    Returns:
        list: A sorted list of names of employees in the target department.
              Returns an empty list if the department doesn't exist or has no employees.
    """
    if departments_df.empty or employees_df.empty:
        return []

    # Find the department ID for the target department name
    target_dept = departments_df[departments_df['name'] == target_dept_name]
    if target_dept.empty:
        return [] # Department not found

    target_dept_id = target_dept['id'].iloc[0] # Get the first matching department ID

    # Merge (join) employees and departments on the department ID
    merged_df = pd.merge(employees_df, departments_df, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))

    # Filter for employees in the target department
    result_df = merged_df[merged_df['departmentId'] == target_dept_id]

    # Get the names and sort them
    result_names = sorted(result_df['name_emp'].tolist())

    return result_names

# --- Testing Framework ---
def run_tests():
    """
    Runs test cases against the solve_sql_problem function.
    """
    test_cases = [
        # Test Case 1: Basic case - Find employees in 'Sales'
        {
            "inputs": {
                "employees_df": pd.DataFrame({
                    'id': [1, 2, 3, 4, 5],
                    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
                    'departmentId': [101, 102, 101, 103, 102]
                }),
                "departments_df": pd.DataFrame({
                    'id': [101, 102, 103],
                    'name': ['Sales', 'Engineering', 'HR']
                }),
                "target_dept_name": 'Sales'
            },
            "expected_output": ['Alice', 'Charlie']
        },
        # Test Case 2: Target department exists but has no employees
        {
            "inputs": {
                "employees_df": pd.DataFrame({
                    'id': [1, 2],
                    'name': ['Frank', 'Grace'],
                    'departmentId': [202, 202] # No one in Marketing (201)
                }),
                "departments_df": pd.DataFrame({
                    'id': [201, 202],
                    'name': ['Marketing', 'Support']
                }),
                "target_dept_name": 'Marketing'
            },
            "expected_output": []
        },
        # Test Case 3: Target department does not exist
        {
            "inputs": {
                "employees_df": pd.DataFrame({
                    'id': [1],
                    'name': ['Heidi'],
                    'departmentId': [301]
                }),
                "departments_df": pd.DataFrame({
                    'id': [301],
                    'name': ['Finance']
                }),
                "target_dept_name": 'Sales' # 'Sales' dept doesn't exist
            },
            "expected_output": []
        },
        # Test Case 4: Empty employees table
        {
            "inputs": {
                "employees_df": pd.DataFrame(columns=['id', 'name', 'departmentId']),
                "departments_df": pd.DataFrame({
                    'id': [101],
                    'name': ['Sales']
                }),
                "target_dept_name": 'Sales'
            },
            "expected_output": []
        },
        # Test Case 5: Empty departments table
        {
            "inputs": {
                "employees_df": pd.DataFrame({
                    'id': [1],
                    'name': ['Ivy'],
                    'departmentId': [101]
                }),
                "departments_df": pd.DataFrame(columns=['id', 'name']),
                "target_dept_name": 'Sales'
            },
            "expected_output": []
        },
         # Test Case 6: Multiple employees in the target department (check sorting)
        {
            "inputs": {
                "employees_df": pd.DataFrame({
                    'id': [1, 2, 3, 4, 5],
                    'name': ['Zoe', 'Xavier', 'Yara', 'Wendy', 'Victor'],
                    'departmentId': [401, 402, 401, 401, 403] # Zoe, Yara, Wendy in 401
                }),
                "departments_df": pd.DataFrame({
                    'id': [401, 402, 403],
                    'name': ['DevOps', 'QA', 'Product']
                }),
                "target_dept_name": 'DevOps'
            },
            "expected_output": ['Wendy', 'Yara', 'Zoe'] # Expect sorted names
        },
    ]

    correct_count = 0
    total_tests = len(test_cases)

    # Capture standard output to prevent interference with test results
    original_stdout = sys.stdout
    # Redirect stdout to a string buffer
    # sys.stdout = io.StringIO() # Commented out to allow direct printing

    try:
        for i, test_case in enumerate(test_cases):
            inputs = test_case["inputs"]
            expected = test_case["expected_output"]
            test_passed = False
            error_message = ""

            try:
                # Call the solver function with unpacked inputs
                actual = solve_sql_problem(**inputs)

                # Compare actual vs expected
                # Sorting is handled within the function, so direct comparison works
                if actual == expected:
                    test_passed = True
                    correct_count += 1
                else:
                     error_message = f" Expected: {expected}, Actual: {actual}"


            except Exception as e:
                # Catch errors during the execution of the solution function
                error_message = f" Error: {e}"
                test_passed = False

            # Print result directly to original stdout
            print(f"Test {i+1}: {test_passed}{error_message}", file=original_stdout)


    finally:
        # Restore standard output if it was redirected
        # sys.stdout = original_stdout
        pass # No redirection used in the final version

    # Print the summary
    print(f"\n{correct_count} / {total_tests} tests passed.", file=original_stdout)

# --- Main Execution ---
if __name__ == '__main__':
    # Note: The problem description didn't specify how the schema/data is provided.
    # This example uses pandas DataFrames as a convenient way to represent tables
    # in Python, suitable for simulating SQL operations.
    # If the actual problem involves reading from a database file or other source,
    # the `solve_sql_problem` function and test setup would need modification.
    run_tests()