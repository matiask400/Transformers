def magicalString(n):
    """
    Calculates the number of '1's in the first N elements of the magical string S.

    Args:
        n (int): The number of elements to consider in the magical string.

    Returns:
        int: The number of '1's in the first N elements of the magical string.
    """

    if n == 0:
        return 0

    s = [1, 2, 2]
    i = 2
    j = 3

    while j < n:
        if s[i] == 1:
            s.append(3 - s[-1])
            j += 1
        else:
            s.append(3 - s[-1])
            if j < n:
                s.append(3 - s[-1])
            j += 2
        i += 1

    count = 0
    for k in range(n):
        if s[k] == 1:
            count += 1

    return count


def test_magicalString():
    """
    Tests the magicalString function with various inputs and expected outputs.
    """

    test_cases = [
        (6, 3),
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 2),
        (7, 4),
        (8, 4),
        (9, 4),
        (10, 5)
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, (input_n, expected_output) in enumerate(test_cases):
        actual_output = magicalString(input_n)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False (Input: {input_n}, Expected: {expected_output}, Actual: {actual_output})")

    print(f"\nCorrect tests: {correct_tests}/{total_tests}")


if __name__ == "__main__":
    test_magicalString()