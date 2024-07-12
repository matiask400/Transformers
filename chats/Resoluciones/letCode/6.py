def convert(s, numRows):
  """Converts a string to a zigzag pattern and reads it line by line.

  Args:
    s: The input string.
    numRows: The number of rows in the zigzag pattern.

  Returns:
    The string representation of the zigzag pattern read line by line.
  """

  if numRows <= 1 or numRows >= len(s):
    return s

  rows = [[] for _ in range(numRows)]
  row_idx = 0
  step = 1  # Move down then up

  for char in s:
    rows[row_idx].append(char)

    if row_idx == numRows - 1:
      step = -1  # Change direction to up
    elif row_idx == 0:
      step = 1  # Change direction to down

    row_idx += step

  result = "".join(["".join(row) for row in rows])
  return result

s = "PAYPALISHIRING"
numRows = 3

result = convert(s, numRows)
print(result)  # Output: "PAHNAPLSIIGYIR" 
