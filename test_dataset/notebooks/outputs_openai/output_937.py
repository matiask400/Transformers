def reorder_logs(logs):
    letter_logs = []
    digit_logs = []
    for log in logs:
        parts = log.split()
        identifier, rest = parts[0], parts[1:]
        if rest[0].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append((rest, identifier, log))
    letter_logs_sorted = sorted(letter_logs, key=lambda x: (x[0], x[1]))
    sorted_letter_logs = [x[2] for x in letter_logs_sorted]
    return sorted_letter_logs + digit_logs

# Test cases
test_cases = [
    (
        ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"],
        ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    ),
    (
        ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"],
        ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
    )
]

correct = 0
total = len(test_cases)

for idx, (logs, expected) in enumerate(test_cases):
    output = reorder_logs(logs)
    result = output == expected
    print(result)
    if result:
        correct += 1

print(f"{correct}/{total}")