from collections import Counter

def can_reorder_doubled(arr):
    count = Counter(arr)
    if len(arr) % 2 != 0:
        return False
    # Sort the keys based on absolute value
    for x in sorted(count.keys(), key=abs):
        if count[x] > count.get(2 * x, 0):
            return False
        count[2 * x] -= count[x]
    return True

def run_tests():
    tests = [
        {"input": [3,1,3,6], "output": False},
        {"input": [2,1,2,6], "output": False},
        {"input": [4,-2,2,-4], "output": True},
        {"input": [1,2,4,16,8,4], "output": False},
    ]
    correct = 0
    total = len(tests)
    for test in tests:
        result = can_reorder_doubled(test["input"])
        expected = test["output"]
        if result == expected:
            print("True")
            correct += 1
        else:
            print("False")
    print(f"{correct}/{total}")

run_tests()