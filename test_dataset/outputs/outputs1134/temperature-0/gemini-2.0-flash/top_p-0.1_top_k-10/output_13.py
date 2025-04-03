def advantage_count(A, B):
    """
    Given two arrays `A` and `B` of equal size, the advantage of `A` with respect to `B` is the number of indices `i` for which `A[i] > B[i]`.

    Return any permutation of `A` that maximizes its advantage with respect to `B`.
    """
    n = len(A)
    sorted_A = sorted(A)
    idx_B = sorted(range(n), key=lambda i: B[i])
    result = [0] * n
    left = 0
    right = n - 1
    for i in idx_B:
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
            "input": {
                "A": [2, 7, 11, 15],
                "B": [1, 10, 4, 11]
            },
            "expected": [2, 11, 7, 15]
        },
        {
            "input": {
                "A": [12, 24, 8, 32],
                "B": [13, 25, 32, 11]
            },
            "expected": [24, 32, 8, 12]
        },
        {
            "input": {
                "A": [2,0,4,1,2],
                "B": [1,3,0,0,2]
            },
            "expected": [2, 2, 1, 0, 4]
        },
        {
            "input": {
                "A": [1,2,3,4],
                "B": [4,3,2,1]
            },
            "expected": [2, 3, 4, 1]
        },
        {
            "input": {
                "A": [1,2,3,4],
                "B": [1,2,3,4]
            },
            "expected": [2, 3, 4, 1]
        }
    ]

    num_correct = 0
    for i, test_case in enumerate(test_cases):
        A = test_case["input"]["A"]
        B = test_case["input"]["B"]
        expected = test_case["expected"]
        actual = advantage_count(A, B)

        advantage_actual = sum(1 for j in range(len(A)) if actual[j] > B[j])
        advantage_expected = sum(1 for j in range(len(A)) if expected[j] > B[j])

        if advantage_actual >= advantage_expected:
            print("True")
            num_correct += 1
        else:
            print("False")

    print(f"{num_correct}/{len(test_cases)}")

if __name__ == "__main__":
    test_advantage_count()