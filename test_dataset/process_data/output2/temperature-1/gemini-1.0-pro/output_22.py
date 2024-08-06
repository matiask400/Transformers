from typing import List

def generate_parenthesis(n: int) -> List[str]:
    if n <= 0:
        return []
    stack = []
    result = []

    def backtrack(open_count, close_count):
        if open_count == close_count == n:
            result.append(''.join(stack))
            return
        if open_count < n:
            stack.append('(') 
            backtrack(open_count + 1, close_count) 
            stack.pop()
        if close_count < open_count:
            stack.append(')')
            backtrack(open_count, close_count + 1)
            stack.pop()

    backtrack(0, 0)
    return result


print('Input 1:
{}
Output 1:
{}'.format(3, generate_parenthesis(3))) 
print('Input 2:
{}
Output 2:
{}'.format(1, generate_parenthesis(1))) 

assert generate_parenthesis(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']
assert generate_parenthesis(1) == ['()']