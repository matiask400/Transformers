def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    
    result = [''] * numRows
    row = 0
    goingDown = False
    
    for i in range(len(s)):
        result[row] += s[i]
        if row == numRows - 1:
            goingDown = True
        elif row == 0:
            goingDown = False
        row += 1 if goingDown else -1
    
    return ''.join(result)

# Example 1
input_1 = "PAYPALISHIRING"
numRows_1 = 3
output_1 = "PAHNAPLSIIGYIR"
print(convert(input_1, numRows_1) == output_1)

# Example 2
input_2 = "PAYPALISHIRING"
numRows_2 = 4
output_2 = "PINALSIGYAHRPI"
print(convert(input_2, numRows_2) == output_2)

# Example 3
input_3 = "A"
numRows_3 = 1
output_3 = "A"
print(convert(input_3, numRows_3) == output_3)