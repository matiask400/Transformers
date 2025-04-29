def flip_game_states(currentState):
    result = []
    state = list(currentState)
    for i in range(len(state) - 1):
        if state[i] == '+' and state[i+1] == '+':
            new_state = state.copy()
            new_state[i] = '-'
            new_state[i+1] = '-'
            result.append(''.join(new_state))
    return result

def run_tests():
    test_cases = [
        {
            "input": "++++",
            "expected": ["--++", "+--+", "++--"]
        },
        {
            "input": "+",
            "expected": []
        },
        {
            "input": "++--++",
            "expected": ["----++", "+-- -++", "++----"]
        },
        {
            "input": "+++-++",
            "expected": ["--- -++", "++- --"]
        },
        {
            "input": "-----",
            "expected": []
        },
        {
            "input": "++",
            "expected": ["--"]
        },
        {
            "input": "+++-",
            "expected": ["--- -"]
        }
    ]
    
    correct = 0
    total = len(test_cases)
    for test in test_cases:
        input_state = test["input"]
        expected = test["expected"]
        output = flip_game_states(input_state)
        # Compare as sets since order doesn't matter
        if set(output) == set(expected):
            print("True")
            correct += 1
        else:
            print("False")
    print(f"{correct}/{total}")

run_tests()