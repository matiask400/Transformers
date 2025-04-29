from functools import lru_cache
from collections import Counter

def run_tests():
    def alice_wins(nums):
        initial_xor = 0
        for num in nums:
            initial_xor ^= num

        counter = Counter(nums)
        unique_nums = tuple(sorted(counter.items()))
        
        @lru_cache(None)
        def can_win(state, current_xor):
            if current_xor == 0:
                return True  # Current player wins
            state_counter = Counter(dict(state))
            for num in state_counter:
                next_xor = current_xor ^ num
                if state_counter[num] == 1:
                    next_state = tuple(sorted((k, v) for k, v in state_counter.items() if k != num))
                else:
                    next_state = tuple(sorted((k, v-1) if k == num else (k, v) for k, v in state_counter.items()))
                if next_xor == 0:
                    continue  # This move makes current_xor 0, which is a losing move
                opponent_can_win = can_win(next_state, next_xor)
                if not opponent_can_win:
                    return True  # Current player can force a win
            return False  # No winning moves

        return can_win(unique_nums, initial_xor)

    test_cases = [
        # (nums, expected_output)
        ([1, 1, 2], False),
        ([0], True),
        ([1, 2, 3], True),
        ([4, 4, 4, 4], True),
        ([1, 2, 1, 2], True),
        ([1, 1, 1], False),
        ([2, 2, 3, 3, 4], True),
        ([5, 5, 5, 5, 5], False),
        ([7, 7, 7, 7, 7, 7], True),
        ([8], True)
    ]

    correct = 0
    total = len(test_cases)
    for idx, (nums, expected) in enumerate(test_cases, 1):
        result = alice_wins(nums)
        test_passed = result == expected
        print(test_passed)
        if test_passed:
            correct += 1
    print(f"{correct}/{total}")

run_tests()