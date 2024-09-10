def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    rows = ['' for _ in range(numRows)]
    current_row = 0
    going_down = False

    for char in s:
        rows[current_row] += char
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1

    return ''.join(rows)

# Test cases
print(convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR')
print(convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI')
print(convert('A', 1) == 'A')