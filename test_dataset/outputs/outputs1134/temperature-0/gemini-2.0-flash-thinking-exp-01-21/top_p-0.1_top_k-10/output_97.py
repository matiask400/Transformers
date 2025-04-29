def remove_vowels(s):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    new_string = ""
    for char in s:
        if char not in vowels:
            new_string += char
    return new_string

def test_remove_vowels():
    test_cases = [
        {"input": "leetcodeisacommunityforcoders", "expected_output": "ltcdscmmntyfrcdrs"},
        {"input": "aeiou", "expected_output": ""},
        {"input": "bcdfghjklmnpqrstvwxyz", "expected_output": "bcdfghjklmnpqrstvwxyz"},
        {"input": "", "expected_output": ""},
        {"input": "programming", "expected_output": "prgrammng"}
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        input_s = test_case["input"]
        expected_output = test_case["expected_output"]
        actual_output = remove_vowels(input_s)
        if actual_output == expected_output:
            print(True)
            correct_tests += 1
        else:
            print(False)

    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    test_remove_vowels()