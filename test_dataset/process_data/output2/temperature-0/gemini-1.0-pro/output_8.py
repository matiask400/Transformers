import re

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        sign = -1 if s[0] == '-' else 1
        if s[0] in ['-', '+']:
            s = s[1:]
        
        num_re = re.compile(r'^\d+')
        num = num_re.match(s)
        if not num:
            return 0
        
        num = int(num.group())
        num = sign * num
        
        max_int = 2**31 - 1
        min_int = -2**31
        if num > max_int:
            return max_int
        elif num < min_int:
            return min_int
        else:
            return num


# Example test cases
sol = Solution()

input1 = "42"
output1 = sol.myAtoi(input1)
print(output1 == 42)

input2 = "   -42"
output2 = sol.myAtoi(input2)
print(output2 == -42)

input3 = "4193 with words"
output3 = sol.myAtoi(input3)
print(output3 == 4193)

input4 = "words and 987"
output4 = sol.myAtoi(input4)
print(output4 == 0)

input5 = "-91283472332"
output5 = sol.myAtoi(input5)
print(output5 == -2147483648)