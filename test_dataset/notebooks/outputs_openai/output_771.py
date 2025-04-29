def count_jewels(jewels, stones):
    jewel_set = set(jewels)
    return sum(s in jewel_set for s in stones)

def run_tests():
    tests = [
        ({"jewels": "aA", "stones": "aAAbbbb"}, 3),
        ({"jewels": "z", "stones": "ZZ"}, 0),
    ]
    correct = 0
    total = len(tests)
    for test, expected in tests:
        output = count_jewels(**test)
        if output == expected:
            print(True)
            correct += 1
        else:
            print(False)
    print(f"{correct}/{total}")

run_tests()