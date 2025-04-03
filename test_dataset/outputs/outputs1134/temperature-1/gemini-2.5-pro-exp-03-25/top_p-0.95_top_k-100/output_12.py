import collections
from typing import List

def isNStraightHand(hand: List[int], W: int) -> bool:
    """
    Determines if a hand of cards can be rearranged into groups of W consecutive cards.

    Args:
        hand: A list of integers representing the cards.
        W: The desired size of each group.

    Returns:
        True if the hand can be rearranged as specified, False otherwise.
    """
    n = len(hand)

    # Condition 1: The total number of cards must be divisible by W.
    if n % W != 0:
        return False

    # Condition 2: Handle the edge case where W = 1. Any hand is valid if W=1
    # as long as the length constraint is met (checked above).
    if W == 1:
        return True

    # Count the frequency of each card.
    counts = collections.Counter(hand)

    # Get the unique card numbers in sorted order.
    # Processing cards in increasing order ensures that we always start
    # potential groups with the smallest available card.
    sorted_keys = sorted(counts.keys())

    # Iterate through the sorted unique card numbers.
    for num in sorted_keys:
        # If we have cards with the current number 'num'...
        if counts[num] > 0:
            # This 'num' must be the start of 'num_starts' groups.
            num_starts = counts[num]

            # Check if we can form 'num_starts' groups starting with 'num'.
            # Each group needs cards num, num+1, ..., num + W - 1.
            for i in range(W):
                card_needed = num + i
                # If we don't have enough of the required consecutive card...
                if counts[card_needed] < num_starts:
                    # We cannot form all the required groups starting at 'num'.
                    return False
                # Decrement the count for the card used in these 'num_starts' groups.
                counts[card_needed] -= num_starts

    # If we successfully processed all card numbers and formed groups, return True.
    # The counts of all cards should be zero at this point if successful.
    return True

# Testing framework
def run_tests():
    test_cases = [
        ([1,2,3,6,2,3,4,7,8], 3, True),
        ([1,2,3,4,5], 4, False),
        ([1,1,2,2,3,3], 3, True),
        ([1,2,3], 1, True),
        ([1,2,4,5,6,7], 3, False),
        ([8,10,12], 3, False), # Non-consecutive
        ([8, 9, 10, 10, 11, 12], 3, True),
        ([5, 1], 1, True),
        ([], 3, True), # Empty hand, 0 % 3 == 0
        ([1,1,1,2,2,2,3,3,3], 3, True),
        ([1,1,2,3,4], 3, False), # Not enough 2s
        ([1,2,3,3,4,4,5,6], 4, True),
         ([1], 2, False), # length % W != 0
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (hand, W, expected) in enumerate(test_cases):
        # Create a copy for mutable input
        hand_copy = list(hand)
        result = isNStraightHand(hand_copy, W)
        passed = result == expected
        print(f"Test {i+1}: Input=(hand={hand}, W={W}), Output={result}, Expected={expected} -> {passed}")
        if passed:
            correct_count += 1

    print(f"\nPassed {correct_count} out of {total_tests} tests.")

# Execute the tests
if __name__ == "__main__":
    run_tests()