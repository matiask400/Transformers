import collections
import sys

def isNStraightHand(hand, W):
    """
    Checks if the hand can be rearranged into groups of W consecutive cards.

    Args:
        hand: A list of integers representing the cards.
        W: The desired size of each group.

    Returns:
        True if the hand can be rearranged as specified, False otherwise.
    """
    n = len(hand)

    # 1. Check if the total number of cards is divisible by W.
    # If not, it's impossible to form groups of size W using all cards.
    if n % W != 0:
        return False

    # 2. Handle the edge case where W is 1. Any hand can be divided into
    # groups of size 1.
    if W == 1:
        return True

    # 3. Count the frequency of each card number.
    counts = collections.Counter(hand)

    # 4. Get the unique card numbers and sort them. This allows us to
    # process potential groups starting from the smallest card.
    sorted_keys = sorted(counts.keys())

    # 5. Iterate through the sorted unique card numbers.
    for card in sorted_keys:
        # If we have instances of the current 'card' left to process...
        # This 'card' must be the start of a new consecutive group(s)
        # because we are processing cards in ascending order.
        if counts[card] > 0:
            num_groups_starting_here = counts[card]

            # Try to form 'num_groups_starting_here' groups starting with 'card'.
            # Each group needs cards: card, card + 1, ..., card + W - 1.
            for i in range(W):
                current_card_needed = card + i

                # Check if we have enough of the required consecutive card.
                if counts[current_card_needed] < num_groups_starting_here:
                    # Not enough cards to form the required number of groups.
                    return False

                # "Use up" the cards for the groups we are forming.
                counts[current_card_needed] -= num_groups_starting_here

                # Optional optimization: if count becomes 0, we could remove the key,
                # but Counter handles lookups of 0-count keys fine.

    # If we successfully processed all cards and formed groups, return True.
    return True

def run_tests():
    """
    Runs predefined test cases against the isNStraightHand function.
    """
    test_cases = [
        # Example 1
        {'input': {'hand': [1, 2, 3, 6, 2, 3, 4, 7, 8], 'W': 3}, 'expected': True},
        # Example 2
        {'input': {'hand': [1, 2, 3, 4, 5], 'W': 4}, 'expected': False},
        # Additional Test Cases
        {'input': {'hand': [1, 1, 2, 2, 3, 3], 'W': 3}, 'expected': True},
        {'input': {'hand': [1, 1, 2, 2, 3, 3], 'W': 2}, 'expected': True},
        {'input': {'hand': [1, 2, 3, 4, 5, 6], 'W': 3}, 'expected': True},
        {'input': {'hand': [1, 2, 3, 4, 5], 'W': 3}, 'expected': False}, # Length not divisible
        {'input': {'hand': [1], 'W': 1}, 'expected': True},
        {'input': {'hand': [], 'W': 3}, 'expected': True}, # Empty hand, 0 groups needed
        {'input': {'hand': [5, 1], 'W': 1}, 'expected': True},
        {'input': {'hand': [8, 10, 12], 'W': 3}, 'expected': False}, # Not consecutive
        {'input': {'hand': [1, 2, 3, 3, 4, 5], 'W': 3}, 'expected': False}, # Cannot form second group
        {'input': {'hand': [1, 1, 1, 2, 2, 2, 3, 3, 3], 'W': 3}, 'expected': True},
        {'input': {'hand': [1, 2, 3, 4], 'W': 2}, 'expected': True},
        {'input': {'hand': [1, 2, 3, 5, 6, 7], 'W': 3}, 'expected': False}, # Gap in numbers
        {'input': {'hand': [i for i in range(100)], 'W': 10}, 'expected': True}, # Larger test
        {'input': {'hand': [i for i in range(99)], 'W': 10}, 'expected': False}, # Larger test - not divisible
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, test in enumerate(test_cases):
        hand_input = test['input']['hand']
        W_input = test['input']['W']
        expected_output = test['expected']

        # Use a copy of the hand list to avoid modifying the original test case data
        # if the function were to modify the list in place (though this one doesn't).
        actual_output = isNStraightHand(hand_input.copy(), W_input)

        if actual_output == expected_output:
            print(f"True")
            correct_count += 1
        else:
            print(f"False")
            # Optional: Print details for failed tests
            # print(f"  Test Case {i+1} Failed:")
            # print(f"  Input: hand={hand_input}, W={W_input}")
            # print(f"  Expected: {expected_output}, Got: {actual_output}")


    print(f"{correct_count}/{total_tests}")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()