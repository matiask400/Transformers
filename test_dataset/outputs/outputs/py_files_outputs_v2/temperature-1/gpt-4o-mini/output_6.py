def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    result = []
    cycle_len = 2 * numRows - 2
    for i in range(numRows):
        for j in range(i, len(s), cycle_len):
            result.append(s[j])
            if 0 < i < numRows - 1 and j + cycle_len - 2 * i < len(s):
                result.append(s[j + cycle_len - 2 * i])
    return ''.join(result)

input_1 = ('PAYPALISHIRING', 3)
output_1 = 'PAHNAPLSIIGYIR'
result_1 = convert(*input_1) == output_1

input_2 = ('PAYPALISHIRING', 4)
output_2 = 'PINALSIGYAHRPI'
result_2 = convert(*input_2) == output_2

input_3 = ('A', 1)
output_3 = 'A'
result_3 = convert(*input_3) == output_3

print(result_1, result_2, result_3)