def generate_possible_next_moves(current_state):
    """
    Generates all possible states of the string after one valid move in the Flip Game.

    Args:
        current_state (str): The current state of the game, containing only '+' and '-'.

    Returns:
        list[str]: A list of all possible states after one valid move.
                   Returns an empty list if there are no valid moves.
    """
    possible_states = []
    for i in range(len(current_state) - 1):
        if current_state[i:i + 2] == "++":
            new_state = current_state[:i] + "--" + current_state[i + 2:]
            possible_states.append(new_state)
    return possible_states

def test_generate_possible_next_moves():
    """
    Tests the generate_possible_next_moves function with different test cases.
    """
    test_cases = [
        ("++++", ["--++", "+--+", "++--"]),
        ("+", []),
        ("++--++", ["--++++", "++----", "++--++"]),
        ("---", []),
        ("+++++", ["--+++", "+--++", "++--+"]),
        ("+-+", []),
        ("++", ["--"]),
        ("", [])
    ]
    
    num_correct = 0
    total_tests = len(test_cases)
    
    for current_state, expected_output in test_cases:
        actual_output = generate_possible_next_moves(current_state)
        actual_output.sort()
        expected_output.sort()
        
        if actual_output == expected_output:
            print("True")
            num_correct += 1
        else:
            print("False")
            print(f"Input: {current_state}")
            print(f"Expected: {expected_output}")
            print(f"Actual: {actual_output}")

    print(f"{num_correct}/{total_tests}")

if __name__ == "__main__":
    test_generate_possible_next_moves()