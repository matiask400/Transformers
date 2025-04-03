def max_balanced_splits(s):
    count = 0
    balance = 0
    for c in s:
        if c == 'L':
            balance -= 1
        elif c == 'R':
            balance += 1
        if balance == 0:
            count += 1
    return count

def run_tests():
    tests = [
        ("RLRRLLRLRL", 4),
        ("RLLLLRRRLR", 3),
        ("LLLLRRRR", 1),
        ("RLRRRLLRLL", 2),
    ]
    correct = 0
    for s, expected in tests:
        result = max_balanced_splits(s)
        if result == expected:
            print("True")
            correct +=1
        else:
            print("False")
    print(f"{correct}/{len(tests)}")

run_tests()