import sys
import io

def reorderLogFiles(logs: list[str]) -> list[str]:
    """
    Reorders logs according to the specified rules:
    1. Letter-logs come before digit-logs.
    2. Letter-logs are sorted lexicographically by content, then by identifier.
    3. Digit-logs maintain their relative order.

    Args:
        logs: A list of log strings.

    Returns:
        A list of reordered log strings.
    """

    def get_sort_key(log):
        # Split the log into identifier and the rest (content)
        # Use maxsplit=1 to handle cases where content might have spaces
        identifier, rest = log.split(" ", 1)

        # Check if the first character of the content part is a digit
        if rest[0].isdigit():
            # It's a digit-log. Return a tuple that places it after letter-logs.
            # The second element (0) is arbitrary but needed for tuple structure.
            # Since we rely on stable sort for relative order, the exact value here
            # doesn't matter as long as it's consistent for all digit-logs.
            # We don't need to include the original index because Python's sort is stable.
            return (1, None, None) # Type 1 for digit-logs
        else:
            # It's a letter-log. Return a tuple for sorting:
            # (type, content, identifier)
            # Type 0 ensures letter-logs come before digit-logs (type 1).
            # Sorting is then done by content (rest), then by identifier.
            return (0, rest, identifier) # Type 0 for letter-logs

    # Sort the logs using the custom key function.
    # Python's sort is stable, which automatically preserves the relative order
    # of elements that compare as equal (like all digit-logs based on our key).
    logs.sort(key=get_sort_key)
    return logs

# --- Testing Framework ---

def run_tests():
    """
    Runs predefined test cases against the reorderLogFiles function and prints the results.
    """
    test_cases = [
        (
            ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"],
            ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
        ),
        (
            ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"],
            ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
        ),
        (
            ["1 n u", "r 527", "j 893", "6 14", "6 82"],
             ["1 n u", "r 527", "j 893", "6 14", "6 82"] # Letter log first, digits maintain order
        ),
        (
             ["t kvr", "r 3 1", "i 403", "7 so", "t 54"],
             ["7 so", "t kvr", "r 3 1", "i 403", "t 54"] # Letter logs sorted, digits maintain order
        ),
         (
             ["let1 art can", "let2 art can", "let3 art zero"],
             ["let1 art can", "let2 art can", "let3 art zero"] # Sort by identifier when content is same
         ),
         (
             ["dig1 8", "dig2 4", "dig3 6"],
             ["dig1 8", "dig2 4", "dig3 6"] # Only digit logs, maintain order
         ),
         (
             ["letz foo", "lety foo", "leta foo"],
             ["leta foo", "lety foo", "letz foo"] # Only letter logs, sort by identifier
         ),
         (
             ["zld 93 0", "fp kindle book", "10a echo show", "17g 12 25 6", "ab1 kindle book", "125 echo show plus"],
             ["10a echo show", "125 echo show plus", "ab1 kindle book", "fp kindle book", "zld 93 0", "17g 12 25 6"]
         )

    ]

    correct_count = 0
    total_tests = len(test_cases)

    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    for i, (input_logs, expected_output) in enumerate(test_cases):
        # Create a copy to avoid modifying the original test case input
        input_copy = list(input_logs)
        result = reorderLogFiles(input_copy)
        passed = (result == expected_output)
        print(passed) # Print True or False for each test
        if passed:
            correct_count += 1

    # Restore stdout
    sys.stdout = old_stdout

    # Print the captured output (True/False for each test)
    print(captured_output.getvalue(), end="")

    # Print the final summary
    print(f"{correct_count}/{total_tests}")

# Execute the tests
if __name__ == "__main__":
    run_tests()