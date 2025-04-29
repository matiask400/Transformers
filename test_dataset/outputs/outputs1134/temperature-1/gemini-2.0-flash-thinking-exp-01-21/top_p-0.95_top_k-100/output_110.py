def solve():
    def test_query(tables, query, expected_output):
        def execute_query(tables, query):
            lines = query.strip().split('\n')
            select_clause = lines[0].split('SELECT ')[1].split(' FROM ')[0].split(', ')
            from_clause = lines[0].split(' FROM ')[1].split(' WHERE ')[0] if ' WHERE ' in lines[0] else lines[0].split(' FROM ')[1]
            where_clause = lines[0].split(' WHERE ')[1] if ' WHERE ' in lines[0] else None

            table_data = tables[from_clause]
            result = []

            for row in table_data:
                if where_clause:
                    parts = where_clause.split(' = ')
                    column_name = parts[0]
                    value = parts[1].strip("'")

                    if column_name not in row:
                        continue

                    row_value = row[column_name]
                    if isinstance(row_value, str):
                        if row_value == value:
                            pass
                        else:
                            continue
                    elif isinstance(row_value, int):
                        try:
                            if row_value == int(value):
                                pass
                            else:
                                continue
                        except ValueError:
                            continue
                    else:
                        continue

                selected_row = tuple(row[col] for col in select_clause)
                result.append(selected_row)
            return result

        actual_output = execute_query(tables, query)

        def normalize_output(output):
            return sorted(list(output))

        normalized_actual = normalize_output(actual_output)
        normalized_expected = normalize_output(expected_output)

        return normalized_actual == normalized_expected

    test_cases = [
        {
            "tables": {
                "Students": [
                    {'sid': 101, 'sname': 'Alice', 'major': 'CS', 'age': 20},
                    {'sid': 102, 'sname': 'Bob', 'major': 'Math', 'age': 21},
                    {'sid': 103, 'sname': 'Charlie', 'major': 'CS', 'age': 19}
                ]
            },
            "query": "SELECT sname FROM Students WHERE major = 'CS'",
            "expected_output": [('Alice',), ('Charlie',)]
        },
        {
            "tables": {
                "Students": [
                    {'sid': 101, 'sname': 'Alice', 'major': 'CS', 'age': 20},
                    {'sid': 102, 'sname': 'Bob', 'major': 'Math', 'age': 21},
                    {'sid': 103, 'sname': 'Charlie', 'major': 'CS', 'age': 19},
                    {'sid': 104, 'sname': 'David', 'major': 'Physics', 'age': 22}
                ]
            },
            "query": "SELECT sname, age FROM Students WHERE age > 20",
            "expected_output": [('Bob', 21), ('David', 22)]
        },
        {
            "tables": {
                "Courses": [
                    {'cid': 'CS101', 'cname': 'Intro to CS', 'credits': 3},
                    {'cid': 'MA201', 'cname': 'Linear Algebra', 'credits': 4},
                    {'cid': 'PH101', 'cname': 'Physics I', 'credits': 4}
                ]
            },
            "query": "SELECT cname FROM Courses WHERE credits = 4",
            "expected_output": [('Linear Algebra',), ('Physics I',)]
        },
         {
            "tables": {
                "Enrolled": [
                    {'sid': 101, 'cid': 'CS101', 'grade': 'A'},
                    {'sid': 102, 'cid': 'MA201', 'grade': 'B'},
                    {'sid': 101, 'cid': 'MA201', 'grade': 'C'},
                    {'sid': 103, 'cid': 'PH101', 'grade': 'A'}
                ]
            },
            "query": "SELECT cid, grade FROM Enrolled WHERE sid = 101",
            "expected_output": [('CS101', 'A'), ('MA201', 'C')]
        },
        {
            "tables": {
                "Students": [
                    {'sid': 101, 'sname': 'Alice', 'major': 'CS', 'age': 20},
                    {'sid': 102, 'sname': 'Bob', 'major': 'Math', 'age': 21}
                ],
                "Enrolled": [
                    {'sid': 101, 'cid': 'CS101', 'grade': 'A'},
                    {'sid': 102, 'cid': 'MA201', 'grade': 'B'}
                ]
            },
            "query": "SELECT sname FROM Students WHERE sid = 102",
            "expected_output": [('Bob',)]
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        result = test_query(test_case["tables"], test_case["query"], test_case["expected_output"])
        if result:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")

    print(f"Correct tests: {correct_tests} over {total_tests}")

solve()