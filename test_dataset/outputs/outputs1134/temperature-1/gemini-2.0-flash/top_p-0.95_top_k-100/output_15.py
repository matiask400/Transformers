def can_cross(stones):
    """
    Determines if the frog can cross the river by landing on the last stone.

    Args:
        stones: A list of integers representing the positions of the stones in sorted ascending order.

    Returns:
        True if the frog can cross the river, False otherwise.
    """

    n = len(stones)
    if n == 2:
        return stones[1] == 1

    stone_positions = {stone: i for i, stone in enumerate(stones)}
    reachable = {0: {1}}

    for i in range(n - 1):
        stone = stones[i]
        if stone not in reachable:
            continue

        for k in reachable[stone]:
            for jump in [k - 1, k, k + 1]:
                if jump > 0 and stone + jump in stone_positions:
                    next_stone_index = stone_positions[stone + jump]
                    if stone + jump not in reachable:
                        reachable[stone + jump] = set()
                    reachable[stone + jump].add(jump)

    return stones[-1] in reachable


def test_can_cross():
    """
    Tests the can_cross function with several test cases.
    """
    test_cases = [
        ([0, 1, 3, 5, 6, 8, 12, 17], True),
        ([0, 1, 2, 3, 4, 8, 9, 11], False),
        ([0, 1], True),
        ([0, 2], False),
        ([0, 1, 2, 3, 5, 6, 7, 9], True),
        ([0, 1, 2, 3, 5], False),
        ([0,1,3,6,10,15], False),
        ([0, 1, 3, 6, 7], False)
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (stones, expected) in enumerate(test_cases):
        actual = can_cross(stones)
        if actual == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")

    print(f"\nCorrect tests: {correct_count}/{total_tests}")


if __name__ == "__main__":
    test_can_cross()