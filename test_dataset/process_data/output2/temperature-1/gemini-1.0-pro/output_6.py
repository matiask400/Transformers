s = 'PAYPALISHIRING'
input1 = convert(s, 3)
print(input1 == 'PAHNAPLSIIGYIR')
s = 'PAYPALISHIRING'
input2 = convert(s, 4)
print(input2 == 'PINALSIGYAHRPI')
s = 'A'
input3 = convert(s, 1)
print(input3 == 'A')

def convert(s, numRows):
    if numRows == 1:
        return s
    rows = [[] for _ in range(numRows)]
    i, row = 0, 0
    direction = 1
    while i < len(s):
        rows[row].append(s[i])
        if row == 0:
            direction = 1
        elif row == numRows - 1:
            direction = -1
        row += direction
        i += 1
    return ''.join([''.join(row) for row in rows])