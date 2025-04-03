import math

# Define the core function to solve the problem
def solve(L, R):
    """
    Counts numbers in the range [L, R] having a prime number of set bits.

    Args:
        L: The lower bound of the range (inclusive).
        R: The upper bound of the range (inclusive).

    Returns:
        The count of numbers satisfying the condition.
    """

    # Determine the maximum possible number of set bits.
    # Since R <= 10^6, and 2^20 > 10^6, the maximum number of bits needed
    # is 20. So, we only need primes up to 20.
    # Primes up to 20 are: 2, 3, 5, 7, 11, 13, 17, 19.
    # We use a set for efficient lookup.
    prime_set_bits = {2, 3, 5, 7, 11, 13, 17, 19}

    count = 0
    for num in range(L, R + 1):
        # Calculate the number of set bits (1s) in the binary representation
        # Using bin(num) which returns '0b...' string, and counting '1's
        set_bits = bin(num).count('1')

        # Check if the count of set bits is in our precomputed set of primes
        if set_bits in prime_set_bits:
            count += 1

    return count

# Define the test function
def run_tests():
    """
    Runs predefined test cases against the solve function and prints the results.
    """
    test_cases = [
        # Example 1
        (6, 10, 4),
        # Example 2
        (10, 15, 5),
        # Custom Test Cases
        (1, 1, 0),      # 1 -> 1 (1 set bit, 1 is not prime)
        (2, 2, 0),      # 2 -> 10 (1 set bit, 1 is not prime)
        (3, 3, 1),      # 3 -> 11 (2 set bits, 2 is prime)
        (2, 3, 1),      # Range [2, 3]: 3 is the only one
        (1, 10, 6),     # Range [1, 10]: 3, 5, 6, 7, 9, 10 (counts: 2, 2, 2, 3, 2, 2)
        (840, 850, 6),  # A slightly larger range test
        (999990, 1000000, 5) # Test near the upper bound
    ]

    correct_count = 0
    total_tests = len(test_cases)

    print("Running tests...")
    for i, (L, R, expected) in enumerate(test_cases):
        result = solve(L, R)
        passed = result == expected
        print(f"Test {i+1}: {passed}")
        if passed:
            correct_count += 1
        # Optional: Print details on failure for debugging
        # else:
        #     print(f"  Input: L={L}, R={R}")
        #     print(f"  Expected: {expected}")
        #     print(f"  Got: {result}")

    print(f"\nResult: {correct_count}/{total_tests} tests passed.")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()