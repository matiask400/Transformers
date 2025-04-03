import subprocess

def test_word_frequency(words_txt_content, expected_output):
    """
    Tests the word frequency calculation using a bash script.

    Args:
        words_txt_content: The content of the words.txt file.
        expected_output: The expected output of the bash script.

    Returns:
        True if the test passes, False otherwise.
    """

    try:
        # Create a temporary file with the given content
        with open("words.txt", "w") as f:
            f.write(words_txt_content)

        # Run the bash script
        script = """
        tr -s ' ' '\\n' < words.txt | sort | uniq -c | sort -nr
        """
        process = subprocess.Popen(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()

        # Clean up the temporary file
        subprocess.run(["rm", "words.txt"])

        # Compare the output with the expected output
        if output.strip() == expected_output.strip():
            return True
        else:
            print("Expected:")
            print(expected_output.strip())
            print("Got:")
            print(output.strip())
            return False

    except Exception as e:
        print(f"Error during test: {e}")
        return False

def run_tests():
    """
    Runs a series of tests for the word frequency calculation.
    """

    tests = [
        {
            "input": "the day is sunny the the\nthe sunny is is",
            "expected": "4 the\n3 is\n2 sunny\n1 day"
        },
        {
            "input": "apple banana apple orange banana apple",
            "expected": "3 apple\n2 banana\n1 orange"
        },
        {
            "input": "one two three four five six seven eight nine ten",
            "expected": "1 one\n1 two\n1 three\n1 ten\n1 seven\n1 six\n1 nine\n1 five\n1 four\n1 eight"
        },
        {
            "input": "a a a a a",
            "expected": "5 a"
        },
        {
            "input": "  a   b  c   ",
            "expected": "1 c\n1 b\n1 a"
        }
    ]

    correct_count = 0
    total_count = len(tests)

    for i, test in enumerate(tests):
        result = test_word_frequency(test["input"], test["expected"])
        print(result)
        if result:
            correct_count += 1

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    run_tests()