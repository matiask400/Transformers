def solve_lock(deadends, target):
    deadend_set = set(deadends)
    if "0000" in deadend_set:
        return -1
    if "0000" == target:
        return 0

    queue = [("0000", 0)]
    visited_set = {"0000"}

    while queue:
        current_state, turns = queue.pop(0)

        if current_state == target:
            return turns

        for i in range(4):
            digit = int(current_state[i])

            # Turn forward
            next_digit_forward = str((digit + 1) % 10)
            next_state_forward = list(current_state)
            next_state_forward[i] = next_digit_forward
            next_state_forward = "".join(next_state_forward)

            if next_state_forward not in deadend_set and next_state_forward not in visited_set:
                visited_set.add(next_state_forward)
                queue.append((next_state_forward, turns + 1))

            # Turn backward
            next_digit_backward = str((digit - 1 + 10) % 10)
            next_state_backward = list(current_state)
            next_state_backward[i] = next_digit_backward
            next_state_backward = "".join(next_state_backward)

            if next_state_backward not in deadend_set and next_state_backward not in visited_set:
                visited_set.add(next_state_backward)
                queue.append((next_state_backward, turns + 1))

    return -1

def run_tests():
    tests = [
        {
            "deadends": ["0201","0101","0102","1212","2002"],
            "target": "0202",
            "expected": 6
        },
        {
            "deadends": ["8888"],
            "target": "0009",
            "expected": 1
        },
        {
            "deadends": ["8887","8889","8878","8898","8788","8988","7888","9888"],
            "target": "8888",
            "expected": -1
        },
        {
            "deadends": ["0000"],
            "target": "8888",
            "expected": -1
        },
        {
            "deadends": [],
            "target": "9999",
            "expected": 4
        },
        {
            "deadends": ["1111"],
            "target": "1111",
            "expected": -1
        },
        {
            "deadends": ["0001"],
            "target": "9999",
            "expected": 8
        }
    ]

    correct_count = 0
    for i, test in enumerate(tests):
        result = solve_lock(test["deadends"], test["target"])
        if result == test["expected"]:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
    print(f"{correct_count}/{len(tests)}")

if __name__ == '__main__':
    run_tests()