def smallest_repunit_divByK(K: int) -> int:
    """
    Given a positive integer `K`, you need to find the length of the smallest positive integer `N` such that `N` is divisible by `K`, and `N` only contains the digit `1`.

    Return the length of `N`. If there is no such `N`, return -1.

    Note: `N` may not fit in a 64-bit signed integer.
    """
    if K % 2 == 0 or K % 5 == 0:
        return -1

    remainder = 0
    length = 0
    for i in range(1, K + 1):
        remainder = (remainder * 10 + 1) % K
        length += 1
        if remainder == 0:
            return length

    return -1

def test_smallest_repunit_divByK():
    test_cases = [
        (1, 1),
        (2, -1),
        (3, 3),
        (7, 6),
        (9, 9),
        (11, 2),
        (13, 6),
        (17, 16),
        (19, 18),
        (21, 6),
        (23, 22),
        (101, 4),
        (99991, 5),
        (99999, 9),
        (100000, -1)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for K, expected in test_cases:
        result = smallest_repunit_divByK(K)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

if __name__ == '__main__':
    test_smallest_repunit_divByK()