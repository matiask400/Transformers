def reorder_logs(logs):
    letter_logs = []
    digit_logs = []
    for log in logs:
        words = log.split()
        if words[1].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(log)

    letter_logs.sort(key=lambda x: (x.split(maxsplit=1)[1], x.split()[0]))
    return letter_logs + digit_logs

def test_reorder_logs():
    tests = [
        {
            "input": ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"],
            "expected": ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
        },
        {
            "input": ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"],
            "expected": ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
        },
        {
            "input": ["j mo", "5 m w", "g 6 u", "t q h", "r 0 e", "u 2 o"],
            "expected": ["j mo", "t q h", "5 m w", "g 6 u", "r 0 e", "u 2 o"]
        },
         {
            "input": ["a 1 9", "b 9 5 0", "pica 3 1", "jean 4 2"],
            "expected": ["pica 3 1", "jean 4 2", "a 1 9", "b 9 5 0"]
         }

    ]

    correct_count = 0
    total_tests = len(tests)

    for i, test in enumerate(tests):
        input_logs = test["input"]
        expected_output = test["expected"]
        actual_output = reorder_logs(input_logs)

        if actual_output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_tests}")


if __name__ == "__main__":
    test_reorder_logs()