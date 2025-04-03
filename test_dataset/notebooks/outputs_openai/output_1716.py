def totalMoney(n):
    total = 0
    for day in range(1, n + 1):
        week_number = (day - 1) // 7
        day_of_week = (day - 1) % 7 + 1
        amount = week_number + day_of_week
        total += amount
    return total

def run_tests():
    test_cases = [
        (4, 10),
        (10, 37),
        (20, 96)
    ]
    correct = 0
    total_tests = len(test_cases)
    for inp, expected in test_cases:
        result = totalMoney(inp)
        if result == expected:
            print('True')
            correct += 1
        else:
            print('False')
    print(f"{correct}/{total_tests}")

run_tests()