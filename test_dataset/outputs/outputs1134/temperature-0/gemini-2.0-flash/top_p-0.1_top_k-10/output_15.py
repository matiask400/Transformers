def can_cross(stones):
    """
    Determines if the frog can cross the river by landing on the last stone.

    Args:
        stones: A list of stones' positions (in units) in sorted ascending order.

    Returns:
        True if the frog can cross the river, False otherwise.
    """

    if not stones or len(stones) < 2:
        return False

    stone_set = set(stones)
    jumps = {0: {0}}  # {stone_position: {possible_jump_sizes}}

    for stone in stones:
        if stone in jumps:
            for jump_size in jumps[stone]:
                for next_jump in [jump_size - 1, jump_size, jump_size + 1]:
                    if next_jump > 0 and stone + next_jump in stone_set:
                        if stone + next_jump not in jumps:
                            jumps[stone + next_jump] = set()
                        jumps[stone + next_jump].add(next_jump)

    return stones[-1] in jumps


def test_can_cross():
    """
    Tests the can_cross function with several test cases.
    """

    test_cases = [
        ([0, 1, 3, 5, 6, 8, 12, 17], True),
        ([0, 1, 2, 3, 4, 8, 9, 11], False),
        ([0, 1], True),
        ([0, 2], False),
        ([0, 1, 3, 6, 10, 15], False),
        ([0, 1, 2, 3, 5, 6, 8, 12, 17], True),
        ([0, 1, 2, 3, 5, 6, 7, 9, 13, 17], True),
        ([0, 1, 2, 3, 5, 6, 7, 9, 13, 18], False),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], True),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21], False)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (stones, expected) in enumerate(test_cases):
        result = can_cross(stones)
        if result == expected:
            print(f"Test {i + 1}: True")
            correct_count += 1
        else:
            print(f"Test {i + 1}: False")

    print(f"\n{correct_count}/{total_count}")


if __name__ == "__main__":
    test_can_cross()