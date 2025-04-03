import copy
from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    Rotates the image by 90 degrees (clockwise) in-place.

    The rotation can be achieved by first transposing the matrix
    and then reversing each row.
    """
    n = len(matrix)
    if n <= 1:
        return # No rotation needed for 0x0 or 1x1

    # 1. Transpose the matrix (swap elements across the main diagonal)
    # Iterate through the upper triangle (including the diagonal)
    for i in range(n):
        # Only need to iterate j from i to n-1.
        # More precisely, j from i+1 to n-1 to avoid swapping diagonal elements
        # with themselves and swapping other elements twice.
        for j in range(i + 1, n):
            # Swap matrix[i][j] and matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 2. Reverse each row
    for i in range(n):
        # Use two pointers to reverse the row in-place
        left, right = 0, n - 1
        while left < right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1
        # Alternatively, use list's built-in reverse method:
        # matrix[i].reverse()


# --- Testing Framework ---

def run_tests():
    """
    Runs test cases against the rotate function.
    """
    test_cases = [
        # Input matrix, Expected output matrix
        ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
        ([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]),
        ([[1]], [[1]]),
        ([[1,2],[3,4]], [[3,1],[4,2]]),
        # Additional test case: 4x4 matrix
        ([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]),
        # Additional test case: 5x5 matrix (odd dimension)
        ([[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11,12,13,14,15],
          [16,17,18,19,20],
          [21,22,23,24,25]],
         [[21,16,11, 6, 1],
          [22,17,12, 7, 2],
          [23,18,13, 8, 3],
          [24,19,14, 9, 4],
          [25,20,15,10, 5]])
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (input_matrix, expected_output) in enumerate(test_cases):
        # Create a deep copy of the input matrix for the function to modify
        matrix_to_rotate = copy.deepcopy(input_matrix)

        # Call the rotate function (modifies matrix_to_rotate in-place)
        rotate(matrix_to_rotate)

        # Compare the modified matrix with the expected output
        if matrix_to_rotate == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
            # Optional: Print details on failure
            # print(f"  Input:    {input_matrix}")
            # print(f"  Expected: {expected_output}")
            # print(f"  Got:      {matrix_to_rotate}")

    print(f"{correct_count}/{total_tests} tests passed.")

# Run the tests
if __name__ == "__main__":
    run_tests()