from collections import deque

def openLock(deadends, target):
    dead = set(deadends)
    if "0000" in dead:
        return -1
    visited = set("0000")
    queue = deque([("0000", 0)])
    
    while queue:
        state, steps = queue.popleft()
        if state == target:
            return steps
        for i in range(4):
            digit = int(state[i])
            for move in (-1, 1):
                new_digit = (digit + move) % 10
                new_state = state[:i] + str(new_digit) + state[i+1:]
                if new_state not in dead and new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))
    return -1

def run_tests():
    test_cases = [
        {
            "deadends": ["0201","0101","0102","1212","2002"],
            "target": "0202",
            "output": 6
        },
        {
            "deadends": ["8888"],
            "target": "0009",
            "output": 1
        },
        {
            "deadends": ["8887","8889","8878","8898","8788","8988","7888","9888"],
            "target": "8888",
            "output": -1
        },
        {
            "deadends": ["0000"],
            "target": "8888",
            "output": -1
        }
    ]
    
    passed = 0
    total = len(test_cases)
    
    for tc in test_cases:
        result = openLock(tc["deadends"], tc["target"])
        is_correct = result == tc["output"]
        print(is_correct)
        if is_correct:
            passed += 1
    print(f"{passed}/{total}")

run_tests()