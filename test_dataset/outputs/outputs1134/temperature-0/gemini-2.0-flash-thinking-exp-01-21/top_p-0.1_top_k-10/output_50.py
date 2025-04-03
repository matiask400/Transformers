def solve():
    def candy(ratings):
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)

    def run_test(ratings, expected_output):
        output = candy(ratings)
        if output == expected_output:
            print('True')
        else:
            print('False')
        return output == expected_output

    test_cases = [
        ([1, 0, 2], 5),
        ([1, 2, 2], 4),
        ([1, 3, 2, 2, 1], 7),
        ([0], 1),
        ([1, 1, 1], 3),
        ([1, 2, 3, 4, 5], 15),
        ([5, 4, 3, 2, 1], 15),
        ([1, 2, 3, 2, 1], 9),
        ([2, 1, 0], 6),
        ([1, 2, 87, 87, 87, 2, 1], 13)
    ]

    correct_count = 0
    for ratings, expected_output in test_cases:
        if run_test(ratings, expected_output):
            correct_count += 1

    print(f"{correct_count}/{len(test_cases)}")

solve()