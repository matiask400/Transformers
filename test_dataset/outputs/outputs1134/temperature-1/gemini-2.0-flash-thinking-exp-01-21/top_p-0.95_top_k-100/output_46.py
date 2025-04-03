def sort_array_by_parity(A):
    """
    Given an array A of non-negative integers, return an array consisting of all the even elements of A,
    followed by all the odd elements of A.

    You may return any answer array that satisfies this condition.

    Example 1:
    Input: [3,1,2,4]
    Output: [2,4,3,1]
    The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

    Note:
    1 <= A.length <= 5000
    0 <= A[i] <= 5000
    """
    even_elements = []
    odd_elements = []
    for num in A:
        if num % 2 == 0:
            even_elements.append(num)
        else:
            odd_elements.append(num)
    return even_elements + odd_elements

def run_tests():
    test_cases = [
        {
            "input": [3, 1, 2, 4],
            "expected_output": [2, 4, 3, 1]
        },
        {
            "input": [0],
            "expected_output": [0]
        },
        {
            "input": [1],
            "expected_output": [1]
        },
        {
            "input": [2, 1, 4, 3, 6, 5],
            "expected_output": [2, 4, 6, 1, 3, 5]
        },
        {
            "input": [1, 3, 5, 7],
            "expected_output": [1, 3, 5, 7]
        },
        {
            "input": [2, 4, 6, 8],
            "expected_output": [2, 4, 6, 8]
        },
        {
            "input": [],
            "expected_output": []
        },
        {
            "input": [0, 2, 4, 1, 3],
            "expected_output": [0, 2, 4, 1, 3]
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        input_array = test_case["input"]
        expected_output = test_case["expected_output"]
        actual_output = sort_array_by_parity(input_array)

        is_correct = True

        even_actual = [x for x in actual_output if x % 2 == 0]
        odd_actual = [x for x in actual_output if x % 2 != 0]
        even_expected = [x for x in expected_output if x % 2 == 0]
        odd_expected = [x for x in expected_output if x % 2 != 0]

        if even_actual != even_expected:
             is_correct = False
        if odd_actual != odd_expected:
             is_correct = False

        even_actual_prefix = actual_output[:len(even_actual)]
        odd_actual_suffix = actual_output[len(even_actual):]

        if even_actual_prefix != even_actual:
            is_correct = False
        if odd_actual_suffix != odd_actual:
            is_correct = False

        if is_correct:
            print(True)
            correct_tests += 1
        else:
            print(False)
            print(f"Test {i+1} failed:")
            print(f"  Input: {input_array}")
            print(f"  Expected Output: {expected_output}")
            print(f"  Actual Output: {actual_output}")

    print(f"\n{correct_tests}/{total_tests} correct tests")

if __name__ == "__main__":
    run_tests()