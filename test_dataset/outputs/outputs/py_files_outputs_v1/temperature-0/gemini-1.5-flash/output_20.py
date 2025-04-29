def is_valid(s):
    stack = []
    parentheses = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in parentheses.values():
            stack.append(char)
        elif char in parentheses.keys():
            if stack and stack[-1] == parentheses[char]:
                stack.pop()
            else:
                return False
        else:
            return False
    return len(stack) == 0

# Example 1
input_1 = "()"
output_1 = is_valid(input_1)

# Example 2
input_2 = "()[]{}"
output_2 = is_valid(input_2)

# Example 3
input_3 = "(]"
output_3 = is_valid(input_3)

# Check if the outputs are correct
print(f"Example 1: Output is {output_1}, Expected output is True: {output_1 == True}")
print(f"Example 2: Output is {output_2}, Expected output is True: {output_2 == True}")
print(f"Example 3: Output is {output_3}, Expected output is False: {output_3 == False}")