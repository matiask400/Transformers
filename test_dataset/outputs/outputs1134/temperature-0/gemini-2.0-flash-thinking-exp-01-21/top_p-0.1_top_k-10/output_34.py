from collections import deque
from fractions import Fraction

def solve():
    def get_min_operators(x, target):
        if x == target:
            return 0
        q = deque([(Fraction(x), 0)])
        visited = {Fraction(x): 0}
        while q:
            current_val, current_ops = q.popleft()
            if current_val == target:
                return current_ops
            if current_ops >= 10: # Heuristic limit, can be adjusted
                continue

            next_vals = [
                current_val + x,
                current_val - x,
                current_val * x,
                current_val / x if x != 0 else None # Avoid division by zero, though x is positive integer
            ]

            for next_val in next_vals:
                if next_val is not None:
                    if next_val not in visited or current_ops + 1 < visited[next_val]:
                        visited[next_val] = current_ops + 1
                        q.append((next_val, current_ops + 1))
        return -1 # Should not reach here based on problem description

    def run_test(x, target, expected_output):
        actual_output = get_min_operators(x, target)
        if actual_output == expected_output:
            print('True')
        else:
            print('False')
        return actual_output == expected_output

    test_cases = [
        {'x': 3, 'target': 19, 'expected': 5},
        {'x': 5, 'target': 501, 'expected': 8},
        {'x': 100, 'target': 100000000, 'expected': 3},
        {'x': 2, 'target': 2, 'expected': 0},
        {'x': 2, 'target': 4, 'expected': 1},
        {'x': 2, 'target': 0, 'expected': 1},
        {'x': 2, 'target': 1, 'expected': 1},
        {'x': 2, 'target': 3, 'expected': 2},
        {'x': 3, 'target': 27, 'expected': 2},
        {'x': 3, 'target': 81, 'expected': 3},
        {'x': 6, 'target': 7, 'expected': 2},
        {'x': 7, 'target': 6, 'expected': 2},
        {'x': 10, 'target': 1, 'expected': 1},
        {'x': 10, 'target': 100, 'expected': 1},
        {'x': 10, 'target': 1000, 'expected': 2},
        {'x': 2, 'target': 16, 'expected': 3},
        {'x': 2, 'target': 32, 'expected': 4},
        {'x': 2, 'target': 64, 'expected': 5},
        {'x': 2, 'target': 128, 'expected': 6},
        {'x': 2, 'target': 256, 'expected': 7},
        {'x': 2, 'target': 512, 'expected': 8},
        {'x': 2, 'target': 1024, 'expected': 9},
        {'x': 2, 'target': 2048, 'expected': 10},
        {'x': 3, 'target': 1, 'expected': 1},
        {'x': 3, 'target': 2, 'expected': 3},
        {'x': 3, 'target': 4, 'expected': 3},
        {'x': 3, 'target': 5, 'expected': 4},
        {'x': 3, 'target': 6, 'expected': 1},
        {'x': 3, 'target': 7, 'expected': 4},
        {'x': 3, 'target': 8, 'expected': 5},
        {'x': 3, 'target': 9, 'expected': 1},
        {'x': 3, 'target': 10, 'expected': 3},
        {'x': 3, 'target': 11, 'expected': 4},
        {'x': 3, 'target': 12, 'expected': 2},
        {'x': 3, 'target': 13, 'expected': 5},
        {'x': 3, 'target': 14, 'expected': 6},
        {'x': 3, 'target': 15, 'expected': 3},
        {'x': 3, 'target': 16, 'expected': 7},
        {'x': 3, 'target': 17, 'expected': 8},
        {'x': 3, 'target': 18, 'expected': 2},
        {'x': 3, 'target': 20, 'expected': 6},
        {'x': 3, 'target': 21, 'expected': 3},
        {'x': 3, 'target': 22, 'expected': 7},
        {'x': 3, 'target': 23, 'expected': 8},
        {'x': 3, 'target': 24, 'expected': 3},
        {'x': 3, 'target': 25, 'expected': 9},
        {'x': 3, 'target': 26, 'expected': 10},
        {'x': 4, 'target': 64, 'expected': 2},
        {'x': 4, 'target': 65, 'expected': 5},
        {'x': 6, 'target': 30, 'expected': 2},
        {'x': 7, 'target': 49, 'expected': 1},
        {'x': 8, 'target': 64, 'expected': 1},
        {'x': 9, 'target': 81, 'expected': 1},
        {'x': 10, 'target': 100, 'expected': 1},
        {'x': 2, 'target': 1000000, 'expected': 19}, # Added to test larger numbers
        {'x': 3, 'target': 1000, 'expected': 10}, # Added to test larger numbers
        {'x': 5, 'target': 1000, 'expected': 6}, # Added to test larger numbers
        {'x': 10, 'target': 10000, 'expected': 3}, # Added to test larger numbers
        {'x': 10, 'target': 100000, 'expected': 4}, # Added to test larger numbers
        {'x': 10, 'target': 1000000, 'expected': 5}, # Added to test larger numbers
        {'x': 10, 'target': 10000000, 'expected': 6}, # Added to test larger numbers
        {'x': 10, 'target': 100000000, 'expected': 3}, # Example 3 again
        {'x': 3, 'target': 19, 'expected': 5}, # Example 1 again
        {'x': 5, 'target': 501, 'expected': 8}, # Example 2 again
    ]

    correct_count = 0
    for test in test_cases:
        if run_test(test['x'], test['target'], test['expected']):
            correct_count += 1

    print(f"{correct_count}/{len(test_cases)}")

solve()