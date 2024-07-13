def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    
    result = [''] * numRows
    row = 0
    direction = 1
    
    for i in range(len(s)):
        result[row] += s[i]
        
        if row == numRows - 1:
            direction = -1
        elif row == 0:
            direction = 1
        
        row += direction
    
    return ''.join(result)

# Test cases
input_1 = "PAYPALISHIRING"
output_1 = "PAHNAPLSIIGYIR"
input_2 = "PAYPALISHIRING"
output_2 = "PINALSIGYAHRPI"
input_3 = "A"
output_3 = "A"

print(f"Input 1: {input_1}")
print(f"Output 1: {output_1}")
print(f"Expected Output 1: {convert(input_1, 3)}")
print(f"Test 1: {convert(input_1, 3) == output_1}")

print(f"Input 2: {input_2}")
print(f"Output 2: {output_2}")
print(f"Expected Output 2: {convert(input_2, 4)}")
print(f"Test 2: {convert(input_2, 4) == output_2}")

print(f"Input 3: {input_3}")
print(f"Output 3: {output_3}")
print(f"Expected Output 3: {convert(input_3, 1)}")
print(f"Test 3: {convert(input_3, 1) == output_3}")