def remove_vowels(s):
    vowels = "aeiou"
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
        ("Aeiou", "Aeiou"),
        ("hello", "hll"),
        ("programming", "prgrmmng"),
        ("", "")
    ]

    correct_count = 0
    total_count = len(test_cases)

    for input_string, expected_output in test_cases:
        actual_output = remove_vowels(input_string)
        if actual_output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_remove_vowels()