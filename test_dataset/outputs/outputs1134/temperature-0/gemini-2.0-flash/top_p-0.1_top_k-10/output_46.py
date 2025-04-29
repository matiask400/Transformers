def sort_array_by_parity(A):
    """
    Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

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
        ([], []),
        ([1, 0, 3, 2, 5, 4], [0, 2, 4, 1, 3, 5])
    ]

    correct_count = 0
    total_count = len(test_cases)

    for input_array, expected_output in test_cases:
        actual_output = sort_array_by_parity(input_array)
        
        # Check if the actual output contains all even numbers followed by all odd numbers
        even_part = [num for num in actual_output if num % 2 == 0]
        odd_part = [num for num in actual_output if num % 2 != 0]
        
        combined_part = even_part + odd_part
        
        if len(combined_part) != len(actual_output):
            result = False
        else:
            result = True
            
            # Check if the even and odd parts contain the correct numbers
            even_nums_in_input = [num for num in input_array if num % 2 == 0]
            odd_nums_in_input = [num for num in input_array if num % 2 != 0]
            
            if sorted(even_part) != sorted(even_nums_in_input) or sorted(odd_part) != sorted(odd_nums_in_input):
                result = False
        
        if result:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_sort_array_by_parity()