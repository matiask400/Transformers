def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [''] * numRows
    index, step = 0, 1
    for c in s:
        rows[index] += c
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step
    return ''.join(rows)

# Test Cases
print(convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR')
print(convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI')
print(convert('A', 1) == 'A')