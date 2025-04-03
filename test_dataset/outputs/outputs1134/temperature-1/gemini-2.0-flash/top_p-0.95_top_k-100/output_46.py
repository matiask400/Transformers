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

def test_sort_array_by_parity():
    test_cases = [
        ([3, 1, 2, 4], [2, 4, 3, 1]),
        ([0, 1, 2], [0, 2, 1]),
        ([1, 3, 5], [1, 3, 5]),
        ([2, 4, 6], [2, 4, 6]),
        ([0], [0]),
        ([1], [1]),
        ([2,1], [2,1]),
        ([1,2], [2,1])
    ]

    correct_count = 0
    total_count = len(test_cases)

    for input_array, expected_output in test_cases:
        actual_output = sort_array_by_parity(input_array)
        
        # Custom comparison to handle different possible outputs
        even_actual = [x for x in actual_output if x % 2 == 0]
        odd_actual = [x for x in actual_output if x % 2 != 0]

        even_expected = [x for x in expected_output if x % 2 == 0]
        odd_expected = [x for x in expected_output if x % 2 != 0]
        
        if even_actual == even_expected and odd_actual == odd_expected and len(even_actual) + len(odd_actual) == len(input_array):
            print("True")
            correct_count += 1
        else:
            print("False")
            
    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_sort_array_by_parity()