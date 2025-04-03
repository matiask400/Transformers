def solve():
    def can_cross_river(stones):
        n = len(stones)
        if n <= 1:
            return False
        if stones[1] != 1:
            return False

        memo = {}

        def is_possible(current_index, last_jump):
            if current_index == n - 1:
                return True
            if (current_index, last_jump) in memo:
                return memo[(current_index, last_jump)]

            for next_jump in [last_jump - 1, last_jump, last_jump + 1]:
                if next_jump > 0:
                    next_stone_pos = stones[current_index] + next_jump
                    for next_index in range(current_index + 1, n):
                        if stones[next_index] == next_stone_pos:
                            if is_possible(next_index, next_jump):
                                memo[(current_index, last_jump)] = True
                                return True

            memo[(current_index, last_jump)] = False
            return False

        return is_possible(1, 1)

    test_cases = [
        ([0, 1, 3, 5, 6, 8, 12, 17], True),
        ([0, 1, 2, 3, 4, 8, 9, 11], False),
        ([0, 1], True),
        ([0, 2], False),
        ([0, 1, 10], False),
        ([0, 1, 2, 5], False),
        ([0,1,2,3,4,5,6,7,8,9,10], True),
        ([0, 1, 3, 6, 10, 15], True),
        ([0, 1, 2, 3, 5, 6, 7, 8], False),
        ([0, 1, 2, 3, 5, 7, 9, 12], True)
    ]

    correct_count = 0
    for i, (stones, expected_output) in enumerate(test_cases):
        actual_output = can_cross_river(stones)
        if actual_output == expected_output:
            print(f'Test {i+1}: True')
            correct_count += 1
        else:
            print(f'Test {i+1}: False')

    print(f'{correct_count}/{len(test_cases)}')

solve()