def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [''] * numRows
    cur_row = 0
    going_down = False
    for c in s:
        rows[cur_row] += c
        if cur_row == 0 or cur_row == numRows - 1:
            going_down = not going_down
        cur_row += 1 if going_down else -1
    return ''.join(rows)

# Test the solution with provided examples
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

for i, (s, numRows) in enumerate(inputs):
    output = convert(s, numRows)
    print(output == expected_outputs[i])