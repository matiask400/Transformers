def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [''] * numRows
    row_index = 0
    direction = 1
    for char in s:
        rows[row_index] += char
        if row_index == numRows - 1:
            direction = -1
        elif row_index == 0:
            direction = 1
        row_index += direction
    return ''.join(rows)


input_1 = ("PAYPALISHIRING", 3)
output_1 = "PAHNAPLSIIGYIR"
input_2 = ("PAYPALISHIRING", 4)
output_2 = "PINALSIGYAHRPI"
input_3 = ("A", 1)
output_3 = "A"

print(convert(*input_1) == output_1)
print(convert(*input_2) == output_2)
print(convert(*input_3) == output_3)