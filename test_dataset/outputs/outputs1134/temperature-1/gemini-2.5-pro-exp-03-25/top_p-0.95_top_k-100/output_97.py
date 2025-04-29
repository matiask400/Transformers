import sys
from io import StringIO

def remove_vowels(s: str) -> str:
    """
    Removes the vowels 'a', 'e', 'i', 'o', 'u' from a string.

    Args:
        s: The input string, consisting of only lowercase English letters.

    Returns:
        A new string with all vowels removed.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    # Use a generator expression with join for efficiency
    return "".join(char for char in s if char not in vowels)

# --- Testing Framework ---

def run_tests():
    """
    Runs predefined test cases against the remove_vowels function and prints the results.
    """
    test_cases = [
        # Example Cases
        {"input": "leetcodeisacommunityforcoders", "expected": "ltcdscmmntyfrcdrs"},
        {"input": "aeiou", "expected": ""},

        # Additional Cases
        {"input": "python", "expected": "pythn"},
        {"input": "programming", "expected": "prgrmmng"},
        {"input": "xyz", "expected": "xyz"}, # No vowels
        {"input": "a", "expected": ""},      # Single vowel
        {"input": "b", "expected": "b"},      # Single consonant
        {"input": "aeiouaeiouaeiou", "expected": ""}, # Only vowels
        {"input": "rhythm", "expected": "rhythm"}, # Word without standard vowels
        {"input": "strength", "expected": "strngth"},
        {"input": "bookkeeper", "expected": "bkkpr"},
        {"input": "mississippi", "expected": "mssssrpp"},

        # Constraint Cases
        {"input": "q"*1000, "expected": "q"*1000}, # Max length, no vowels
        {"input": "u"*1000, "expected": ""},       # Max length, only vowels
        {"input": ("ab"*500), "expected": "b"*500}, # Max length, mixed
    ]

    correct_count = 0
    total_tests = len(test_cases)

    # Redirect stdout to capture prints within the loop if needed,
    # but here we just print directly.
    original_stdout = sys.stdout
    # captured_output = StringIO()
    # sys.stdout = captured_output

    for i, test in enumerate(test_cases):
        input_s = test["input"]
        expected_output = test["expected"]

        # Ensure input constraints are met for the test case (optional, good practice)
        if not (1 <= len(input_s) <= 1000 and all('a' <= char <= 'z' for char in input_s)):
             print(f"Test {i+1} skipped: Input '{input_s}' violates constraints.")
             total_tests -= 1 # Adjust total count if skipping
             continue

        try:
            actual_output = remove_vowels(input_s)
            result = actual_output == expected_output
            print(f"{result}") # Print True or False directly
            if result:
                correct_count += 1
        except Exception as e:
            print(f"Test {i+1} failed with exception: {e}")
            # Optionally print False here as well
            # print(f"False")


    # Restore stdout
    # sys.stdout = original_stdout
    # print(captured_output.getvalue()) # Print all captured True/False

    # Print the final summary
    print(f"{correct_count}/{total_tests}")

if __name__ == "__main__":
    run_tests()