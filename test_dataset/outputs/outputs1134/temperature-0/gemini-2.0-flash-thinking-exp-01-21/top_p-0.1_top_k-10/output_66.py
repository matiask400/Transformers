def num_jewels_in_stones(jewels: str, stones: str) -> int:
    """
    Counts how many stones are jewels.

    Args:
        jewels: A string representing the types of stones that are jewels.
        stones: A string representing the stones you have.

    Returns:
        The number of stones that are also jewels.
    """
    jewel_set = set(jewels)
    count = 0
    for stone in stones:
        if stone in jewel_set:
            count += 1
    return count

def run_tests():
    tests = [
        {"jewels": "aA", "stones": "aAAbbbb", "expected": 3},
        {"jewels": "z", "stones": "ZZ", "expected": 0},
        {"jewels": "abc", "stones": "def", "expected": 0},
        {"jewels": "AbC", "stones": "AAAbbbCCC", "expected": 6},
        {"jewels": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "stones": "石头", "expected": 0},
        {"jewels": "a", "stones": "aaaaaaaaaa", "expected": 10},
        {"jewels": "A", "stones": "AAAAAAAAAA", "expected": 10},
        {"jewels": "", "stones": "abc", "expected": 0},
        {"jewels": "abc", "stones": "", "expected": 0},
    ]

    correct_tests = 0
    for i, test in enumerate(tests):
        result = num_jewels_in_stones(test["jewels"], test["stones"])
        if result == test["expected"]:
            print(True)
            correct_tests += 1
        else:
            print(False)

    print(f"{correct_tests}/{len(tests)}")

if __name__ == '__main__':
    run_tests()