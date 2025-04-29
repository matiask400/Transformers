def addOperators(num: str, target: int):
    res = []
    n = len(num)
    
    def helper(index, path, evaluated, multed):
        if index == n:
            if evaluated == target:
                res.append(path)
            return
        for i in range(index, n):
            # Avoid numbers with leading zero
            if i != index and num[index] == '0':
                break
            curr_str = num[index:i+1]
            curr = int(curr_str)
            if index == 0:
                helper(i+1, curr_str, curr, curr)
            else:
                helper(i+1, path + '+' + curr_str, evaluated + curr, curr)
                helper(i+1, path + '-' + curr_str, evaluated - curr, -curr)
                helper(i+1, path + '*' + curr_str, evaluated - multed + multed * curr, multed * curr)
    
    helper(0, "", 0, 0)
    return res

test_cases = [
    ("123", 6, ["1*2*3","1+2+3"]),
    ("232", 8, ["2*3+2","2+3*2"]),
    ("105", 5, ["1*0+5","10-5"]),
    ("00", 0, ["0+0","0-0","0*0"]),
    ("3456237490", 9191, [])
]

correct = 0
total = len(test_cases)

for num, target, expected in test_cases:
    output = addOperators(num, target)
    if sorted(output) == sorted(expected):
        print('True')
        correct +=1
    else:
        print('False')

print(f"{correct}/{total}")