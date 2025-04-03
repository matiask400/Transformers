def candy(ratings):
    n = len(ratings)
    candies = [1] * n

    # Left to right pass
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Right to left pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)

def run_tests():
    test_cases = [
        ([1, 0, 2], 5),
        ([1, 2, 2], 4),
        ([1], 1),
        ([1, 3, 4, 5, 2], 11),
        ([1, 2, 87, 87, 87, 2, 1], 13),
        ([2, 2, 2, 2, 2], 5),
        ([1, 3, 2, 2, 1], 7),
        ([1, 6, 10, 8, 7, 3, 2], 12),
    ]

    correct = 0
    for ratings, expected in test_cases:
        result = candy(ratings)
        if result == expected:
            print('True')
            correct += 1
        else:
            print('False')
    print(f"{correct}/{len(test_cases)}")

if __name__ == "__main__":
    run_tests()