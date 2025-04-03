from fractions import Fraction
from collections import deque

def least_operations(x, target):
    from fractions import Fraction
    from collections import deque

    # BFS initialization
    queue = deque()
    queue.append((Fraction(x), 0))
    visited = set()
    visited.add(Fraction(x))

    while queue:
        current, ops = queue.popleft()
        if current == target:
            return ops
        # Apply operations
        for op in ['+', '-', '*', '/']:
            if op == '+':
                next_val = current + x
            elif op == '-':
                next_val = current - x
            elif op == '*':
                next_val = current * x
            elif op == '/':
                if x != 0:
                    next_val = current / x
                else:
                    continue
            if next_val not in visited:
                visited.add(next_val)
                queue.append((next_val, ops + 1))
    return -1  # If target is not reachable

def run_tests():
    tests = [
        ((3, 19), 5),
        ((5, 501), 8),
        ((100, 100000000), 3)
    ]
    correct = 0
    total = len(tests)
    for i, ((x, target), expected) in enumerate(tests):
        result = least_operations(x, Fraction(target))
        if result == expected:
            print(True)
            correct += 1
        else:
            print(False)
    print(f"{correct}/{total}")

run_tests()