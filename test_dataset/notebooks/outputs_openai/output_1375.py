def numTimesAllBlue(light):
    count = 0
    max_on = 0
    for i, bulb in enumerate(light, 1):
        max_on = max(max_on, bulb)
        if max_on == i:
            count +=1
    return count

def run_tests():
    tests = [
        {"light": [2,1,3,5,4], "expected": 3},
        {"light": [3,2,4,1,5], "expected": 2},
        {"light": [4,1,2,3], "expected": 1},
        {"light": [2,1,4,3,6,5], "expected": 3},
        {"light": [1,2,3,4,5,6], "expected": 6},
    ]
    correct = 0
    total = len(tests)
    for test in tests:
        result = numTimesAllBlue(test["light"])
        if result == test["expected"]:
            print(True)
            correct +=1
        else:
            print(False)
    print(f"{correct}/{total}")

run_tests()