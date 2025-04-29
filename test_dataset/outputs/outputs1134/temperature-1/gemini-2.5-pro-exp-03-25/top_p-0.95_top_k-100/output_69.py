import subprocess
import os
import sys

# The one-liner bash script to be tested
# 1. grep -oE '[a-z]+' words.txt: Extracts all sequences of lowercase letters, each on a new line.
# 2. sort: Sorts the words alphabetically, grouping identical words together.
# 3. uniq -c: Counts consecutive identical lines (words) and prepends the count. Output: " count word"
# 4. sort -nr: Sorts the lines numerically (-n) in reverse (-r) order based on the first field (the count).
# 5. awk '{print $2 " " $1}': Rearranges the output to "word count".
bash_command = "grep -oE '[a-z]+' words.txt | sort | uniq -c | sort -nr | awk '{print $2 \" \" $1}'"
# Alternative using tr (less robust if non-space whitespace exists, but works per constraints):
# bash_command = "cat words.txt | tr -s ' ' '\\n' | grep -v '^$' | sort | uniq -c | sort -nr | awk '{print $2 \" \" $1}'"

def run_test(input_content, expected_output, test_index):
    """
    Runs a single test case.
    Creates words.txt, executes the bash command, compares output, prints result, and cleans up.
    """
    test_file = "words.txt"
    passed = False

    # Ensure clean state before test
    if os.path.exists(test_file):
        try:
            os.remove(test_file)
        except OSError as e:
            print(f"Error removing pre-existing {test_file} before test {test_index + 1}: {e}", file=sys.stderr)
            # Decide if this should fail the test or just warn
            # For now, let's proceed cautiously, it might be a permissions issue

    try:
        # 1. Create words.txt with input content
        with open(test_file, "w", encoding="utf-8") as f:
            f.write(input_content)

        # 2. Execute the bash command
        # Use shell=True because we are executing a shell pipeline
        # Use capture_output=True to get stdout/stderr
        # Use text=True for string output
        # We don't use check=True because grep returns 1 if no matches are found (e.g., empty file),
        # which is expected behavior for some tests. We check return code manually if needed.
        result = subprocess.run(
            bash_command,
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        # Check if grep failed unexpectedly (return code 1 is OK if input/output empty)
        if result.returncode != 0 and not (result.returncode == 1 and result.stdout.strip() == "" and expected_output == ""):
             print(f"Test {test_index + 1} Bash Error: Exit code {result.returncode}", file=sys.stderr)
             print(f"Stderr: {result.stderr.strip()}", file=sys.stderr)
             # Continue to comparison, maybe output is still correct?

        # 3. Compare actual output (stripping trailing newline) with expected output
        actual_output = result.stdout.strip()
        if actual_output == expected_output:
            passed = True

        print(passed) # Print True or False for this test

    except Exception as e:
        # Catch any exception during file writing or subprocess execution
        print(f"\nTest {test_index + 1} Python Exception: {e}", file=sys.stderr)
        print(False) # Test fails if an exception occurs

    finally:
        # 4. Clean up words.txt
        if os.path.exists(test_file):
            try:
                os.remove(test_file)
            except OSError as e:
                # Warn if cleanup fails, but don't alter test result based on cleanup failure
                print(f"Warning: Error removing {test_file} after test {test_index + 1}: {e}", file=sys.stderr)

    return passed

def test_word_frequency(test_cases):
    """
    Runs all test cases and prints the final score.
    """
    passed_count = 0
    total_tests = len(test_cases)

    for i, (input_content, expected_output) in enumerate(test_cases):
        if run_test(input_content, expected_output, i):
            passed_count += 1

    print(f"{passed_count} / {total_tests}")

# Define test cases: tuples of (input_content, expected_output)
test_cases = [
    # Case 1: Example from description
    (
        "the day is sunny the the\nthe sunny is is",
        "the 4\nis 3\nsunny 2\nday 1"
    ),
    # Case 2: Empty file
    (
        "",
        ""
    ),
    # Case 3: File with only spaces/newlines
    # grep -oE '[a-z]+' will find no matches, producing empty output.
    (
        "   \n  \n \t ", # Added tab for variety, although constraints say only space
        ""
    ),
    # Case 4: One word
    (
        "hello",
        "hello 1"
    ),
    # Case 5: One word repeated
    (
        "word word word",
        "word 3"
    ),
    # Case 6: Multiple lines, different frequencies (unique counts)
    (
        "apple banana apple\ncherry banana apple\napple grape",
        "apple 4\nbanana 2\ncherry 1\ngrape 1" # Note: Tie for count 1 handled by sort (alpha)
        # Expected output after awk reorder and sort -nr should be:
        # apple 4
        # banana 2
        # cherry 1  <-- alphabetically first for count 1
        # grape 1   <-- alphabetically second for count 1
        # Re-checking constraint: "Don't worry about handling ties, it is guaranteed that each word's frequency count is unique."
        # OK, the example above violates this guarantee. Let's create one that satisfies it.
        "apple banana apple\ncherry banana apple\napple grape apple",
        # Counts: apple 5, banana 2, cherry 1, grape 1 (violates again!)
        # Try again:
        "one two three one two one\nfour five four\nsix seven\none four six one eight",
        # Counts: one 5, four 3, two 2, six 2 (violates!)
        # OK, let's use a simpler case guaranteed to have unique counts
        "go go go\nstop stop\nwait",
        "go 3\nstop 2\nwait 1" # This satisfies the unique count constraint.
    ),
    # Case 7: Leading/trailing spaces and multiple spaces between words
    (
        "  leading spaces   worda  wordb   trailing spaces  \n another  line worda ",
        # grep -oE extracts: leading, spaces, worda, wordb, trailing, spaces, another, line, worda
        # Counts: worda 2, spaces 2 (violates unique count constraint!)
        # Let's modify to ensure unique counts:
        "  big cats   run fast   big dogs chase big cats \n fast cats climb ",
        # words: big, cats, run, fast, big, dogs, chase, big, cats, fast, cats, climb
        # counts: big 3, cats 3 (violates!)
        # It seems hard to manually create complex cases with guaranteed unique counts.
        # Let's trust the simpler examples and the problem statement's guarantee for unseen inputs.
        # Using the original example from thought process that *did* have unique counts:
        "a b c a b a\nd e f d e\ng h i g\na d g x",
        # Counts: a 4, d 3, g 3 (violates!)
        # One more try:
        "zulu yankee xenia zulu yankee zulu\nwhiskey victor whiskey\nuniform tango\nzulu whiskey uniform zulu",
        # zulu: 5
        # whiskey: 3
        # yankee: 2
        # uniform: 2 (violates!)
        # Let's use a very simple one that works:
         " most frequent word appears most\n second frequent appears second\n word appears once",
         # most: 2, frequent: 2 (violates!)
         # Final attempt with a known unique count example:
         "echo echo echo echo\nfoxtrot foxtrot foxtrot\ngolf golf\nhotel",
         "echo 4\nfoxtrot 3\ngolf 2\nhotel 1" # This works and satisfies constraints.
    ),
    # Case 8: Single line, multiple spaces
    (
        "alpha  beta   alpha    gamma",
        "alpha 2\nbeta 1\ngamma 1" # Violates constraint! Reverting to a simpler guaranteed case.
        "one   two    one    three",
        "one 2\nthree 1\ntwo 1" # Violates constraint!
        # Let's just use the case from the problem description again, slightly modified
        "the day is sunny the the\nthe sunny is is now",
        "the 4\nis 3\nsunny 2\nday 1\nnow 1" # Violates constraint!
        # OK, let's focus on testing the pipeline logic rather than complex unique counts.
        # Use Case 7 example but adjust expectation based on actual counts (ignoring uniqueness constraint for test design)
         "  leading spaces   worda  wordb   trailing spaces  \n another  line worda ",
         # Actual counts: worda 2, spaces 2, leading 1, wordb 1, trailing 1, another 1, line 1
         # Expected Output (sorted by freq desc, then alpha asc for ties):
         "spaces 2\nworda 2\nanother 1\nleading 1\nline 1\ntrailing 1\nwordb 1"
    ),


]

if __name__ == "__main__":
    # Run the tests
    test_word_frequency(test_cases)