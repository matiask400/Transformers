import sys
import io
import pandas as pd

# -- PROBLEM DESCRIPTION (Assumed based on "SQL Schema" prompt) --
# Although the specific SQL query/task is missing, we'll assume a common task:
# Given a DataFrame representing a table (e.g., 'Employees'), filter rows based
# on a condition and select specific columns.
#
# Let's assume the task is:
# "Select the 'name' and 'salary' of employees from the 'Employees' table
#  where the 'department' is 'Sales'."
#
# The input to our Python function will be a pandas DataFrame representing
# the 'Employees' table. The output should be a list of dictionaries,
# where each dictionary represents a selected row with 'name' and 'salary'.
# --------------------------------------------------------------------

# -- SQL Schema (Implicitly defined by the DataFrame structure in tests) --
# We'll assume an 'Employees' table/DataFrame with columns like:
# 'employee_id', 'name', 'department', 'salary'
# -----------------------------------------------------------------------


def solve_sql_problem(employees_df: pd.DataFrame) -> list[dict]:
    """
    Simulates an SQL query to select name and salary of employees
    in the 'Sales' department.

    Args:
        employees_df: A pandas DataFrame representing the Employees table.
                      Expected columns: 'name', 'salary', 'department'.

    Returns:
        A list of dictionaries, where each dictionary contains the 'name'
        and 'salary' of an employee in the 'Sales' department.
        Returns an empty list if the DataFrame is empty, lacks required columns,
        or no employees match the criteria.
    """
    # Check if required columns exist
    if not all(col in employees_df.columns for col in ['name', 'salary', 'department']):
        # Handle missing columns gracefully, perhaps return empty list or raise error
        # For this example, return empty list if columns are missing
        return []

    # Filter rows where department is 'Sales'
    sales_employees = employees_df[employees_df['department'] == 'Sales']

    # Select only the 'name' and 'salary' columns
    result_df = sales_employees[['name', 'salary']]

    # Convert the resulting DataFrame to a list of dictionaries
    result_list = result_df.to_dict('records')

    return result_list

# --- Test Harness ---

def compare_results(actual, expected):
    """
    Compares two lists of dictionaries, ignoring order of elements
    and order of keys within dictionaries.
    """
    if not isinstance(actual, list) or not isinstance(expected, list):
        return False
    if len(actual) != len(expected):
        return False

    # Convert lists of dicts to lists of sorted tuples of items for comparison
    try:
        actual_sorted = sorted([tuple(sorted(d.items())) for d in actual])
        expected_sorted = sorted([tuple(sorted(d.items())) for d in expected])
        return actual_sorted == expected_sorted
    except Exception:
        # Handle cases where elements might not be dicts or items aren't sortable
        return False

def run_tests():
    """
    Defines test cases and runs them against the solve_sql_problem function.
    """
    test_cases = [
        # Test Case 1: Basic case with Sales employees
        {
            "input": pd.DataFrame({
                'employee_id': [1, 2, 3, 4],
                'name': ['Alice', 'Bob', 'Charlie', 'David'],
                'department': ['Sales', 'HR', 'Sales', 'Engineering'],
                'salary': [70000, 60000, 75000, 80000]
            }),
            "expected": [
                {'name': 'Alice', 'salary': 70000},
                {'name': 'Charlie', 'salary': 75000}
            ],
            "description": "Basic Sales Filter"
        },
        # Test Case 2: No Sales employees
        {
            "input": pd.DataFrame({
                'employee_id': [1, 2],
                'name': ['Eve', 'Frank'],
                'department': ['HR', 'Engineering'],
                'salary': [65000, 85000]
            }),
            "expected": [],
            "description": "No Sales Employees"
        },
        # Test Case 3: Empty input DataFrame
        {
            "input": pd.DataFrame(columns=['employee_id', 'name', 'department', 'salary']),
            "expected": [],
            "description": "Empty Input Table"
        },
        # Test Case 4: All employees are in Sales
        {
            "input": pd.DataFrame({
                'employee_id': [1, 2],
                'name': ['Grace', 'Heidi'],
                'department': ['Sales', 'Sales'],
                'salary': [72000, 68000]
            }),
            "expected": [
                {'name': 'Grace', 'salary': 72000},
                {'name': 'Heidi', 'salary': 68000}
            ],
            "description": "All Sales Employees"
        },
        # Test Case 5: DataFrame with missing required columns (should return empty)
        {
            "input": pd.DataFrame({
                'employee_id': [1],
                'name': ['Ivy'],
                # 'department' column is missing
                'salary': [90000]
            }),
            "expected": [],
            "description": "Missing 'department' Column"
        },
         # Test Case 6: DataFrame with different data types for salary
        {
            "input": pd.DataFrame({
                'employee_id': [1, 2, 3],
                'name': ['Judy', 'Ken', 'Leo'],
                'department': ['Sales', 'HR', 'Sales'],
                'salary': [71000.50, 62000, 73000] # Mix of float and int
            }),
            "expected": [
                {'name': 'Judy', 'salary': 71000.50},
                {'name': 'Leo', 'salary': 73000}
            ],
            "description": "Mixed Salary Types"
        },
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, test in enumerate(test_cases):
        input_data = test["input"]
        expected_output = test["expected"]
        description = test["description"]

        # print(f"--- Running Test {i+1}: {description} ---")
        try:
            actual_output = solve_sql_problem(input_data.copy()) # Pass a copy
            is_correct = compare_results(actual_output, expected_output)
            print(f"{is_correct}") # Print True or False per test
            if is_correct:
                correct_count += 1
        except Exception as e:
            print(f"False") # Test failed due to exception
            # print(f"Error during test execution: {e}")
        # print("-" * 20)


    print(f"\n{correct_count}/{total_tests} correct")

# --- Main Execution ---
if __name__ == "__main__":
    # Ensure pandas is installed
    try:
        import pandas as pd
    except ImportError:
        print("Error: pandas library is required. Please install it using 'pip install pandas'")
        sys.exit(1)

    run_tests()