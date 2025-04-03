import sqlite3

def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def compare_output(actual_output, expected_output):
    if actual_output == expected_output:
        return True
    return False

def test_sql_query(schema, test_data, query, expected_output):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Execute schema
    cursor.executescript(schema)

    # Execute test data
    cursor.executescript(test_data)

    # Execute query
    actual_output = execute_query(conn, query)

    conn.close()

    return compare_output(actual_output, expected_output), actual_output


def run_tests(test_cases):
    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        schema = test_case['schema']
        test_data = test_case['test_data']
        query = test_case['query']
        expected_output = test_case['expected_output']

        test_passed, actual_output = test_sql_query(schema, test_data, query, expected_output)

        if test_passed:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Actual Output: {actual_output}")
            print(f"  Expected Output: {expected_output}")

    print(f"\n{correct_tests}/{total_tests}")


if __name__ == '__main__':
    test_cases = [
        {
            'schema': """
                CREATE TABLE Employees (
                    emp_id INT PRIMARY KEY,
                    name VARCHAR(50),
                    department VARCHAR(50)
                );
            """,
            'test_data': """
                INSERT INTO Employees (emp_id, name, department) VALUES
                (1, 'Alice', 'Sales'),
                (2, 'Bob', 'Marketing'),
                (3, 'Charlie', 'Sales');
            """,
            'query': "SELECT department, COUNT(*) FROM Employees GROUP BY department;",
            'expected_output': [('Marketing', 1), ('Sales', 2)]
        },
        {
            'schema': """
                CREATE TABLE Students (
                    student_id INT PRIMARY KEY,
                    name VARCHAR(50),
                    major VARCHAR(50)
                );
            """,
            'test_data': """
                INSERT INTO Students (student_id, name, major) VALUES
                (101, 'Alice', 'Computer Science'),
                (102, 'Bob', 'Physics'),
                (103, 'Charlie', 'Computer Science'),
                (104, 'David', 'Biology');
            """,
            'query': "SELECT major, COUNT(*) FROM Students GROUP BY major ORDER BY major;",
            'expected_output': [('Biology', 1), ('Computer Science', 2), ('Physics', 1)]
        },
        {
            'schema': """
                CREATE TABLE Products (
                    product_id INT PRIMARY KEY,
                    name VARCHAR(50),
                    price DECIMAL(10, 2)
                );
            """,
            'test_data': """
                INSERT INTO Products (product_id, name, price) VALUES
                (1, 'Laptop', 1200.00),
                (2, 'Mouse', 25.00),
                (3, 'Keyboard', 75.00),
                (4, 'Monitor', 300.00);
            """,
            'query': "SELECT AVG(price) FROM Products;",
            'expected_output': [(400.0,)] # Average price
        },
        {
            'schema': """
                CREATE TABLE Orders (
                    order_id INT PRIMARY KEY,
                    customer_id INT,
                    order_date DATE,
                    total_amount DECIMAL(10, 2)
                );
            """,
            'test_data': """
                INSERT INTO Orders (order_id, customer_id, order_date, total_amount) VALUES
                (1, 1001, '2023-01-15', 150.00),
                (2, 1002, '2023-02-20', 200.00),
                (3, 1001, '2023-03-25', 100.00);
            """,
            'query': "SELECT customer_id, SUM(total_amount) FROM Orders GROUP BY customer_id;",
            'expected_output': [(1001, 250.0), (1002, 200.0)]
        },
        {
            'schema': """
                CREATE TABLE Departments (
                    dept_id INT PRIMARY KEY,
                    dept_name VARCHAR(50)
                );
                CREATE TABLE Employees (
                    emp_id INT PRIMARY KEY,
                    emp_name VARCHAR(50),
                    dept_id INT,
                    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
                );
            """,
            'test_data': """
                INSERT INTO Departments (dept_id, dept_name) VALUES
                (1, 'Sales'),
                (2, 'Marketing');
                INSERT INTO Employees (emp_id, emp_name, dept_id) VALUES
                (1, 'Alice', 1),
                (2, 'Bob', 2),
                (3, 'Charlie', 1);
            """,
            'query': "SELECT d.dept_name, COUNT(e.emp_id) FROM Departments d LEFT JOIN Employees e ON d.dept_id = e.dept_id GROUP BY d.dept_name ORDER BY d.dept_name;",
            'expected_output': [('Marketing', 1), ('Sales', 2)]
        },
        {
            'schema': """
                CREATE TABLE Students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    grade TEXT
                );
            """,
            'test_data': """
                INSERT INTO Students (name, age, grade) VALUES
                ('Alice', 10, '5th'),
                ('Bob', 11, '6th'),
                ('Charlie', 10, '5th');
            """,
            'query': "SELECT grade, COUNT(*) FROM Students WHERE age = 10 GROUP BY grade;",
            'expected_output': [('5th', 2)]
        },
         {
            'schema': """
                CREATE TABLE Sales (
                    sale_id INTEGER PRIMARY KEY,
                    product_name TEXT,
                    quantity INTEGER,
                    price REAL
                );
            """,
            'test_data': """
                INSERT INTO Sales (product_name, quantity, price) VALUES
                ('Apple', 10, 1.0),
                ('Banana', 20, 0.5),
                ('Apple', 5, 1.0),
                ('Orange', 15, 0.75);
            """,
            'query': "SELECT product_name, SUM(quantity) FROM Sales GROUP BY product_name ORDER BY product_name;",
            'expected_output': [('Apple', 15), ('Banana', 20), ('Orange', 15)]
        },
        {
            'schema': """
                CREATE TABLE Books (
                    book_id INTEGER PRIMARY KEY,
                    title TEXT,
                    author TEXT,
                    genre TEXT
                );
            """,
            'test_data': """
                INSERT INTO Books (title, author, genre) VALUES
                ('The Lord of the Rings', 'J.R.R. Tolkien', 'Fantasy'),
                ('Pride and Prejudice', 'Jane Austen', 'Romance'),
                ('Harry Potter', 'J.K. Rowling', 'Fantasy'),
                ('Emma', 'Jane Austen', 'Romance');
            """,
            'query': "SELECT genre, COUNT(*) FROM Books GROUP BY genre HAVING COUNT(*) > 1 ORDER BY genre;",
            'expected_output': [('Fantasy', 2), ('Romance', 2)]
        }

    ]

    run_tests(test_cases)