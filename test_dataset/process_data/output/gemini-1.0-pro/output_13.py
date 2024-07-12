def roman_to_int(s: str) -> int:
  """Converts a Roman numeral to an integer.

  Args:
    s (str): The Roman numeral to convert.

  Returns:
    int: The integer value of the Roman numeral.
  """
  roman_numerals = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000,
  }

  result = 0
  for i in range(len(s)):
    if i > 0 and roman_numerals[s[i]] > roman_numerals[s[i - 1]]:
      result += roman_numerals[s[i]] - 2 * roman_numerals[s[i - 1]]
    else:
      result += roman_numerals[s[i]]
  return result


# Example 1
s = "III"
print(roman_to_int(s))

# Example 2
s = "IV"
print(roman_to_int(s))

# Example 3
s = "IX"
print(roman_to_int(s))

# Example 4
s = "LVIII"
print(roman_to_int(s))

# Example 5
s = "MCMXCIV"
print(roman_to_int(s))