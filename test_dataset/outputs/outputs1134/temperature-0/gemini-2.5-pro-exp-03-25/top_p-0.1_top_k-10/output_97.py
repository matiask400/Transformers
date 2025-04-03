import sys

def removeVowels(s: str) -> str:
    """
    Removes vowels ('a', 'e', 'i', 'o', 'u') from a string.

    Args:
        s: The input string.

    Returns:
        The string with vowels removed.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    # Use a generator expression within join for efficiency.
    # It iterates through the string once, building the result.
    return "".join(char for char in s if char not in vowels)

# List of test cases, each is a tuple (input_string, expected_output)
test_cases = [
    ("leetcodeisacommunityforcoders", "ltcdscmmntyfrcdrs"),
    ("aeiou", ""),
    ("python", "pythn"),
    ("programming", "prgrmmng"),
    ("xyz", "xyz"),
    ("a", ""),
    ("b", "b"),
    ("aeiouaeiou", ""),
    ("abababab", "bbbbbb"),
    ("mississippi", "msssstpp"),
    ("strength", "strngth"),
    ("rhythm", "rhythm"), # String with no vowels
    ("bookkeeper", "bkkpr"),
]

# Function to run tests
def run_tests():
    """
    Runs the test cases against the removeVowels function and prints the results.
    """
    correct_tests = 0
    total_tests = len(test_cases)

    for i, (input_s, expected_output) in enumerate(test_cases):
        # Call the student's function
        actual_output = removeVowels(input_s)

        # Compare the actual output with the expected output
        passed = actual_output == expected_output
        print(passed) # Print True or False for each test

        if passed:
            correct_tests += 1

    # Print the final summary
    print(f"{correct_tests}/{total_tests}")

# Execute the tests
if __name__ == "__main__":
    run_tests()