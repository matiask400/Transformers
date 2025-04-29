def numJewelsInStones(jewels: str, stones: str) -> int:
    """
    Given strings jewels representing the types of stones that are jewels, and stones
    representing the stones you have, return how many of the stones you have are also jewels.

    Letters are case sensitive, so "a" is considered a different type of stone from "A".

    Example 1:
    Input: jewels = "aA", stones = "aAAbbbb"
    Output: 3

    Example 2:
    Input: jewels = "z", stones = "ZZ"
    Output: 0

    Constraints:
    1 <= jewels.length, stones.length <= 50
    jewels and stones consist of only English letters.
    All the characters of jewels are unique.
    """
    jewel_set = set(jewels)
    count = 0
    for stone in stones:
        if stone in jewel_set:
            count += 1
    return count

def test_numJewelsInStones():
    test_cases = [
        {"jewels": "aA", "stones": "aAAbbbb", "expected": 3},
        {"jewels": "z", "stones": "ZZ", "expected": 0},
        {"jewels": "abc", "stones": "def", "expected": 0},
        {"jewels": "Ab", "stones": "aabbAA", "expected": 4},
        {"jewels": "K", "stones": "KKKKKKK", "expected": 7},
        {"jewels": "a", "stones": "aaaaabbbbb", "expected": 5},
        {"jewels": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "stones": "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ", "expected": 52},
        {"jewels": "", "stones": "abc", "expected": 0},
        {"jewels": "abc", "stones": "", "expected": 0},
        {"jewels": "j", "stones": "jjjjjjJ", "expected": 6},
    ]

    correct_tests = 0
    for i, test_case in enumerate(test_cases):
        result = numJewelsInStones(test_case["jewels"], test_case["stones"])
        if result == test_case["expected"]:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")

    print(f"\n{correct_tests}/{len(test_cases)}")

if __name__ == '__main__':
    test_numJewelsInStones()