def remove_vowels(s):
    vowels = set('aeiou')
    return ''.join([char for char in s if char not in vowels])

def run_tests():
    test_cases = [
        {
            'input': "leetcodeisacommunityforcoders",
            'expected': "ltcdscmmntyfrcdrs"
        },
        {
            'input': "aeiou",
            'expected': ""
        },
        {
            'input': "helloworld",
            'expected': "hellwrld"
        },
        {
            'input': "python",
            'expected': "pythn"
        },
        {
            'input': "bcdfghjklmnpqrstvwxyz",
            'expected': "bcdfghjklmnpqrstvwxyz"
        },
        {
            'input': "a",
            'expected': ""
        },
        {
            'input': "b",
            'expected': "b"
        },
        {
            'input': "aaaabbbb",
            'expected': "bbbb"
        },
        {
            'input': "xyz",
            'expected': "xyz"
        }
    ]
    correct = 0
    total = len(test_cases)
    for case in test_cases:
        input_str = case['input']
        expected = case['expected']
        output = remove_vowels(input_str)
        if output == expected:
            print(True)
            correct +=1
        else:
            print(False)
    print(f"{correct}/{total}")

run_tests()