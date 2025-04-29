import sqlite3
import os

def run_sql_tests(sql_query, test_cases):
    """
    Runs SQL tests against an in-memory SQLite database.

    Args:
        sql_query (str): The SQL query to be tested.
        test_cases (list): A list of test cases. Each test case is a dictionary
                           with 'customers_data', 'orders_data', and 'expected_output'.
    """
    correct_count = 0
    total_tests = len(test_cases)
    db_name = ':memory:' # Use in-memory database

    conn = None # Initialize conn to None

    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        for i, test_case in enumerate(test_cases):
            # print(f"--- Running Test Case {i+1} ---")
            customers_data = test_case['customers_data']
            orders_data = test_case['orders_data']
            expected_output = test_case['expected_output']

            # 1. Setup: Create tables and insert data
            cursor.execute("DROP TABLE IF EXISTS Customers;")
            cursor.execute("DROP TABLE IF EXISTS Orders;")
            cursor.execute("""
            CREATE TABLE Customers (
                customer_id INT PRIMARY KEY,
                name VARCHAR(255)
            );
            """)
            cursor.execute("""
            CREATE TABLE Orders (
                order_id INT PRIMARY KEY,
                order_date DATE,
                customer_id INT,
                product_id INT,
                FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
            );
            """)

            if customers_data:
                 cursor.executemany("INSERT INTO Customers (customer_id, name) VALUES (?, ?);", customers_data)
            if orders_data:
                cursor.executemany("INSERT INTO Orders (order_id, order_date, customer_id, product_id) VALUES (?, ?, ?, ?);", orders_data)
            conn.commit()

            # 2. Execute the student's query
            try:
                cursor.execute(sql_query)
                actual_output_raw = cursor.fetchall()
                # Sort actual output for consistent comparison
                actual_output = sorted(actual_output_raw)
            except Exception as e:
                print(f"False # Error executing query: {e}")
                actual_output = f"Error: {e}" # Store error message if query fails

            # 3. Compare and Print Result
            # Sort expected output for consistent comparison
            expected_output_sorted = sorted(expected_output)

            if isinstance(actual_output, list) and actual_output == expected_output_sorted:
                print("True")
                correct_count += 1
            else:
                 # print(f"Expected: {expected_output_sorted}")
                 # print(f"Actual:   {actual_output}")
                 print("False")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

    # Print final score
    print(f"{correct_count}/{total_tests} tests passed.")

# -----------------------------------------------------------------------------
# SQL Query to be tested
# -----------------------------------------------------------------------------

# Problem: Find the most frequently ordered product(s) for each customer.
#          If there is a tie for the most frequent product, include all tied products.
# Result columns: customer_id, product_id
# Tables:
#   Customers (customer_id, name)
#   Orders (order_id, order_date, customer_id, product_id)

sql_query = """
WITH ProductCounts AS (
    -- Count how many times each customer ordered each product
    SELECT
        customer_id,
        product_id,
        COUNT(*) AS order_count
    FROM Orders
    GROUP BY customer_id, product_id
),
RankedProducts AS (
    -- Rank products by order count for each customer
    -- Use RANK() to handle ties (all tied products get rank 1)
    SELECT
        customer_id,
        product_id,
        RANK() OVER (PARTITION BY customer_id ORDER BY order_count DESC) as rnk
    FROM ProductCounts
)
-- Select only the products with rank 1 (most frequent)
SELECT
    customer_id,
    product_id
FROM RankedProducts
WHERE rnk = 1;
"""

# -----------------------------------------------------------------------------
# Test Cases
# -----------------------------------------------------------------------------

test_cases = [
    # Test Case 1: Basic scenario
    {
        'customers_data': [
            (1, 'Alice'),
            (2, 'Bob'),
            (3, 'Charlie')
        ],
        'orders_data': [
            (1, '2020-07-31', 1, 1),
            (2, '2020-07-30', 2, 2),
            (3, '2020-08-29', 3, 3),
            (4, '2020-07-29', 1, 2),
            (5, '2020-06-10', 1, 3),
            (6, '2020-08-01', 2, 1),
            (7, '2020-08-01', 3, 3),
            (8, '2020-08-03', 1, 2),
            (9, '2020-08-07', 2, 3),
            (10, '2020-07-15', 1, 2)
        ],
        'expected_output': [
            (1, 2), # Alice ordered product 2 three times (most frequent)
            (2, 1), # Bob ordered product 1 once
            (2, 2), # Bob ordered product 2 once
            (2, 3), # Bob ordered product 3 once (tie for Bob)
            (3, 3)  # Charlie ordered product 3 twice (most frequent)
        ]
    },
    # Test Case 2: Tie for most frequent product
    {
        'customers_data': [
            (10, 'David')
        ],
        'orders_data': [
            (11, '2023-01-01', 10, 101),
            (12, '2023-01-02', 10, 102),
            (13, '2023-01-03', 10, 101),
            (14, '2023-01-04', 10, 102)
        ],
        'expected_output': [
            (10, 101), # David ordered 101 twice
            (10, 102)  # David ordered 102 twice (tie)
        ]
    },
    # Test Case 3: Single order per customer
    {
        'customers_data': [
            (20, 'Eve'),
            (21, 'Frank')
        ],
        'orders_data': [
            (21, '2023-02-01', 20, 201),
            (22, '2023-02-02', 21, 202)
        ],
        'expected_output': [
            (20, 201),
            (21, 202)
        ]
    },
    # Test Case 4: One customer with multiple orders, another with none
    {
        'customers_data': [
            (30, 'Grace'),
            (31, 'Heidi')
        ],
        'orders_data': [
            (31, '2023-03-01', 30, 301),
            (32, '2023-03-02', 30, 302),
            (33, '2023-03-03', 30, 301)
            # Heidi has no orders
        ],
        'expected_output': [
            (30, 301) # Grace ordered 301 twice (most frequent)
        ]
    },
     # Test Case 5: No orders at all
    {
        'customers_data': [
            (40, 'Ivy'),
            (41, 'Judy')
        ],
        'orders_data': [],
        'expected_output': []
    },
    # Test Case 6: All orders for one product by one customer
    {
        'customers_data': [
            (50, 'Kevin')
        ],
        'orders_data': [
            (51, '2023-05-01', 50, 501),
            (52, '2023-05-02', 50, 501),
            (53, '2023-05-03', 50, 501)
        ],
        'expected_output': [
            (50, 501)
        ]
    },
    # Test Case 7: Complex ties
    {
        'customers_data': [
            (60, 'Liam'),
            (61, 'Mia')
        ],
        'orders_data': [
             # Liam: 10 (x3), 20 (x3), 30 (x2) -> Tie between 10 and 20
            (601, '2024-01-01', 60, 10),
            (602, '2024-01-02', 60, 20),
            (603, '2024-01-03', 60, 10),
            (604, '2024-01-04', 60, 30),
            (605, '2024-01-05', 60, 20),
            (606, '2024-01-06', 60, 10),
            (607, '2024-01-07', 60, 20),
            (608, '2024-01-08', 60, 30),
             # Mia: 40 (x2), 50 (x1) -> 40 is most frequent
            (611, '2024-01-10', 61, 40),
            (612, '2024-01-11', 61, 50),
            (613, '2024-01-12', 61, 40),
        ],
        'expected_output': [
            (60, 10),
            (60, 20),
            (61, 40)
        ]
    }
]

# -----------------------------------------------------------------------------
# Run the tests
# -----------------------------------------------------------------------------
run_sql_tests(sql_query, test_cases)