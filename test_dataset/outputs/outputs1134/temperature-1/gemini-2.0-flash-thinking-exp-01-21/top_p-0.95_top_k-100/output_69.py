import subprocess
import tempfile
import os

def test_word_frequency_script(words_txt_content, expected_output):
    """
    Tests the bash script for word frequency calculation.

    Args:
        words_txt_content (str): The content of words.txt for the test case.
        expected_output (str): The expected output of the bash script.

    Returns:
        bool: True if the test passed, False otherwise.
    """
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmpfile:
        tmpfile.write(words_txt_content)
        words_file_path = tmpfile.name

    command = f"cat {words_file_path} | tr -s ' ' '\\n' | sort | uniq -c | sort -nr | awk '{{print $2, $1}}'"

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()

    os.unlink(words_file_path)

    actual_output = stdout.strip()
    expected_output = expected_output.strip()

    if actual_output == expected_output:
        return True
    else:
        print(f"Expected:\n{expected_output}\nActual:\n{actual_output}")
        return False

def run_tests():
    """
    Runs all test cases and prints the results.
    """
    test_cases = [
        {
            "words_txt_content": "the day is sunny the the\nthe sunny is is",
            "expected_output": "the 4\nis 3\nsunny 2\nday 1"
        },
        {
            "words_txt_content": "a a a b b c",
            "expected_output": "a 3\nb 2\nc 1"
        },
        {
            "words_txt_content": "hello world hello",
            "expected_output": "hello 2\nworld 1"
        },
        {
            "words_txt_content": "  word1   word2 word1  ",
            "expected_output": "word1 2\nword2 1"
        },
        {
            "words_txt_content": "line1\nline2 line2\nline3 line3 line3",
            "expected_output": "line3 3\nline2 2\nline1 1"
        },
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        print(f"Test Case {i+1}: ", end="")
        if test_word_frequency_script(test_case["words_txt_content"], test_case["expected_output"]):
            print("True")
            correct_tests += 1
        else:
            print("False")

    print(f"\n{correct_tests}/{total_tests}")

if __name__ == "__main__":
    run_tests()