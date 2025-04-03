from collections import Counter

def canDivideHand(hand, W):
    if len(hand) % W != 0:
        return False
    count = Counter(hand)
    for num in sorted(count):
        if count[num] > 0:
            needed = count[num]
            for i in range(num, num + W):
                if count.get(i, 0) < needed:
                    return False
                count[i] -= needed
    return True

# Define test cases as tuples of (hand, W, expected)
test_cases = [
    ([1,2,3,6,2,3,4,7,8], 3, True),
    ([1,2,3,4,5], 4, False),
]

correct = 0
total = len(test_cases)
for hand, W, expected in test_cases:
    result = canDivideHand(hand, W)
    if result == expected:
        print(True)
        correct += 1
    else:
        print(False)
print(f"{correct}/{total}")