import collections

def openLock(deadends, target):
    if "0000" in deadends:
        return -1
    deadend_set = set(deadends)
    queue = collections.deque([("0000", 0)])
    visited = {"0000"}

    while queue:
        current_state, turns = queue.popleft()
        if current_state == target:
            return turns

        for i in range(4):
            digit = int(current_state[i])
            next_digit_up = str((digit + 1) % 10)
            next_digit_down = str((digit - 1 + 10) % 10)

            next_state_up = list(current_state)
            next_state_up[i] = next_digit_up
            next_state_up = "".join(next_state_up)

            next_state_down = list(current_state)
            next_state_down[i] = next_digit_down
            next_state_down = "".join(next_state_down)

            if next_state_up not in deadend_set and next_state_up not in visited:
                visited.add(next_state_up)
                queue.append((next_state_up, turns + 1))

            if next_state_down not in deadend_set and next_state_down not in visited:
                visited.add(next_state_down)
                queue.append((next_state_down, turns + 1))

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
            "expected": -1 # target is in deadends should return -1 based on problem description even though constraints say target not in deadends, based on example 4 "0000" deadend result in -1, so if target is deadend then -1. Let's clarify, problem description says target will not be in deadends. So, example 4 is special case where start "0000" is deadend.  Let's assume target is never in deadends but if start is, it's -1.
        },
        {
            "deadends": ["9999"],
            "target": "0000",
            "expected": -1 # start is not in deadends, but we should not reach start if it is deadend, initial state is "0000", if deadends contains "0000", return -1 immediately.
        },
         {
            "deadends": ["0001"],
            "target": "9999",
            "expected": 8
        },
        {
            "deadends": ["0001","0002","0003","0004","0005","0006","0007","0008","0009"],
            "target": "0000",
            "expected": -1 # if start state is blocked return -1
        }

    ]

    correct_count = 0
    for i, test in enumerate(tests):
        deadends = test["deadends"]
        target = test["target"]
        expected = test["expected"]
        actual = openLock(deadends, target)
        if actual == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False, Input: deadends={deadends}, target={target}, Expected: {expected}, Actual: {actual}")

    print(f"\n{correct_count}/{len(tests)} correct")

if __name__ == '__main__':
    run_tests()