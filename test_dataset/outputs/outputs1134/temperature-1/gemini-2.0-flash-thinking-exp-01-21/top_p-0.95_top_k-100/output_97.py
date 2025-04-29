def remove_vowels(s):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    new_string = ""
    for char in s:
        if char not in vowels:
            new_string += char
    return new_string

def test_remove_vowels():
    test_cases = [
        ("leetcodeisacommunityforcoders", "ltcdscmmntyfrcdrs"),
        ("aeiou", ""),
        ("bcdfghjklmnpqrstvwxyz", "bcdfghjklmnpqrstvwxyz"),
        ("Aeiou", "Aiou"), # should only remove lowercase vowels based on problem description
        ("", ""),
        ("programming", "prgrmmng"),
        ("string", "strng"),
        ("vowels", "vwls"),
        ("consonants", "cnsnnts"),
        ("hello world", "hll wrld")
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for input_str, expected_output in test_cases:
        actual_output = remove_vowels(input_str)
        if actual_output == expected_output:
            print('True')
            correct_tests += 1
        else:
            print('False')
    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    test_remove_vowels()