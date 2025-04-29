def count_prime_set_bits(L: int, R: int) -> int:
    """
    Given two integers `L` and `R`, find the count of numbers in the range `[L, R]`
    (inclusive) having a prime number of set bits in their binary representation.

    (Recall that the number of set bits an integer has is the number of `1`s present
    when written in binary.  For example, `21` written in binary is `10101` which
    has 3 set bits.  Also, 1 is not a prime.)

    Example 1:
    Input: L = 6, R = 10
    Output: 4
    Explanation:
    6 -> 110 (2 set bits, 2 is prime)
    7 -> 111 (3 set bits, 3 is prime)
    9 -> 1001 (2 set bits , 2 is prime)
    10->1010 (2 set bits , 2 is prime)

    Example 2:
    Input: L = 10, R = 15
    Output: 5
    Explanation:
    10 -> 1010 (2 set bits, 2 is prime)
    11 -> 1011 (3 set bits, 3 is prime)
    12 -> 1100 (2 set bits, 2 is prime)
    13 -> 1101 (3 set bits, 3 is prime)
    14 -> 1110 (3 set bits, 3 is prime)
    15 -> 1111 (4 set bits, 4 is not prime)
    Note:
    `L, R` will be integers `L <= R` in the range `[1, 10^6]`.

    `R - L` will be at most 10000.
    """
    primes = {2, 3, 5, 7, 11, 13, 17, 19}
    count = 0
    for i in range(L, R + 1):
        set_bits = bin(i).count('1')
        if set_bits in primes:
            count += 1
    return count


def test_count_prime_set_bits():
    test_cases = [
        ((6, 10), 4),
        ((10, 15), 5),
        ((1, 10), 4),
        ((1, 1), 0),
        ((2, 2), 1),
        ((0, 0), 0),
        ((1, 2), 1),
        ((1, 3), 2)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (input_args, expected_output) in enumerate(test_cases):
        L, R = input_args
        actual_output = count_prime_set_bits(L, R)
        if actual_output == expected_output:
            print(f"Test {i + 1}: True")
            correct_count += 1
        else:
            print(f"Test {i + 1}: False (Expected: {expected_output}, Actual: {actual_output})")

    print(f"{correct_count}/{total_count}")


if __name__ == "__main__":
    test_count_prime_set_bits()