def largeGroupPositions(s):
    res = []
    n = len(s)
    i = 0
    for j in range(n):
        if j == n - 1 or s[j] != s[j + 1]:
            if j - i + 1 >= 3:
                res.append([i, j])
            i = j + 1
    return res

# Define test cases
test_cases = [
    {"input": "abbxxxxzzy", "expected": [[3,6]]},
    {"input": "abc", "expected": []},
    {"input": "abcdddeeeeaabbbcd", "expected": [[3,5],[6,9],[12,14]]},
    {"input": "aba", "expected": []},
]

# Run tests
correct = 0
for tc in test_cases:
    output = largeGroupPositions(tc["input"])
    if output == tc["expected"]:
        print("True")
        correct += 1
    else:
        print("False")
print(f"{correct}/{len(test_cases)}")