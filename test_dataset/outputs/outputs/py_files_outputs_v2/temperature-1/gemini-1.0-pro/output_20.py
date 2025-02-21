def is_valid(s):
	
    # Create a dictionary of opening and closing brackets.
    brackets = {')': '(', '}': '{', ']': '['}

    # Create a stack to store the opening brackets.
    stack = []

    # Iterate over the string.
    for char in s:

        # If the character is an opening bracket, push it onto the stack.
        if char in brackets.values():
            stack.append(char)

        # If the character is a closing bracket, check if the top of the stack is the matching opening bracket.
        elif char in brackets.keys():
            if not stack or stack.pop() != brackets[char]:
                return False

        # If the character is not a bracket, ignore it.
        else:
            continue

    # If the stack is empty, all brackets have been closed correctly.
    return not stack


# Test the function.
input1 = '()'
output1 = is_valid(input1)
print(output1 == True)

input2 = '()[]{}'
output2 = is_valid(input2)
print(output2 == True)

input3 = '(]' 
output3 = is_valid(input3)
print(output3 == False)

input4 = '([)]'
output4 = is_valid(input4)
print(output4 == False)

input5 = '{[]}'
output5 = is_valid(input5)
print(output5 == True)