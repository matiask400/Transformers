def remove_vowels(s):
  """
  Removes vowels from a string.

  Args:
    s: The input string.

  Returns:
    The string with vowels removed.
  """
  vowels = "aeiou"
  result = ""
  for char in s:
    if char not in vowels:
      result += char
  return result

def test_remove_vowels():
  """
  Tests the remove_vowels function.
  """
  test_cases = [
      {"input": "leetcodeisacommunityforcoders", "expected": "ltcdscmmntyfrcdrs"},
      {"input": "aeiou", "expected": ""},
      {"input": "bcdfghjklmnpqrstvwxyz", "expected": "bcdfghjklmnpqrstvwxyz"},
      {"input": "a", "expected": ""},
      {"input": "e", "expected": ""},
      {"input": "i", "expected": ""},
      {"input": "o", "expected": ""},
      {"input": "u", "expected": ""},
      {"input": "", "expected": ""},
      {"input": "programming", "expected": "prgrmmng"}
  ]

  num_correct = 0
  total_tests = len(test_cases)

  for i, test_case in enumerate(test_cases):
    input_string = test_case["input"]
    expected_output = test_case["expected"]
    actual_output = remove_vowels(input_string)

    if actual_output == expected_output:
      print("True")
      num_correct += 1
    else:
      print("False")
      print(f"Test case {i+1} failed:")
      print(f"  Input: {input_string}")
      print(f"  Expected: {expected_output}")
      print(f"  Actual: {actual_output}")

  print(f"{num_correct}/{total_tests}")

if __name__ == "__main__":
  test_remove_vowels()