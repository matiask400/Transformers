def solve_query(customers, orders):
    customer_names_with_orders = set()
    for order in orders:
        for customer in customers:
            if customer['CustomerID'] == order['CustomerID']:
                customer_names_with_orders.add(customer['Name'])
                break
    return sorted(list(customer_names_with_orders))

def run_tests():
    test_cases = [
        {
            'customers': [
                {'CustomerID': 1, 'Name': 'Alice', 'City': 'New York'},
                {'CustomerID': 2, 'Name': 'Bob', 'City': 'London'},
                {'CustomerID': 3, 'Name': 'Charlie', 'City': 'Paris'}
            ],
            'orders': [
                {'OrderID': 101, 'CustomerID': 1, 'OrderDate': '2023-01-01'},
                {'OrderID': 102, 'CustomerID': 2, 'OrderDate': '2023-01-05'}
            ],
            'expected_output': ['Alice', 'Bob']
        },
        {
            'customers': [
                {'CustomerID': 1, 'Name': 'Alice', 'City': 'New York'},
                {'CustomerID': 2, 'Name': 'Bob', 'City': 'London'},
                {'CustomerID': 3, 'Name': 'Charlie', 'City': 'Paris'}
            ],
            'orders': [],
            'expected_output': []
        },
        {
            'customers': [
                {'CustomerID': 1, 'Name': 'Alice', 'City': 'New York'},
                {'CustomerID': 2, 'Name': 'Bob', 'City': 'London'},
                {'CustomerID': 3, 'Name': 'Charlie', 'City': 'Paris'}
            ],
            'orders': [
                {'OrderID': 101, 'CustomerID': 1, 'OrderDate': '2023-01-01'},
                {'OrderID': 102, 'CustomerID': 1, 'OrderDate': '2023-01-05'},
                {'OrderID': 103, 'CustomerID': 3, 'OrderDate': '2023-01-10'}
            ],
            'expected_output': ['Alice', 'Charlie']
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        customers = test_case['customers']
        orders = test_case['orders']
        expected_output = test_case['expected_output']

        actual_output = solve_query(customers, orders)

        if actual_output == expected_output:
            print(f'Test {i+1}: True')
            correct_tests += 1
        else:
            print(f'Test {i+1}: False')
            print(f'  Expected: {expected_output}')
            print(f'  Actual:   {actual_output}')

    print(f'Correct tests: {correct_tests}/{total_tests}')

if __name__ == '__main__':
    run_tests()