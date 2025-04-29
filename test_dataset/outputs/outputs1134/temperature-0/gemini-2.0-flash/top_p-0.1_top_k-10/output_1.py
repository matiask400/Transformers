def count_prime_set_bits(L, R):
    """
    Counts the numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

    Args:
        L: The left bound of the range.
        R: The right bound of the range.

    Returns:
        The count of numbers in the range [L, R] having a prime number of set bits.
    """

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def count_set_bits(n):
        count = 0
        while n > 0:
            n &= (n - 1)
            count += 1
        return count

    count = 0
    for i in range(L, R + 1):
        set_bits = count_set_bits(i)
        if is_prime(set_bits):
            count += 1
    return count


def test_count_prime_set_bits():
    test_cases = [
        ((6, 10), 4),
        ((10, 15), 5),
        ((1, 1), 0),
        ((1, 2), 1),
        ((1, 3), 2),
        ((1, 4), 2),
        ((1, 5), 3),
        ((1, 6), 3),
        ((1, 7), 4),
        ((1, 8), 4),
        ((1, 9), 4),
        ((1, 10), 5),
        ((1, 100), 33),
        ((1, 1000), 251),
        ((1, 10000), 1912),
        ((1, 100000), 14693),
        ((1, 1000000), 113527),
        ((6617, 6621), 1),
        ((6617, 6622), 2),
        ((6617, 6623), 3),
        ((6617, 6624), 3),
        ((6617, 6625), 3),
        ((6617, 6626), 3),
        ((6617, 6627), 3),
        ((6617, 6628), 3),
        ((6617, 6629), 3),
        ((6617, 6630), 3),
        ((6617, 6631), 4),
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (args, expected) in enumerate(test_cases):
        result = count_prime_set_bits(*args)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Input: {args}, Expected: {expected}, Got: {result})")

    print(f"\nCorrect: {correct_count}/{total_tests}")


if __name__ == "__main__":
    test_count_prime_set_bits()