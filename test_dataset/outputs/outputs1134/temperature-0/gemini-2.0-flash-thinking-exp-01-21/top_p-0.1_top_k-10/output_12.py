from collections import Counter

def is_possible_hand(hand, W):
    """
    Checks if Alice can rearrange her hand into groups of size W with consecutive cards.

    Args:
        hand: A list of integers representing Alice's hand of cards.
        W: The size of each group.

    Returns:
        True if Alice can rearrange her hand, False otherwise.
    """
    if len(hand) % W != 0:
        return False
    count = Counter(hand)
    sorted_hand = sorted(list(set(hand)))

    for card in sorted_hand:
        while count[card] > 0:
            for i in range(W):
                current_card = card + i
                if count[current_card] == 0:
                    return False
                count[current_card] -= 1
    return True

def run_tests():
    tests = [
        (([1, 2, 3, 6, 2, 3, 4, 7, 8], 3), True),
        (([1, 2, 3, 4, 5], 4), False),
        (([1, 2, 3, 4, 5, 6], 3), True),
        (([1, 2, 3, 4, 5, 6], 2), True),
        (([1, 2, 3, 4, 5, 6], 1), True),
        (([1, 1, 2, 2, 3, 3], 3), True),
        (([1, 1, 2, 2, 3, 3], 2), True),
        (([1, 1, 1, 2, 2, 2, 3, 3, 3], 3), True),
        (([1, 1, 1, 2, 2, 2, 3, 3, 3], 4), False),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3), True),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 4), True),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 6), True),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), True),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 13), False),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 3), False),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 2), False),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 1), True),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), True),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6), False),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), True),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9], 4), False),
        (([1, 2, 3, 4, 5, 6, 7, 8], 4), True),
        (([1, 2, 3, 4, 5, 6, 7, 8], 5), False),
        (([1, 2, 3, 4, 5, 6, 7], 7), True),
        (([1, 2, 3, 4, 5, 6, 7], 8), False),
        (([1, 2, 3, 4, 5, 6], 6), True),
        (([1, 2, 3, 4, 5, 6], 7), False),
        (([1, 2, 3, 4, 5], 5), True),
        (([1, 2, 3, 4, 5], 6), False),
        (([1, 2, 3, 4], 4), True),
        (([1, 2, 3, 4], 5), False),
        (([1, 2, 3], 3), True),
        (([1, 2, 3], 4), False),
        (([1, 2], 2), True),
        (([1, 2], 3), False),
        (([1], 1), True),
        (([1], 2), False),
        (([1, 1, 2, 2, 3, 3], 3), True),
        (([1, 1, 2, 2, 3, 3], 4), False),
        (([1, 1, 1, 2, 2, 2], 3), True),
        (([1, 1, 1, 2, 2, 2], 4), False),
        (([1, 1, 1, 1, 2, 2, 2, 2], 4), True),
        (([1, 1, 1, 1, 2, 2, 2, 2], 5), False),
        (([1, 1, 1, 1, 1, 2, 2, 2, 2, 2], 5), True),
        (([1, 1, 1, 1, 1, 2, 2, 2, 2, 2], 6), False),
        (([0,0,1,1,2,2], 3), True),
        (([0,0,1,1,2,2], 2), True),
        (([0,0,1,1,2,2], 4), False),
        (([0,0,0,1,1,1,2,2,2], 3), True),
        (([0,0,0,1,1,1,2,2,2], 4), False),
    ]

    correct_count = 0
    for i, (input_args, expected_output) in enumerate(tests):
        hand, W = input_args
        actual_output = is_possible_hand(hand, W)
        if actual_output == expected_output:
            print(f'Test {i+1}: True')
            correct_count += 1
        else:
            print(f'Test {i+1}: False')

    print(f"\n{correct_count}/{len(tests)} correct")

if __name__ == '__main__':
    run_tests()