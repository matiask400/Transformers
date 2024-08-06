def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [''] * numRows
    row_index = 0
    step = 1
    for char in s:
        rows[row_index] += char
        if row_index == numRows - 1:
            step = -1
        elif row_index == 0:
            step = 1
        row_index += step
    return ''.join(rows)


# Test the function with the provided examples
input_1 = "PAYPALISHIRING"
input_2 = "PAYPALISHIRING"
input_3 = "A"

output_1 = convert(input_1, 3)
output_2 = convert(input_2, 4)
output_3 = convert(input_3, 1)

print(output_1 == "PAHNAPLSIIGYIR")  # Expected output: True
print(output_2 == "PINALSIGYAHRPI")  # Expected output: True
print(output_3 == "A")  # Expected output: True