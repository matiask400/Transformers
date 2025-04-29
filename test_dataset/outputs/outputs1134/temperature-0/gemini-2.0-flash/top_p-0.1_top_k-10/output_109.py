def generatePossibleNextMoves(currentState):
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
    result = []
    for i in range(len(currentState) - 1):
        if currentState[i:i+2] == "++":
            result.append(currentState[:i] + "--" + currentState[i+2:])
    return result

def test_generatePossibleNextMoves():
    test_cases = [
        {"input": "++++", "expected": ["--++","+--+","++--"]},
        {"input": "+", "expected": []},
        {"input": "++", "expected": ["--"]},
        {"input": "+++", "expected": ["--+","+--"]},
        {"input": "-+++", "expected": ["--+-","+---"]},
        {"input": "+++++", "expected": ["--+++","+--++","++--+","+++--"]},
        {"input": "---", "expected": []},
        {"input": "", "expected": []},
        {"input": "++--++", "expected": ["-- --++","++----","++-- --"]},
        {"input": "+-+-+", "expected": []}
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, test_case in enumerate(test_cases):
        input_str = test_case["input"]
        expected_output = test_case["expected"]
        actual_output = generatePossibleNextMoves(input_str)

        if sorted(actual_output) == sorted(expected_output):
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: {input_str}")
            print(f"  Expected: {expected_output}")
            print(f"  Actual: {actual_output}")

    print(f"\nCorrect: {correct_count}/{total_count}")

if __name__ == "__main__":
    test_generatePossibleNextMoves()