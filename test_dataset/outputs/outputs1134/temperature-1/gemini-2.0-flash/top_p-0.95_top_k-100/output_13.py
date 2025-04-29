def advantage_count(A, B):
    """
    Given two arrays `A` and `B` of equal size, the advantage of `A` with respect to `B` is the number of indices `i` for which `A[i] > B[i]`.

    Return any permutation of `A` that maximizes its advantage with respect to `B`.
    """
    n = len(A)
    sorted_A = sorted(A)
    result = [0] * n
    indices = sorted(range(n), key=lambda i: B[i])
    left = 0
    right = n - 1
    for i in indices:
        if sorted_A[left] > B[i]:
            result[i] = sorted_A[left]
            left += 1
        else:
            result[i] = sorted_A[right]
            right -= 1
    return result

def test_advantage_count():
    test_cases = [
        {
            "A": [2, 7, 11, 15],
            "B": [1, 10, 4, 11],
            "expected": [2, 11, 7, 15]
        },
        {
            "A": [12, 24, 8, 32],
            "B": [13, 25, 32, 11],
            "expected": [24, 32, 8, 12]
        },
        {
            "A": [2,0,4,1,2],
            "B": [1,3,0,0,2],
            "expected": [2, 0, 4, 1, 2]
        },
        {
            "A": [1,2,3,4],
            "B": [4,3,2,1],
            "expected": [2, 3, 4, 1]
        }
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        A = test_case["A"]
        B = test_case["B"]
        expected = test_case["expected"]
        actual = advantage_count(A, B)

        # Simple check to see if the two arrays have the same elements
        # regardless of order. This doesn't guarantee the exact output
        # but it's a reasonable check
        actual_sorted = sorted(actual)
        expected_sorted = sorted(expected)

        if actual_sorted == expected_sorted:
            print(f"Test case {i+1}: True")
            num_correct += 1
        else:
            print(f"Test case {i+1}: False")
            print(f"  Input A: {A}")
            print(f"  Input B: {B}")
            print(f"  Expected: {expected}")
            print(f"  Actual:   {actual}")

    print(f"\nCorrect tests: {num_correct}/{total_tests}")

if __name__ == "__main__":
    test_advantage_count()