def solve_frog_jump(stones):
    stone_positions = set(stones)
    stone_indices = {stone: index for index, stone in enumerate(stones)}
    memo = {}

    def can_reach(current_index, last_jump):
        if current_index == len(stones) - 1:
            return True
        if (current_index, last_jump) in memo:
            return memo[(current_index, last_jump)]

        for next_jump in [last_jump - 1, last_jump, last_jump + 1]:
            if next_jump > 0:
                next_pos = stones[current_index] + next_jump
                if next_pos in stone_positions:
                    next_index = stone_indices[next_pos]
                    if next_index > current_index:
                        if can_reach(next_index, next_jump):
                            memo[(current_index, last_jump)] = True
                            return True

        memo[(current_index, last_jump)] = False
        return False

    return can_reach(0, 1)

def run_tests():
    tests = [
        ([0,1,3,5,6,8,12,17], True),
        ([0,1,2,3,4,8,9,11], False),
        ([0,1], True),
        ([0, 2], False),
        ([0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165579041, 267914206, 433493247, 701408733, 1134903170, 1836311903], True)
    ]
    correct_count = 0
    for i, (stones, expected_output) in enumerate(tests):
        output = solve_frog_jump(stones)
        if output == expected_output:
            print(f'Test {i+1}: True')
            correct_count += 1
        else:
            print(f'Test {i+1}: False')
    print(f'{correct_count}/{len(tests)}')

if __name__ == '__main__':
    run_tests()