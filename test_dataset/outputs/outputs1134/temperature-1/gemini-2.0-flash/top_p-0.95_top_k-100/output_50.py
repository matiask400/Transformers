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
        ([1, 0, 1, 0, 1], 9),
        ([1, 2, 87, 87, 87, 2, 1], 13),
        ([1, 6, 10, 8, 5, 10, 6, 3, 2, 1], 18),
        ([0], 1),
        ([0, 0], 2),
        ([0, 0, 0], 3),
        ([0,1,2,5,3,2,7],13)
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, (ratings, expected) in enumerate(enumerate(test_cases)):
        actual = candy(ratings)
        if actual == expected:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False (Input: {ratings}, Expected: {expected}, Actual: {actual})")

    print(f"\n{num_correct}/{total_tests} correct")

if __name__ == "__main__":
    test_candy()