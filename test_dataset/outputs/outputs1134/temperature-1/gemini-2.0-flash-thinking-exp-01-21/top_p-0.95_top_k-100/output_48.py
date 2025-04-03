def magicalString(n):
    if n <= 0:
        return 0
    s = [1, 2, 2]
    index = 2
    next_digit = 1
    while len(s) < n:
        count = s[index]
        for _ in range(count):
            s.append(next_digit)
        index += 1
        next_digit = 3 - next_digit
    count1 = 0
    for i in range(n):
        if s[i] == 1:
            count1 += 1
    return count1

def test_magicalString():
    test_cases = [
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 3),
        (6, 3),
        (7, 4),
        (10, 4),
        (15, 6),
        (20, 9),
    ]
    correct_tests = 0
    total_tests = len(test_cases)
    for input_n, expected_output in test_cases:
        actual_output = magicalString(input_n)
        if actual_output == expected_output:
            print('True')
            correct_tests += 1
        else:
            print('False')
    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    test_magicalString()