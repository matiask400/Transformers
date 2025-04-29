def reorder_logs(logs):
    letter_logs = []
    digit_logs = []
    for log in logs:
        parts = log.split(' ', 1)
        identifier = parts[0]
        content = parts[1]
        is_digit_log = True
        for char in content.split():
            if not char.isdigit():
                is_digit_log = False
                break
        if is_digit_log:
            digit_logs.append(log)
        else:
            letter_logs.append({'identifier': identifier, 'content': content, 'original': log})

    letter_logs.sort(key=lambda x: (x['content'], x['identifier']))

    sorted_letter_log_strings = [log['original'] for log in letter_logs]

    return sorted_letter_log_strings + digit_logs

def run_tests():
    test_cases = [
        {
            "input": ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"],
            "expected": ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
        },
        {
            "input": ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"],
            "expected": ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
        },
        {
            "input": ["j mo", "5 sl", "5 gc", "t kr"],
            "expected": ["j mo", "t kr", "5 sl", "5 gc"]
        },
        {
            "input": ["mi2 jog mid pet", "wz3 34 54 39", "t2 90 12 13", "j9 saw steed wonder"],
            "expected": ["mi2 jog mid pet", "j9 saw steed wonder", "wz3 34 54 39", "t2 90 12 13"]
        }
    ]

    num_correct = 0
    for i, test_case in enumerate(test_cases):
        actual_output = reorder_logs(test_case["input"])
        if actual_output == test_case["expected"]:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: {test_case['input']}")
            print(f"  Expected: {test_case['expected']}")
            print(f"  Actual: {actual_output}")

    print(f"\n{num_correct} correct out of {len(test_cases)}")

if __name__ == '__main__':
    run_tests()