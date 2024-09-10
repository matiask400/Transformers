def reverseInteger(x):
    if x == 0:
        return 0
    
    sign = 1 if x > 0 else -1
    x = abs(x)
    reversed_num = 0
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    
    if reversed_num > 2**31 - 1 or reversed_num < -2**31:
        return 0
    else:
        return sign * reversed_num

# Example 1
input_1 = 123
output_1 = 321
print(f"Input: {input_1}, Output: {reverseInteger(input_1)}, Expected: {output_1}, Correct: {reverseInteger(input_1) == output_1}")

# Example 2
input_2 = -123
output_2 = -321
print(f"Input: {input_2}, Output: {reverseInteger(input_2)}, Expected: {output_2}, Correct: {reverseInteger(input_2) == output_2}")

# Example 3
input_3 = 120
output_3 = 21
print(f"Input: {input_3}, Output: {reverseInteger(input_3)}, Expected: {output_3}, Correct: {reverseInteger(input_3) == output_3}")

# Example 4
input_4 = 0
output_4 = 0
print(f"Input: {input_4}, Output: {reverseInteger(input_4)}, Expected: {output_4}, Correct: {reverseInteger(input_4) == output_4}")