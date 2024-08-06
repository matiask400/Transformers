from typing import List

def generate_parenthesis(n: int) -> List[str]:
    if n == 0:
        return [""]
    result = []
    for i in range(n):
        for left in generate_parenthesis(i):
            for right in generate_parenthesis(n-1-i):
                result.append("({}){}".format(left, right))
    return result

input_1 = 3
output_1 = generate_parenthesis(input_1)
print(output_1 == ["((()))","(()())","(())()","()(())","()()()"], output_1)

input_2 = 1
output_2 = generate_parenthesis(input_2)
print(output_2 == ["()"], output_2)