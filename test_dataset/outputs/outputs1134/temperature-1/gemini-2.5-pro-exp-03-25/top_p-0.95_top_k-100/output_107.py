import sys
import io

# Assume the SQL tables are represented as lists of dictionaries in Python
# Example Schema:
# Customers table: [{'id': int, 'name': str}, ...]
# Orders table: [{'id': int, 'customerId': int}, ...]

def find_customers_without_orders(customers_table, orders_table):
    """
    Finds customers who have never placed an order.

    Args:
        customers_table: A list of dictionaries representing the Customers table.
                         Each dictionary has keys 'id' and 'name'.
        orders_table: A list of dictionaries representing the Orders table.
                      Each dictionary has keys 'id' and 'customerId'.

    Returns:
        A list of dictionaries, where each dictionary represents a customer
        who has never ordered. Each dictionary has one key 'Customers'
        with the customer's name as the value.
        Example: [{'Customers': 'Henry'}, {'Customers': 'Max'}]
    """
    
    # 1. Get the set of all customer IDs who have placed orders
    # Using a set provides efficient lookups (O(1) on average)
    customer_ids_with_orders = set()
    for order in orders_table:
        # Check if 'customerId' key exists to handle potential malformed data
        if 'customerId' in order:
            customer_ids_with_orders.add(order['customerId'])

    # 2. Iterate through customers and find those whose IDs are not in the set
    customers_without_orders_list = []
    for customer in customers_table:
         # Check if 'id' and 'name' keys exist
        if 'id' in customer and 'name' in customer:
            if customer['id'] not in customer_ids_with_orders:
                # Format the output as required: [{'Customers': name}]
                customers_without_orders_list.append({'Customers': customer['name']})

    return customers_without_orders_list

# --- Testing Framework ---

def run_tests():
    """
    Runs predefined test cases against the find_customers_without_orders function.
    """
    test_cases = [
        {
            'name': 'LeetCode Example',
            'customers': [
                {'id': 1, 'name': 'Joe'},
                {'id': 2, 'name': 'Henry'},
                {'id': 3, 'name': 'Sam'},
                {'id': 4, 'name': 'Max'}
            ],
            'orders': [
                {'id': 1, 'customerId': 3},
                {'id': 2, 'customerId': 1}
            ],
            'expected': [
                {'Customers': 'Henry'},
                {'Customers': 'Max'}
            ]
        },
        {
            'name': 'No Orders Placed',
            'customers': [
                {'id': 1, 'name': 'Alice'},
                {'id': 2, 'name': 'Bob'}
            ],
            'orders': [],
            'expected': [
                {'Customers': 'Alice'},
                {'Customers': 'Bob'}
            ]
        },
        {
            'name': 'All Customers Placed Orders',
            'customers': [
                {'id': 1, 'name': 'Charlie'},
                {'id': 2, 'name': 'David'}
            ],
            'orders': [
                {'id': 1, 'customerId': 1},
                {'id': 2, 'customerId': 2}
            ],
            'expected': []
        },
        {
            'name': 'No Customers',
            'customers': [],
            'orders': [
                {'id': 1, 'customerId': 1}
            ],
            'expected': []
        },
        {
            'name': 'Empty Tables',
            'customers': [],
            'orders': [],
            'expected': []
        },
         {
            'name': 'Duplicate Orders',
            'customers': [
                {'id': 1, 'name': 'Eve'},
                {'id': 2, 'name': 'Frank'}
            ],
            'orders': [
                {'id': 1, 'customerId': 1},
                {'id': 2, 'customerId': 1}, # Duplicate order for Eve
                 {'id': 3, 'customerId': 1}
            ],
            'expected': [
                 {'Customers': 'Frank'}
            ]
        },
        {
            'name': 'Order from non-existent customer (should be ignored)',
             'customers': [
                {'id': 1, 'name': 'Grace'},
                {'id': 2, 'name': 'Heidi'}
            ],
            'orders': [
                {'id': 1, 'customerId': 1}, # Grace ordered
                {'id': 2, 'customerId': 99} # Order from customer 99 (not in Customers table)
            ],
            'expected': [
                {'Customers': 'Heidi'}
            ]
        }
    ]

    correct_count = 0
    total_tests = len(test_cases)

    # Redirect stdout to capture prints
    old_stdout = sys.stdout
    redirected_output = io.StringIO()
    sys.stdout = redirected_output

    for i, test in enumerate(test_cases):
        customers_input = test['customers']
        orders_input = test['orders']
        expected_output = test['expected']

        # Run the student's function
        try:
            actual_output = find_customers_without_orders(customers_input, orders_input)

            # Sort both lists of dictionaries for order-insensitive comparison
            # Use a stable sort key, e.g., the 'Customers' value
            actual_sorted = sorted(actual_output, key=lambda x: x.get('Customers', ''))
            expected_sorted = sorted(expected_output, key=lambda x: x.get('Customers', ''))


            # Compare the results
            if actual_sorted == expected_sorted:
                print("True") # Test passed
                correct_count += 1
            else:
                print("False") # Test failed
                # Optional: Print detailed failure info for debugging
                # print(f"--- Failure Details Test {i+1} ({test['name']}) ---")
                # print(f"Input Customers: {customers_input}")
                # print(f"Input Orders: {orders_input}")
                # print(f"Expected (sorted): {expected_sorted}")
                # print(f"Actual (sorted): {actual_sorted}")
                # print("--- End Failure Details ---")

        except Exception as e:
             print(f"False") # Test failed due to error
             # Optional: Print error details
             # print(f"--- Error Test {i+1} ({test['name']}) ---")
             # print(f"Error: {e}")
             # import traceback
             # traceback.print_exc()
             # print("--- End Error Details ---")


    # Restore stdout
    sys.stdout = old_stdout

    # Print the captured output
    print(redirected_output.getvalue(), end='')

    # Print the final score summary
    print(f"{correct_count}/{total_tests}")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()