def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    current_row = 0
    going_down = False

    for char in s:
        rows[current_row] += char
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1

    return ''.join(rows)

# Example inputs and expected outputs
inputs = [
    ("PAYPALISHIRING", 3),
    ("PAYPALISHIRING", 4),
    ("A", 1)
]
expected_outputs = [
    "PAHNAPLSIIGYIR",
    "PINALSIGYAHRPI",
    "A"
]

# Verify the solution
for i, (s, numRows) in enumerate(inputs):
    result = convert(s, numRows)
    print(result == expected_outputs[i])