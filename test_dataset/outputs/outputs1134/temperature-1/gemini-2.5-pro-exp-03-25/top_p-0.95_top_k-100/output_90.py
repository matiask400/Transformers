import sqlite3
import re # Although not used in the final sqlite approach, might be useful for other schema parsing tasks.

# --- Problem Description ---
# The task is to implement a Python function that can process a given SQL schema.
# Since no specific query or expected data output is provided, we will implement
# a function that performs a basic analysis of the schema: extracting all table names.
# The testing framework will then compare the list of extracted table names
# against an expected list for various schema inputs.

# --- Solution Function ---
def solve(schema_sql):
    """
    Parses the SQL schema and returns a sorted list of table names defined in it.

    Args:
        schema_sql (str): A string containing SQL CREATE TABLE statements.

    Returns:
        list: A sorted list of table names found in the schema.
              Returns an empty list if parsing fails or no tables are found.
    """
    table_names = []
    try:
        # Use an in-memory SQLite database to parse the schema
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()

        # Execute the schema script. This will create the tables in memory.
        # Using executescript handles multiple statements separated by semicolons.
        cursor.executescript(schema_sql)

        # Query the sqlite_master table (or sqlite_schema for newer versions)
        # to get the names of all user-defined tables.
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")

        # Fetch all results and extract the first column (table name)
        tables = cursor.fetchall()
        table_names = sorted([table[0] for table in tables])

        conn.close()

    except sqlite3.Error as e:
        # If there's an error parsing the SQL (e.g., syntax error),
        # print a message and return an empty list.
        # In a real application, better error handling might be needed.
        # print(f"Warning: Error processing schema: {e}") # Optional: uncomment for debugging
        return [] # Return empty list on error as per test case expectation

    return table_names

# --- Test Cases ---

# The example schema provided in the placeholder image/text
schema_provided = """
CREATE TABLE Highschooler (
    ID int PRIMARY KEY,
    name text,
    grade int
);

CREATE TABLE Friend (
    student_id int,
    friend_id int,
    PRIMARY KEY (student_id, friend_id),
    FOREIGN KEY (student_id) REFERENCES Highschooler(ID),
    FOREIGN KEY (friend_id) REFERENCES Highschooler(ID)
);

CREATE TABLE Likes (
    student_id int,
    liked_id int,
    PRIMARY KEY (student_id, liked_id),
    FOREIGN KEY (student_id) REFERENCES Highschooler(ID),
    FOREIGN KEY (liked_id) REFERENCES Highschooler(ID)
);
"""

# Define test cases
test_cases = [
    {
        "name": "Test Case 1: Provided Schema",
        "input": schema_provided,
        "expected": sorted(['Friend', 'Highschooler', 'Likes'])
    },
    {
        "name": "Test Case 2: Single Table",
        "input": "CREATE TABLE Student (id INT PRIMARY KEY, name TEXT);",
        "expected": sorted(['Student'])
    },
    {
        "name": "Test Case 3: Multiple Tables",
        "input": """
            CREATE TABLE Department (dept_id INT PRIMARY KEY, dept_name TEXT);
            CREATE TABLE Employee (emp_id INT PRIMARY KEY, emp_name TEXT, dept_id INT, FOREIGN KEY (dept_id) REFERENCES Department(dept_id));
            CREATE TABLE Project (proj_id INT PRIMARY KEY, proj_name TEXT);
        """,
        "expected": sorted(['Department', 'Employee', 'Project'])
    },
    {
        "name": "Test Case 4: Empty Schema",
        "input": "",
        "expected": []
    },
    {
        "name": "Test Case 5: Schema with Comments",
        "input": """
            -- This is a comment about the Course table
            CREATE TABLE Course (
                course_id TEXT PRIMARY KEY, -- Unique course identifier
                title TEXT,
                credits INT
            );
            /* Multi-line comment
               explaining the Enrollment table */
            CREATE TABLE Enrollment (
                student_id INT,
                course_id TEXT,
                grade CHAR(1),
                PRIMARY KEY (student_id, course_id) -- Composite key
                -- Foreign keys would normally go here
            );
        """,
        "expected": sorted(['Course', 'Enrollment'])
    },
    {
        "name": "Test Case 6: Case Sensitivity (SQLite default is case-insensitive for identifiers)",
        "input": """
            create table tableOne (col1 int);
            CREATE TABLE TABLETWO (col2 text);
        """,
        # SQLite typically stores table names as defined, but lookups are case-insensitive.
        # The sqlite_master query usually returns the original casing.
        "expected": sorted(['tableOne', 'TABLETWO'])
    },
     {
        "name": "Test Case 7: Invalid SQL Syntax",
        "input": "CREATE TABL Bogus (id INT);",
        # Expect the function to handle the error gracefully and return an empty list
        "expected": []
    },
    {
        "name": "Test Case 8: Schema with Quoted Identifiers",
        "input": """
            CREATE TABLE "My Table" ("My Column" INT PRIMARY KEY, description TEXT);
            CREATE TABLE `Another-Table` (`id` INT);
        """,
         # SQLite stores quoted identifiers including the quotes if they contain special chars or keywords.
         # The specific behavior can vary, but standard SQL would preserve case within quotes.
         # sqlite_master typically returns the name as stored (including quotes if needed).
         # Let's assume standard behavior where names are returned as created.
        "expected": sorted(['Another-Table', 'My Table'])
    }
]

# --- Test Runner ---
def run_tests(test_cases):
    """
    Runs the defined test cases against the solve function.
    """
    correct_count = 0
    total_tests = len(test_cases)

    for i, test in enumerate(test_cases):
        test_name = test.get("name", f"Test {i+1}")
        schema_input = test["input"]
        expected_output = test["expected"]

        # Run the solve function
        actual_output = solve(schema_input)

        # Compare actual vs expected
        is_correct = (actual_output == expected_output)

        # Print results
        print(f"{test_name}: {is_correct}")
        # Optional: Print details on failure
        # if not is_correct:
        #     print(f"  Input:\n{schema_input[:100]}...") # Print snippet of input
        #     print(f"  Expected: {expected_output}")
        #     print(f"  Actual:   {actual_output}")


        if is_correct:
            correct_count += 1

    print(f"\n{correct_count}/{total_tests} tests passed.")

# --- Main Execution ---
if __name__ == "__main__":
    run_tests(test_cases)