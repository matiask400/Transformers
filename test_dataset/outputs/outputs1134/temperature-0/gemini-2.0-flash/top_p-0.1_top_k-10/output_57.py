def total_money(n: int) -> int:
    """
    Calculates the total amount of money Hercy will have in the Leetcode bank at the end of the nth day.

    Args:
        n: The number of days.

    Returns:
        The total amount of money.
    """
    weeks = n // 7
    remaining_days = n % 7
    total = 0
    for i in range(weeks):
        total += 7 * (i + 1) + 21
    for i in range(remaining_days):
        total += weeks + i + 1
    return total

def test_total_money():
    """
    Tests the total_money function with the provided examples and additional test cases.
    """
    test_cases = [
        (4, 10),
        (10, 37),
        (20, 96),
        (7, 28),
        (14, 70),
        (1, 1),
        (8, 30),
        (15, 79),
        (21, 112),
        (28, 140)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (n, expected) in enumerate(test_cases):
        actual = total_money(n)
        if actual == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Input: {n}, Expected: {expected}, Actual: {actual})")

    print(f"\n{correct_count}/{total_count} correct")

if __name__ == "__main__":
    test_total_money()