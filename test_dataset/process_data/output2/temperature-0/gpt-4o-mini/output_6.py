def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [''] * numRows
    cur_row = 0
    going_down = False

    for char in s:
        rows[cur_row] += char
        if cur_row == 0:
            going_down = True
        elif cur_row == numRows - 1:
            going_down = False
        cur_row += 1 if going_down else -1

    return ''.join(rows)

# Example inputs
input_1 = ("PAYPALISHIRING", 3)
output_1 = convert(*input_1)
print(output_1 == "PAHNAPLSIIGYIR")

input_2 = ("PAYPALISHIRING", 4)
output_2 = convert(*input_2)
print(output_2 == "PINALSIGYAHRPI")

input_3 = ("A", 1)
output_3 = convert(*input_3)
print(output_3 == "A")