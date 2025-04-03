def getLengthOfOptimalCompression(s: str, k: int) -> int:
    n = len(s)
    dp = {}

    def solve(i, k, last_char, last_count):
        if (i, k, last_char, last_count) in dp:
            return dp[(i, k, last_char, last_count)]

        if i == n:
            if last_count > 1:
                return len(str(last_count)) + 1
            elif last_count == 1:
                return 1
            else:
                return 0

        if k < 0:
            return float('inf')

        if s[i] == last_char:
            new_count = last_count + 1
            cost = 0
            if last_count == 1:
                cost = -1
            elif last_count in [9, 99, 999]:
                cost = 1

            result = solve(i + 1, k, last_char, new_count) + cost
        else:
            len_last_group = 0
            if last_count > 1:
                len_last_group = len(str(last_count)) + 1
            elif last_count == 1:
                len_last_group = 1
            else:
                len_last_group = 0

            result = min(solve(i + 1, k - 1, last_char, last_count), len_last_group + solve(i + 1, k, s[i], 1))

        dp[(i, k, last_char, last_count)] = result
        return result

    return solve(0, k, '', 0)


def test():
    test_cases = [
        (("aaabcccd", 2), 4),
        (("aabbaa", 2), 2),
        (("aaaaaaaaaaa", 0), 3),
        (("abc", 0), 3),
        (("ababcdcdababcdcd", 1), 16),
        (("zzzazz", 1), 3),
        (("crrrccrrrc", 6), 2)
    ]

    correct = 0
    total = len(test_cases)

    for (args, expected) in test_cases:
        result = getLengthOfOptimalCompression(*args)
        if result == expected:
            print("True")
            correct += 1
        else:
            print("False")
            print(f"Input: {args}, Expected: {expected}, Got: {result}")

    print(f"{correct}/{total}")


if __name__ == "__main__":
    test()