import sys
import io

# Since the problem description "SQL Schema" is very generic and doesn't specify
# a concrete task, we will define a placeholder problem and its solution.
# Placeholder Problem: Given a representation of a simplified SQL schema,
# find all unique column names that are used as primary keys across all tables.

# Input format: A dictionary where keys are table names (strings) and values
# are lists of column names (strings) that form the primary key for that table.
# An empty list means the table has no defined primary key in this simplified model.

# Output format: A sorted list of unique primary key column names found in the schema.

def solve(schema_info):
    """
    Finds all unique column names used as primary keys in the given schema.

    Args:
        schema_info: A dictionary representing the schema.
                       Keys are table names (str).
                       Values are lists of primary key column names (list[str]).

    Returns:
        A sorted list of unique primary key column names (list[str]).
    """
    primary_key_columns = set()
    if not isinstance(schema_info, dict):
        # Handle invalid input type gracefully if necessary, though tests assume dict
        return []

    for table_name, pk_columns in schema_info.items():
        # Ensure pk_columns is iterable (e.g., a list) before proceeding
        if isinstance(pk_columns, (list, tuple, set)):
            primary_key_columns.update(pk_columns)
        # Else: Ignore entries where the value isn't a collection of column names

    return sorted(list(primary_key_columns))

# --- Test Framework ---

# Define Test Cases
# Each test case is a dictionary with 'input' and 'expected_output'.
test_cases = [
    {
        'input': {
            'Users': ['user_id'],
            'Products': ['product_id'],
            'Orders': ['order_id']
        },
        'expected_output': ['order_id', 'product_id', 'user_id']
    },
    {
        'input': {
            'OrderItems': ['order_id', 'product_id'],
            'Shipments': ['shipment_id']
        },
        'expected_output': ['order_id', 'product_id', 'shipment_id']
    },
    {
        'input': {}, # Empty schema
        'expected_output': []
    },
    {
        'input': {
            'Users': ['user_id'],
            'Logs': [] # Table with no primary key
        },
        'expected_output': ['user_id']
    },
    {
        'input': {
            'TableA': ['id'],
            'TableB': ['id', 'ref_id'] # 'id' appears twice, should be unique in output
        },
        'expected_output': ['id', 'ref_id']
    },
    {
        'input': {
            'Customers': ['customer_id'],
            'Invoices': ['invoice_id'],
            'InvoiceLines': ['invoice_id', 'line_number'] # Composite key
        },
        'expected_output': ['customer_id', 'invoice_id', 'line_number']
    },
    {
        'input': {
             'Departments': ['dept_no'],
             'Employees': ['emp_no'],
             'Dept_Emp': ['emp_no', 'dept_no'], # Composite FK/PK
             'Salaries': ['emp_no', 'from_date'] # Composite PK
        },
        'expected_output': ['dept_no', 'emp_no', 'from_date']
    },
     {
        'input': {
             'Table_No_PK': None, # Handle potential None value gracefully
             'Another_Table': ['key_col']
        },
        'expected_output': ['key_col'] # solve function should ignore None
    },
    {
        'input': {
             'Table_With_Single_PK': ['id'],
             'Table_With_No_PK_Again': []
        },
        'expected_output': ['id']
    }
]

def run_tests(test_cases):
    """
    Runs the defined test cases against the solve function.
    """
    correct_count = 0
    total_count = len(test_cases)

    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    for i, test_case in enumerate(test_cases):
        input_data = test_case['input']
        expected_output = test_case['expected_output']

        # Make a copy if the solve function modifies the input, though this one doesn't
        # input_data_copy = copy.deepcopy(input_data)
        actual_output = solve(input_data) # Use input_data_copy if modification occurs

        if actual_output == expected_output:
            print(f"True")
            correct_count += 1
        else:
            # Print False for failed test
            print(f"False")
            # Optionally print details for debugging:
            # print(f"Test {i+1} Failed:")
            # print(f"  Input: {input_data}")
            # print(f"  Expected: {expected_output}")
            # print(f"  Actual: {actual_output}")

    # Restore stdout
    sys.stdout = old_stdout

    # Get the captured output
    test_results_output = captured_output.getvalue()

    # Print the captured output (True/False for each test)
    print(test_results_output, end="")

    # Print the final summary line
    print(f"{correct_count}/{total_count}")

# Execute the tests
if __name__ == "__main__":
    run_tests(test_cases)