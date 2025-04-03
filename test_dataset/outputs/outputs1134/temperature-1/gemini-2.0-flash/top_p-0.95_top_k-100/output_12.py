def is_n_straight_hand(hand, W):
    """
    Determines if Alice can rearrange her hand into groups of size W with consecutive cards.

    Args:
        hand: A list of integers representing Alice's hand.
        W: The size of each group.

    Returns:
        True if Alice can rearrange her hand, False otherwise.
    """

    if len(hand) % W != 0:
        return False

    hand.sort()
    count = {}
    for card in hand:
        count[card] = count.get(card, 0) + 1

    for card in hand:
        if count.get(card, 0) > 0:
            for i in range(W):
                needed_card = card + i
                if count.get(needed_card, 0) == 0:
                    return False
                count[needed_card] -= 1

    return True


def test_is_n_straight_hand():
    """
    Tests the is_n_straight_hand function with several test cases.
    """
    test_cases = [
        (([1, 2, 3, 6, 2, 3, 4, 7, 8], 3), True),
        (([1, 2, 3, 4, 5], 4), False),
        (([3, 2, 1, 2, 3, 4, 3, 4, 5], 3), True),
        (([1, 2, 3], 1), True),
        (([1, 2, 3, 4], 2), True),
        (([1, 2, 3, 4, 5, 6], 3), True),
        (([1, 2, 3, 4, 5, 6], 2), True),
        (([1, 2, 3, 4, 5, 6], 1), True),
        (([1, 2, 3, 4, 5, 6, 7], 3), False),
        (([1], 1), True),
        (([1, 1, 1, 2, 2, 2, 3, 3], 3), False)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for (input_hand, w), expected_output in test_cases:
        actual_output = is_n_straight_hand(input_hand, w)
        if actual_output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Input: hand={input_hand}, W={w}")
            print(f"Expected: {expected_output}, Actual: {actual_output}")

    print(f"{correct_count}/{total_count}")


if __name__ == "__main__":
    test_is_n_straight_hand()