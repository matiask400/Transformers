def add_thousands_separator(n):
    s = str(n)
    result = ''
    count = 0
    for i in range(len(s)-1, -1, -1):
        result = s[i] + result
        count +=1
        if count ==3 and i !=0:
            result = '.' + result
            count =0
    return result

def run_tests():
    test_cases = [
        (987, "987"),
        (1234, "1.234"),
        (123456789, "123.456.789"),
        (0, "0")
    ]
    correct = 0
    total = len(test_cases)
    for n, expected in test_cases:
        output = add_thousands_separator(n)
        is_correct = output == expected
        print(is_correct)
        if is_correct:
            correct +=1
    print(f"{correct}/{total}")

run_tests()