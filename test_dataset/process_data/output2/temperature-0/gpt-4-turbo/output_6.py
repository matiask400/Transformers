def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [''] * numRows
    current_row, step = 0, 1
    for char in s:
        rows[current_row] += char
        if current_row == 0:
            step = 1
        elif current_row == numRows - 1:
            step = -1
        current_row += step
    return ''.join(rows)

# Test cases
print(convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR')
print(convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI')
print(convert('A', 1) == 'A')