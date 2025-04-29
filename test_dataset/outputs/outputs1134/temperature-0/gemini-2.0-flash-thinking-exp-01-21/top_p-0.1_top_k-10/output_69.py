import subprocess

def test_word_frequency_script(input_text, expected_output):
    """
    Tests the bash script for word frequency calculation.

    Args:
        input_text (str): The content to be written to words.txt.
        expected_output (str): The expected output of the bash script.

    Returns:
        bool: True if the test passed, False otherwise.
    """
    with open("words.txt", "w") as f:
        f.write(input_text)

    command = "cat words.txt | tr -s ' ' '\\n' | sort | uniq -c | sort -nr | awk '{print $2, $1}'"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()

    actual_output = stdout.strip()
    return actual_output == expected_output.strip()

def run_tests():
    """
    Runs multiple test cases for the word frequency script.
    """
    test_cases = [
        {
            "input": "the day is sunny the the\nthe sunny is is",
            "expected": "the 4\nis 3\nsunny 2\nday 1"
        },
        {
            "input": "",
            "expected": ""
        },
        {
            "input": "hello hello hello",
            "expected": "hello 3"
        },
        {
            "input": "word1  word2   word1\nword3 word2",
            "expected": "word2 2\nword1 2\nword3 1"
        },
        {
            "input": " a  b c   a b  ",
            "expected": "b 2\na 2\nc 1"
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, case in enumerate(test_cases):
        test_passed = test_word_frequency_script(case["input"], case["expected"])
        print(f"Test {i+1}: {'True' if test_passed else 'False'}")
        if test_passed:
            correct_tests += 1

    print(f"\n{correct_tests}/{total_tests}")

if __name__ == "__main__":
    run_tests()