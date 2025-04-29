import sys
import io

# Assume the problem is to represent a simple SQL schema (list of tables and their columns)
# as a Python dictionary where keys are table names and values are lists of column names.
# The input format is assumed to be a list of tuples/lists, where each inner item
# represents a table: (table_name, [column1, column2, ...]) or [table_name, [column1, ...]].

def solve(schema_definition):
    """
    Processes a list representing table definitions and returns a dictionary
    mapping table names to lists of their columns.

    Args:
        schema_definition: A list where each element represents a table.
                           Each element should be an iterable (like a tuple or list)
                           of length 2: (table_name, [col1, col2, ...]).

    Returns:
        A dictionary representing the schema: {table_name: [col1, col2, ...], ...}
    """
    schema_dict = {}
    if not isinstance(schema_definition, list):
        # Handle potentially invalid input type gracefully for testing
        return {"error": "Input must be a list"}

    for item in schema_definition:
        # Check if the item is iterable and has at least two elements
        try:
            if len(item) >= 2:
                table_name = item[0]
                columns = item[1]
                # Basic type checking for table_name (should be string)
                # and columns (should be list-like)
                if isinstance(table_name, str) and hasattr(columns, '__iter__') and not isinstance(columns, str):
                    # Convert columns to a list to ensure consistency
                    schema_dict[table_name] = list(columns)
                else:
                     # Handle malformed item within the list if needed, or ignore
                     # For simplicity, we'll ignore malformed items here
                     # Or return an error marker if strict validation is needed
                     pass # Ignoring malformed item
            else:
                # Ignoring malformed item (less than 2 elements)
                pass
        except (TypeError, IndexError):
             # Handle cases where item is not indexable or causes errors
             # Ignoring malformed item
             pass

    return schema_dict

# --- Test Runner ---

# Define test cases
test_cases = [
    # Test Case 1: Basic schema with two tables
    {
        "input": [('Customers', ['CustomerID', 'Name', 'Email']), ('Orders', ['OrderID', 'CustomerID', 'OrderDate'])],
        "expected": {'Customers': ['CustomerID', 'Name', 'Email'], 'Orders': ['OrderID', 'CustomerID', 'OrderDate']}
    },
    # Test Case 2: Schema with one table
    {
        "input": [('Products', ['ProductID', 'ProductName', 'Price'])],
        "expected": {'Products': ['ProductID', 'ProductName', 'Price']}
    },
    # Test Case 3: Empty schema definition
    {
        "input": [],
        "expected": {}
    },
    # Test Case 4: Schema with table having no columns
    {
        "input": [('LogEntries', [])],
        "expected": {'LogEntries': []}
    },
    # Test Case 5: Input using lists instead of tuples
    {
        "input": [['Users', ['UserID', 'Username']], ['Roles', ['RoleID', 'RoleName']]],
        "expected": {'Users': ['UserID', 'Username'], 'Roles': ['RoleID', 'RoleName']}
    },
    # Test Case 6: Input with mixed types (tuple and list for columns) - should normalize to list
    {
        "input": [('TableA', ('ColA', 'ColB')), ['TableB', ['ColC', 'ColD']]],
        "expected": {'TableA': ['ColA', 'ColB'], 'TableB': ['ColC', 'ColD']}
    },
    # Test Case 7: Input with malformed item (not enough elements) - should be ignored
    {
        "input": [('ValidTable', ['Col1']), ('MalformedTable',)], # Malformed item
        "expected": {'ValidTable': ['Col1']}
    },
    # Test Case 8: Input with malformed item (wrong types) - should be ignored
    {
        "input": [('GoodTable', ['ID']), (123, ['BadName']), ('AnotherTable', 'NotAList')], # Malformed items
        "expected": {'GoodTable': ['ID']}
    },
     # Test Case 9: Input itself is not a list (invalid input type)
    {
        "input": "This is not a list",
        "expected": {"error": "Input must be a list"} # Or specific error handling if defined
    },
    # Test Case 10: More complex schema
    {
        "input": [
            ('employees', ['emp_id', 'first_name', 'last_name', 'dept_id']),
            ('departments', ['dept_id', 'dept_name']),
            ('salaries', ['emp_id', 'salary', 'from_date', 'to_date'])
        ],
        "expected": {
            'employees': ['emp_id', 'first_name', 'last_name', 'dept_id'],
            'departments': ['dept_id', 'dept_name'],
            'salaries': ['emp_id', 'salary', 'from_date', 'to_date']
        }
    },

]

# Run tests
correct_count = 0
total_tests = len(test_cases)

# Redirect stdout to capture prints during testing
original_stdout = sys.stdout
sys.stdout = captured_stdout = io.StringIO()

for i, test in enumerate(test_cases):
    input_data = test["input"]
    expected_output = test["expected"]

    # Capture output of the solve function if needed (not needed for this problem)
    # actual_output = solve(input_data)

    # For this problem, we just call solve and compare return values
    try:
        actual_output = solve(input_data)
        # Comparison
        is_correct = actual_output == expected_output
    except Exception as e:
        # If the function raises an unexpected error, mark as False
        is_correct = False
        print(f"Test {i+1} raised an error: {e}", file=original_stdout) # Print error to original stdout

    # Restore stdout temporarily to print True/False
    sys.stdout = original_stdout
    print(f"{is_correct}") # Print True or False for the test
    sys.stdout = captured_stdout # Redirect again

    if is_correct:
        correct_count += 1

# Restore stdout permanently
sys.stdout = original_stdout

# Print summary
print(f"\n{correct_count}/{total_tests}")

# Optional: Print captured stdout content if needed for debugging
# print("\nCaptured Output:\n", captured_stdout.getvalue())
captured_stdout.close()