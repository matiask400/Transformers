import sys
from typing import List

# Core solution function
def reorderLogFiles(logs: List[str]) -> List[str]:
    """
    Reorders an array of logs according to the specified rules:
    1. Letter-logs come before all digit-logs.
    2. Letter-logs are sorted lexicographically by their contents.
       If contents are the same, sort by identifier.
    3. Digit-logs maintain their relative ordering.

    Args:
        logs: A list of strings, where each string is a log entry.

    Returns:
        A list of strings representing the reordered logs.
    """

    def get_sort_key(log: str):
        """
        Generates a sort key for a given log string.
        The key determines the log's type and sorting order.
        - Letter-logs get a key like (0, content, identifier).
        - Digit-logs get a key like (1,).
        This ensures letter-logs come first (0 < 1) and are sorted correctly.
        Digit-logs maintain relative order due to the stable sort and equal keys.
        """
        # Split the log into identifier and the rest (content)
        # ' ' is the delimiter, maxsplit=1 ensures only the first space is split
        identifier, rest = log.split(' ', 1)

        # Check if the first character of the content part is a digit.
        # Based on constraints, if the first word starts with a digit,
        # all content words are digits, making it a digit-log.
        # Otherwise, it's a letter-log.
        if rest[0].isdigit():
            # It's a digit-log.
            # Return a key tuple starting with 1. All digit-logs will have
            # this primary key. Python's sort stability ensures their
            # relative order is maintained.
            return (1,)
        else:
            # It's a letter-log.
            # Return a key tuple starting with 0 (to come before digit-logs).
            # The secondary sort key is the content ('rest').
            # The tertiary sort key is the identifier.
            return (0, rest, identifier)

    # Use Python's built-in sorted() function with the custom key.
    # sorted() is stable, which is essential for preserving the
    # relative order of digit-logs.
    sorted_logs = sorted(logs, key=get_sort_key)
    return sorted_logs

# Test runner function
def run_tests():
    """
    Runs predefined test cases against the reorderLogFiles function,
    prints 'True' or 'False' for each test, and finally prints the
    fraction of tests passed.
    """
    test_cases = [
        # Example 1 from description
        (
            ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"],
            ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
        ),
        # Example 2 from description
        (
            ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"],
            ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
        ),
        # Test case with mixed logs, including single-letter identifier
        (
            ["1 n u", "r 527", "j 893", "6 14", "6 82"],
            ["1 n u", "r 527", "j 893", "6 14", "6 82"] # letter log first, digits maintain order
        ),
        # Another mixed test case
         (
            ["t kvr", "r 3 1", "i 403", "7 so", "t 54"],
            ["7 so", "t kvr", "r 3 1", "i 403", "t 54"] # letter logs sorted, digits maintain order
         ),
         # Test case: Letter-logs with identical content, sort by identifier
         (
             ["let2 art can", "let1 art can"],
             ["let1 art can", "let2 art can"]
         ),
          # Test case: Letter-logs with identical content, different order
         (
             ["let1 art can", "let2 art can"],
             ["let1 art can", "let2 art can"] # Already sorted by identifier
         ),
         # Test case: Only digit-logs, maintain relative order
         (
             ["dig2 7", "dig1 8"],
             ["dig2 7", "dig1 8"]
         ),
         # Test case: Only letter-logs, sort correctly
         (
             ["let3 zeta", "let1 alpha", "let2 beta"],
             ["let1 alpha", "let2 beta", "let3 zeta"]
         ),
         # Test case: Single letter-log
         (
             ["let1 art can"],
             ["let1 art can"]
         ),
         # Test case: Single digit-log
         (
             ["dig1 1 2 3"],
             ["dig1 1 2 3"]
         ),
         # Test case: Letter logs with same first word in content
         (
            ["a1 art can", "a2 art bat"],
            ["a2 art bat", "a1 art can"]
         )
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    # Iterate through test cases, execute the solution, and compare results
    for i, (logs_input, expected_output) in enumerate(test_cases):
        # Execute the function with the test input
        actual_output = reorderLogFiles(logs_input)
        # Compare the actual output with the expected output
        passed = actual_output == expected_output
        # Print True/False for the current test case
        print(f"{passed}")
        # Increment the count of correct tests if passed
        if passed:
            correct_tests += 1

    # Print the final summary score
    print(f"\n{correct_tests} / {total_tests}")

# Execute the test runner function when the script is run
if __name__ == "__main__":
    run_tests()