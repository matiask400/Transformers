from fractions import Fraction

def solve():
    def get_least_operators(x, target):
        initial_value = Fraction(x)
        target_fraction = Fraction(target)
        queue = [(initial_value, 0)]
        visited_values = {initial_value}
        operator_limit = 10  # Start with a limit, can increase if needed

        while queue:
            current_value, num_operators = queue.pop(0)
            if current_value == target_fraction:
                return num_operators
            if num_operators >= operator_limit:
                continue

            next_ops = ['+', '-', '*', '/']
            for op in next_ops:
                if op == '+':
                    next_value = current_value + Fraction(x)
                elif op == '-':
                    next_value = current_value - Fraction(x)
                elif op == '*':
                    next_value = current_value * Fraction(x)
                elif op == '/':
                    next_value = current_value / Fraction(x)
                else:
                    raise Exception("Unknown operator")

                if next_value not in visited_values:
                    visited_values.add(next_value)
                    queue.append((next_value, num_operators + 1))
        return -1 # Should not reach here given the problem description

    def run_test(x, target, expected_output):
        actual_output = get_least_operators(x, target)
        if actual_output == expected_output:
            print('True')
        else:
            print('False')
        return actual_output == expected_output

    test_cases = [
        {'x': 3, 'target': 19, 'expected': 5},
        {'x': 5, 'target': 501, 'expected': 8},
        {'x': 100, 'target': 100000000, 'expected': 3},
        {'x': 2, 'target': 4, 'expected': 1},
        {'x': 2, 'target': 2, 'expected': 1}, # e.g., 2 * 2 / 2
        {'x': 6, 'target': 30, 'expected': 2}, # 6 * 6 - 6
        {'x': 7, 'target': 43, 'expected': 2}, # 7 * 7 - 7 + 7 / 7
        {'x': 10, 'target': 99, 'expected': 2}, # 10 * 10 - 10 / 10
        {'x': 3, 'target': 27, 'expected': 2}, # 3 * 3 * 3
        {'x': 3, 'target': 1, 'expected': 1}, # 3 / 3
        {'x': 3, 'target': 0, 'expected': 1}, # 3 - 3
        {'x': 2, 'target': 3, 'expected': 2}, # 2 + 2 / 2
        {'x': 7, 'target': 6, 'expected': 2}, # 7 - 7 / 7
        {'x': 2, 'target': 8, 'expected': 2}, # 2 * 2 * 2
        {'x': 2, 'target': 0.5, 'expected': 2}, # 2 / 2 / 2

    ]

    correct_count = 0
    for case in test_cases:
        if run_test(case['x'], case['target'], case['expected']):
            correct_count += 1

    print(f"{correct_count}/{len(test_cases)}")

solve()