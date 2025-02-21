import sys

def myAtoi(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    result = 0
    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            break
    result *= sign
    if result > (2**31 - 1):
        return (2**31 - 1)
    elif result < (-2**31):
        return (-2**31)
    return result

# Test cases
input_1 = "42"
output_1 = myAtoi(input_1)
print(f"Input 1: {input_1}, Output 1: {output_1}")

input_2 = "   -42"
output_2 = myAtoi(input_2)
print(f"Input 2: {input_2}, Output 2: {output_2}")

input_3 = "4193 with words"
output_3 = myAtoi(input_3)
print(f"Input 3: {input_3}, Output 3: {output_3}")

# Check if the results match the expected outputs
print(f"Output 1 matches expected output: {output_1 == 42}")
print(f"Output 2 matches expected output: {output_2 == -42}")
print(f"Output 3 matches expected output: {output_3 == 4193}")