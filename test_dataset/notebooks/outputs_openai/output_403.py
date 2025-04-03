def canCross(stones):
    if not stones or stones[0] != 0:
        return False
    stone_positions = set(stones)
    last_stone = stones[-1]
    memo = {}
    
    def dfs(position, last_jump):
        if (position, last_jump) in memo:
            return memo[(position, last_jump)]
        if position == last_stone:
            return True
        for jump in [last_jump -1, last_jump, last_jump +1]:
            if jump >0 and position + jump in stone_positions:
                if dfs(position + jump, jump):
                    memo[(position, last_jump)] = True
                    return True
        memo[(position, last_jump)] = False
        return False
    
    return dfs(0, 0)

def run_tests():
    tests = [
        {
            "input": [0,1,3,5,6,8,12,17],
            "expected": True
        },
        {
            "input": [0,1,2,3,4,8,9,11],
            "expected": False
        },
        {
            "input": [0,1],
            "expected": True
        },
        {
            "input": [0,1,3,4,5,7,9,10,12],
            "expected": True
        },
        {
            "input": [0,2],
            "expected": False
        }
    ]
    correct = 0
    total = len(tests)
    for test in tests:
        result = canCross(test["input"])
        expected = test["expected"]
        if result == expected:
            print(True)
            correct +=1
        else:
            print(False)
    print(f"{correct}/{total}")

run_tests()