def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [''] * numRows
    row, step = 0, 1
    for char in s:
        rows[row] += char
        if row == numRows - 1:
            step = -1
        elif row == 0:
            step = 1
        row += step
    return ''.join(rows)


# Test cases
input1 = "PAYPALISHIRING"
output1 = "PAHNAPLSIIGYIR"
input2 = "PAYPALISHIRING"
output2 = "PINALSIGYAHRPI"
input3 = "A"
output3 = "A"

print(convert(input1, 3) == output1)
print(convert(input2, 4) == output2)
print(convert(input3, 1) == output3)