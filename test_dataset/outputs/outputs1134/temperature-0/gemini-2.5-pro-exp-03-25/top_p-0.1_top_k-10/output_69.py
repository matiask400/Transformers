import subprocess
import os
import sys

# The bash one-liner script
bash_script_command = r"""cat words.txt | tr -s ' ' '\n' | grep . | sort | uniq -c | sort -nr | awk '{print $2 " " $1}'"""

# Define test cases
test_cases = [
    {
        "name": "Example Case",
        "input": "the day is sunny the the\nthe sunny is is",
        "expected_output": "the 4\nis 3\nsunny 2\nday 1"
    },
    {
        "name": "Single Word Repeated",
        "input": "hello hello hello",
        "expected_output": "hello 3"
    },
    {
        "name": "Multiple Spaces",
        "input": "word1  word2   word1\nword3  word1 word2",
        "expected_output": "word1 3\nword2 2\nword3 1"
    },
    {
        "name": "All Unique Words",
        "input": "alpha beta gamma delta",
        "expected_output": "gamma 1\ndelta 1\nbeta 1\nalpha 1" # Note: Order for ties doesn't matter per problem spec, but sort -nr is stable usually
                                                               # Let's adjust expected based on typical sort behavior (alphabetical for ties)
                                                               # Actually, the problem guarantees unique counts, so ties are not an issue.
                                                               # Let's re-evaluate the expected output based on sort -nr | awk
                                                               # uniq -c output: 1 alpha, 1 beta, 1 delta, 1 gamma
                                                               # sort -nr output: 1 gamma, 1 delta, 1 beta, 1 alpha (reverse alphabetical for ties usually)
                                                               # awk output: gamma 1, delta 1, beta 1, alpha 1
                                                               # Let's stick to the problem statement: unique counts guaranteed.
                                                               # Re-creating a test with unique counts:
        "input": "a a a a b b b c c d",
        "expected_output": "a 4\nb 3\nc 2\nd 1"

    },
    {
        "name": "Empty File",
        "input": "",
        "expected_output": ""
    },
    {
        "name": "File with only spaces and newlines",
        "input": "   \n  \n   ",
        "expected_output": ""
    },
    {
        "name": "Longer Text",
        "input": "this is a test sentence for word frequency calculation this test is simple but effective simple test",
        "expected_output": "test 3\nis 2\nsimple 2\nthis 2\nword 1\nsentence 1\nfrequency 1\nfor 1\neffective 1\ncalculation 1\nbut 1\na 1"
    }
]

def run_tests():
    """
    Runs the bash script against test cases and checks the output.
    """
    correct_tests = 0
    total_tests = len(test_cases)
    script_file = 'words.txt'

    print(f"Running tests using command: {bash_script_command}\n")

    for i, test_case in enumerate(test_cases):
        print(f"--- Test Case {i+1}: {test_case['name']} ---")
        # Create the input file
        with open(script_file, 'w') as f:
            f.write(test_case['input'])

        passed = False
        try:
            # Execute the bash script
            result = subprocess.run(
                bash_script_command,
                shell=True,        # Allows using pipes and shell features
                capture_output=True, # Capture stdout and stderr
                text=True,         # Decode output as text (UTF-8 by default)
                check=False        # Don't raise exception on non-zero exit code
            )

            # Get the actual output, remove trailing newline/whitespace
            actual_output = result.stdout.strip()
            expected_output = test_case['expected_output'].strip()

            # Print captured output for debugging if needed
            # print(f"Input:\n'''\n{test_case['input']}\n'''")
            # print(f"Expected:\n'''\n{expected_output}\n'''")
            # print(f"Actual:\n'''\n{actual_output}\n'''")
            # print(f"Stderr:\n'''\n{result.stderr}\n'''")
            # print(f"Return Code: {result.returncode}")


            # Compare actual output with expected output
            if actual_output == expected_output:
                passed = True
                correct_tests += 1

        except Exception as e:
            print(f"Error during test execution: {e}")
            passed = False
        finally:
            # Clean up the created file
            if os.path.exists(script_file):
                os.remove(script_file)

        print(f"Result: {passed}")
        print("-" * (len(f"--- Test Case {i+1}: {test_case['name']} ---")))


    print(f"\n--- Summary ---")
    print(f"{correct_tests} / {total_tests} tests passed.")

if __name__ == "__main__":
    # This block ensures the code runs when the script is executed directly
    run_tests()