from collections import deque

def open_lock(deadends, target):
    """
    You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.
    The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

    The lock initially starts at '0000', a string representing the state of the 4 wheels.

    You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

    Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
    """
    deadends = set(deadends)
    if "0000" in deadends:
        return -1

    queue = deque([("0000", 0)])
    visited = {"0000"}

    while queue:
        lock, moves = queue.popleft()

        if lock == target:
            return moves

        for i in range(4):
            digit = int(lock[i])
            next_digits = [(digit + 1) % 10, (digit - 1) % 10]

            for next_digit in next_digits:
                next_lock = lock[:i] + str(next_digit) + lock[i+1:]

                if next_lock not in deadends and next_lock not in visited:
                    queue.append((next_lock, moves + 1))
                    visited.add(next_lock)

    return -1

def test_open_lock():
    test_cases = [
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
            "target": "1111",
            "expected": 4
        },
        {
            "deadends": ["1111"],
            "target": "1111",
            "expected": -1
        },
        {
            "deadends": ["0001", "0002", "0003", "0004", "0005", "0006", "0007", "0008", "0009"],
            "target": "9999",
            "expected": -1
        }
    ]

    num_correct = 0
    for i, test_case in enumerate(test_cases):
        deadends = test_case["deadends"]
        target = test_case["target"]
        expected = test_case["expected"]
        actual = open_lock(deadends, target)

        if actual == expected:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Actual: {actual})")

    print(f"\n{num_correct}/{len(test_cases)} correct")

if __name__ == "__main__":
    test_open_lock()