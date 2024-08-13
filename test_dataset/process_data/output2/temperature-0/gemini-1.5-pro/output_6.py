def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [''] * numRows
    row_index = 0
    direction = 1
    for char in s:
        rows[row_index] += char
        row_index += direction
        if row_index == numRows - 1 or row_index == 0:
            direction *= -1
    return ''.join(rows)


input_1 = "PAYPALISHIRING"
output_1 = "PAHNAPLSIIGYIR"
input_2 = "PAYPALISHIRING"
output_2 = "PINALSIGYAHRPI"
input_3 = "A"
output_3 = "A"

print(convert(input_1, 3) == output_1)
print(convert(input_2, 4) == output_2)
print(convert(input_3, 1) == output_3)