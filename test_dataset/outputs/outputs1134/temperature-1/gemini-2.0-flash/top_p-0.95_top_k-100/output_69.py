import subprocess

def test_word_frequency(words_txt_content, expected_output):
  """Tests the word frequency bash script with the given input and expected output.

  Args:
    words_txt_content: The content of the words.txt file.
    expected_output: The expected output of the bash script.

  Returns:
    A tuple containing:
      - A list of boolean values indicating whether each test case passed or failed.
      - The number of correct tests.
      - The total number of tests.
  """

  # Create the words.txt file
  with open("words.txt", "w") as f:
    f.write(words_txt_content)

  # Run the bash script
  try:
    process = subprocess.Popen(
        """tr -s ' ' '\\n' < words.txt | sort | uniq -c | sort -nr""",
        shell=True,
        executable="/bin/bash",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate()
    actual_output = stdout.strip()

    # Compare the actual output with the expected output
    test_passed = actual_output == expected_output
  except Exception as e:
    test_passed = False
    print(f"Error running test: {e}")

  return test_passed


def run_tests():
  """Runs all test cases."""

  test_cases = [
      {
          "words_txt_content": "the day is sunny the the\nthe sunny is is",
          "expected_output": "4 the\n3 is\n2 sunny\n1 day",
      },
      {
          "words_txt_content": "a b c\na b\na",
          "expected_output": "3 a\n2 b\n1 c",
      },
      {
          "words_txt_content": "hello world hello",
          "expected_output": "2 hello\n1 world",
      },
      {
          "words_txt_content": "   a   b  c  \n d  e  \n f",
          "expected_output": "1 f\n1 e\n1 d\n1 c\n1 b\n1 a",
      },
      {
          "words_txt_content": "apple apple banana banana banana",
          "expected_output": "3 banana\n2 apple",
      }
  ]

  results = []
  for test_case in test_cases:
    result = test_word_frequency(
        test_case["words_txt_content"], test_case["expected_output"]
    )
    results.append(result)
    print(result)

  correct_count = sum(results)
  total_count = len(results)

  print(f"{correct_count}/{total_count}")


if __name__ == "__main__":
  run_tests()