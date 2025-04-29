def flip_game(currentState):
    possible_states = []
    for i in range(len(currentState) - 1):
        if currentState[i:i+2] == "++":
            new_state = list(currentState)
            new_state[i:i+2] = "--"
            possible_states.append("".join(new_state))
    return possible_states

def run_tests():
    test_cases = [
        {
            "input": "++++",
            "expected_output": ["--++", "+--+", "++--"]
        },
        {
            "input": "+",
            "expected_output": []
        },
        {
            "input": "--",
            "expected_output": []
        },
        {
            "input": "+-+",
            "expected_output": []
        },
        {
            "input": "++--",
            "expected_output": ["-- --"]
        },
        {
            "input": "--++",
            "expected_output": ["----"]
        },
        {
            "input": "+ ++",
            "expected_output": [] # No consecutive ++
        },
        {
            "input": "+++",
            "expected_output": ["--+", "+--"]
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        input_state = test_case["input"]
        expected_output = sorted(test_case["expected_output"])
        actual_output = sorted(flip_game(input_state))

        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")

    print(f"\n{correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()