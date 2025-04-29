from collections import Counter

def is_possible_hand(hand, W):
    """
    Checks if Alice can rearrange her hand into groups of size W of consecutive cards.

    Args:
        hand: A list of integers representing Alice's hand.
        W: The size of each group and the number of consecutive cards in each group.

    Returns:
        True if Alice can rearrange her hand, False otherwise.
    """
    if len(hand) % W != 0:
        return False

    count = Counter(hand)
    sorted_hand = sorted(list(set(hand)))

    for start_card in sorted_hand:
        if count[start_card] > 0:
            for _ in range(count[start_card]):
                group_formed = True
                for i in range(W):
                    current_card = start_card + i
                    if count[current_card] == 0:
                        return False
                    count[current_card] -= 1
                if not group_formed:
                    return False
    return True

def run_tests():
    test_cases = [
        (([1, 2, 3, 6, 2, 3, 4, 7, 8], 3), True),
        (([1, 2, 3, 4, 5], 4), False),
        (([1,1,2,2,3,3], 3), True),
        (([1,1,2,3,3,4], 3), True),
        (([1,1,2,2,3,3], 2), True),
        (([1,2,3,4,5,6], 2), True),
        (([1,2,3,4,5,6], 3), True),
        (([1,2,3,4,5,6], 4), False),
        (([1,2,3,4,5,6], 5), False),
        (([1,2,3,4,5,6], 6), True),
        (([1], 1), True),
        (([1, 2], 2), True),
        (([1, 3], 2), False),
        (([1, 1, 2, 2], 2), True),
        (([1, 1, 1, 2, 2, 2], 3), True),
        (([1, 1, 1, 2, 2, 3], 3), True),
        (([1, 1, 1, 3, 3, 3], 3), False),
        (([0,0,1,1,2,2], 3), True),
        (([0,0,1,1,2,3], 3), False),
        (([0,1,2,3,4,5], 3), True),
        (([0,1,2,3,4,5,6,7,8,9,10,11], 3), True),
        (([0,1,2,3,4,5,6,7,8,9,10,11], 4), True),
        (([0,1,2,3,4,5,6,7,8,9,10,11], 6), True),
        (([0,1,2,3,4,5,6,7,8,9,10,11], 12), True),
        (([0,0,0,1,1,1,2,2,2], 3), True),
    ]

    correct_count = 0
    for i, (input_args, expected_output) in enumerate(test_cases):
        hand, W = input_args
        actual_output = is_possible_hand(hand, W)
        if actual_output == expected_output:
            print(True)
            correct_count += 1
        else:
            print(False)

    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()