def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    
    result = [''] * numRows
    row = 0
    goingDown = False
    
    for char in s:
        result[row] += char
        
        if row == 0 or row == numRows - 1:
            goingDown = not goingDown
            
        if goingDown:
            row += 1
        else:
            row -= 1
    
    return ''.join(result)

# Example 1
s = "PAYPALISHIRING"
numRows = 3
output = convert(s, numRows)
print(output == "PAHNAPLSIIGYIR", output)

# Example 2
s = "PAYPALISHIRING"
numRows = 4
output = convert(s, numRows)
print(output == "PINALSIGYAHRPI", output)

# Example 3
s = "A"
numRows = 1
output = convert(s, numRows)
print(output == "A", output)