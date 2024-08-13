import re

def myAtoi(s: str) -> int:
    s = s.lstrip()  # remove leading whitespace
    if not s:
        return 0
    
    # check for sign
    if s[0] == '-' or s[0] == '+':
        sign = -1 if s[0] == '-' else 1
        s = s[1:]
    else:
        sign = 1

    # get digits
    digits = re.match('^[0-9]+', s)
    if digits is None:
        return 0
    
    num = int(digits.group(0)) * sign

    # clamp to 32-bit signed int range
    min_int = -2 ** 31
    max_int = 2 ** 31 - 1
    if num < min_int:
        return min_int
    if num > max_int:
        return max_int

    return num


# Test examples
examples = [ 
    {'input': '42', 'output': 42}, 
    {'input': '   -42', 'output': -42}, 
    {'input': '4193 with words', 'output': 4193}, 
    {'input': 'words and 987', 'output': 0}, 
    {'input': '-91283472332', 'output': -2147483648}, 
]

for example in examples:
    output = myAtoi(example['input'])
    print(output == example['output'])