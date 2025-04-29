def isPalindrome(x):
    if x < 0:
        return False
    original = x
    reversed_num = 0
    while x != 0:
        reversed_num = reversed_num * 10 + x % 10
        x = x // 10
    return original == reversed_num

tests = [
    (121, True),
    (-121, False),
    (10, False),
    (-101, False)
]

correct = 0
for x, expected in tests:
    result = isPalindrome(x)
    if result == expected:
        print(True)
        correct += 1
    else:
        print(False)
print(f"{correct}/{len(tests)}")