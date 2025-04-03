def flipGame(currentState):
    """
    You are playing a Flip Game with your friend.

    You are given a string `currentState` that contains only `'+'` and `'-'`. You and your friend take turns to flip two consecutive `"++"` into `"--"`. The game ends when a person can no longer make a move, and therefore the other person will be the winner.

    Return all possible states of the string `currentState` after one valid move. You may return the answer in any order. If there is no valid move, return an empty list `[]`.

    Example 1:
    Input: currentState = "++++"
    Output: ["--++","+--+","++--"]

    Example 2:
    Input: currentState = "+"
    Output: []

    Constraints:
    `1 <= currentState.length <= 500`
    `currentState[i]` is either `'+'` or `'-'`.
    """
    possible_states = []
    for i in range(len(currentState) - 1):
        if currentState[i:i+2] == "++":
            new_state_list = list(currentState)
            new_state_list[i:i+2] = ["-", "-"]
            possible_states.append("".join(new_state_list))
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
            "input": "--++--",
            "expected_output": ["----+-"] # Corrected expected output according to the problem description which says to flip "++" to "--".
        },
        {
            "input": "+++",
            "expected_output": ["--+", "+--"]
        },
        {
            "input": "",
            "expected_output": []
        },
        {
            "input": "-",
            "expected_output": []
        },
        {
            "input": "---",
            "expected_output": []
        },
        {
            "input": "++--++",
            "expected_output": ["-- --++", "++----"]
        }
    ]

    correct_count = 0
    for i, test_case in enumerate(test_cases):
        input_str = test_case["input"]
        expected_output = sorted(test_case["expected_output"])
        actual_output = sorted(flipGame(input_str))
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: {input_str}")
            print(f"  Expected: {expected_output}")
            print(f"  Actual: {actual_output}")

    print(f"\n{correct_count} correct tests over {len(test_cases)}")

if __name__ == '__main__':
    run_tests()