def sort_array_by_parity(A):
    """
    Given an array A of non-negative integers, return an array consisting of all the even elements of A,
    followed by all the odd elements of A.

    You may return any answer array that satisfies this condition.

    Example 1:
    Input: [3,1,2,4]
    Output: [2,4,3,1]

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
            "input": [2, 4, 6],
            "expected_output": [2, 4, 6]
        },
        {
            "input": [1, 3, 5],
            "expected_output": [1, 3, 5]
        },
        {
            "input": [],
            "expected_output": []
        },
        {
            "input": [0, 1, 2, 3, 4, 5],
            "expected_output": [0, 2, 4, 1, 3, 5]
        },
        {
            "input": [5, 4, 3, 2, 1, 0],
            "expected_output": [4, 2, 0, 5, 3, 1]
        },
        {
            "input": [2,1,2,1,2,1],
            "expected_output": [2,2,2,1,1,1]
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
        if len(actual_output) != len(input_array):
            is_correct = False
        if set(actual_output) != set(input_array):
            is_correct = False
        if not all(actual_output.index(x) < actual_output.index(y) for x in even_actual for y in odd_actual if x in actual_output and y in actual_output):
            is_correct = False


        if is_correct:
            print('True')
            correct_tests += 1
        else:
            print('False')

    print(f"{correct_tests}/{total_tests}")

if __name__ == "__main__":
    run_tests()