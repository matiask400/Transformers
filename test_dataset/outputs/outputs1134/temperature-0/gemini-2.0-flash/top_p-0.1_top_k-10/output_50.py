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

def test_candy():
    test_cases = [
        ([1, 0, 2], 5),
        ([1, 2, 2], 4),
        ([1, 2, 3, 4, 5], 15),
        ([5, 4, 3, 2, 1], 15),
        ([1, 2, 3, 2, 1], 9),
        ([1, 0, 1, 0, 1], 7),
        ([0], 1),
        ([0, 0, 0], 3),
        ([1, 2, 87, 87, 87, 2, 1], 13)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for ratings, expected in test_cases:
        result = candy(ratings)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_candy()