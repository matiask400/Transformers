def count_substrings(s: str) -> int:
    count = {'a':0, 'b':0, 'c':0}
    left = 0
    result = 0
    for right in range(len(s)):
        if s[right] in count:
            count[s[right]] += 1
        while all(count[char] > 0 for char in count):
            result += len(s) - right
            if s[left] in count:
                count[s[left]] -= 1
            left += 1
    return result

def run_tests():
    tests = [
        ("abcabc", 10),
        ("aaacb", 3),
        ("abc", 1),
    ]
    correct = 0
    total = len(tests)
    for i, (input_str, expected) in enumerate(tests):
        output = count_substrings(input_str)
        if output == expected:
            print('True')
            correct += 1
        else:
            print('False')
    print(f"{correct}/{total}")

run_tests()