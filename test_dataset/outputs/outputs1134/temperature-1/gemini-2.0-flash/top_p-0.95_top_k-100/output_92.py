def toHexspeak(num):
  """
  Converts a decimal number to its Hexspeak representation.

  Args:
    num: A string representing a decimal integer N.

  Returns:
    The Hexspeak representation of N if it is valid, otherwise "ERROR".
  """
  n = int(num)
  hex_val = hex(n)[2:].upper()
  hexspeak = ""
  for char in hex_val:
    if char == '0':
      hexspeak += 'O'
    elif char == '1':
      hexspeak += 'I'
    else:
      hexspeak += char
  
  valid_chars = {"A", "B", "C", "D", "E", "F", "I", "O"}
  for char in hexspeak:
    if char not in valid_chars:
      return "ERROR"
  
  return hexspeak

def test_toHexspeak():
  """
  Tests the toHexspeak function with various test cases.
  """
  test_cases = [
    ("257", "IOI", True),
    ("3", "ERROR", True),
    ("3000000000000", "A00000000000", True),
    ("1234567890", "499602D2", True),
    ("2147483647", "7FFFFFFF", True),
    ("16", "10", True),
    ("1", "1", True)
  ]
  
  correct_count = 0
  total_count = len(test_cases)
  
  for num, expected, should_pass in test_cases:
      actual = toHexspeak(num)
      if actual == expected:
          print("True")
          correct_count += 1
      else:
          print("False")
  
  print(f"{correct_count}/{total_count}")
  
test_toHexspeak()