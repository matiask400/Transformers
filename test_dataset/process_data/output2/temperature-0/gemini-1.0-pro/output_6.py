def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [[] for _ in range(numRows)]
    row, col = 0, 0
    direction = 1

    for char in s:
        rows[row].append(char)
        if row == 0:
            direction = 1
        elif row == numRows - 1:
            direction = -1
        row += direction

    return ''.join([''.join(row) for row in rows])

input1 = "PAYPALISHIRING"
numRows1 = 3
output1 = convert(input1, numRows1)
print(output1 == "PAHNAPLSIIGYIR")  # True

input2 = "PAYPALISHIRING"
numRows2 = 4
output2 = convert(input2, numRows2)
print(output2 == "PINALSIGYAHRPI")  # True

input3 = "A"
numRows3 = 1
output3 = convert(input3, numRows3)
print(output3 == "A")  # True