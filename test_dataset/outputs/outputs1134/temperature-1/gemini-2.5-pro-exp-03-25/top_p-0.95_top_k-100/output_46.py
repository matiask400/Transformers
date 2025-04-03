import sys
import io
from collections import Counter # Used for robust validation if needed

def solve():
    """
    Implements the solution function and the testing framework.
    """

    # --- Solution Function ---
    def sortArrayByParity(A):
        """
        Rearranges the array A such that all even elements appear before all odd elements.

        Args:
            A: A list of non-negative integers.

        Returns:
            A list with even elements followed by odd elements.
            This implementation uses an in-place two-pointer approach.
        """
        if not A:
            return []

        write_ptr = 0 # Points to the next position where an even number should be placed
        for read_ptr in range(len(A)):
            # If the current element is even
            if A[read_ptr] % 2 == 0:
                # Swap it with the element at write_ptr
                A[read_ptr], A[write_ptr] = A[write_ptr], A[read_ptr]
                # Move the write_ptr forward
                write_ptr += 1
        return A

    # --- Validation Helper ---
    def validate_output(original_input, output_array):
        """
        Validates if the output_array meets the condition: evens first, then odds.
        Also checks if the elements are preserved.

        Args:
            original_input: The original input list.
            output_array: The list returned by the solution function.

        Returns:
            True if the output is valid, False otherwise.
        """
        if len(original_input) != len(output_array):
            print(f"Validation failed: Length mismatch. Input: {len(original_input)}, Output: {len(output_array)}")
            return False

        # Check element preservation (optional but good practice)
        # Using Counter is robust for checking multiset equality
        if Counter(original_input) != Counter(output_array):
             print(f"Validation failed: Element mismatch. Input Counter: {Counter(original_input)}, Output Counter: {Counter(output_array)}")
             return False

        # Check the even/odd ordering property
        first_odd_index = -1
        for i, num in enumerate(output_array):
            if num % 2 != 0:  # Found the first odd number
                first_odd_index = i
                break

        # If no odd numbers were found (first_odd_index remains -1),
        # all numbers must be even. Check this.
        if first_odd_index == -1:
            for num in output_array:
                if num % 2 != 0:
                    print(f"Validation failed: Found odd number {num} when all should be even.")
                    return False
            return True # All are even, which is valid

        # If odd numbers were found, check the partitions
        # 1. Check the 'even' partition (before first_odd_index)
        for i in range(first_odd_index):
            if output_array[i] % 2 != 0:
                print(f"Validation failed: Found odd number {output_array[i]} at index {i} in the 'even' partition.")
                return False

        # 2. Check the 'odd' partition (from first_odd_index onwards)
        for i in range(first_odd_index, len(output_array)):
            if output_array[i] % 2 == 0:
                 print(f"Validation failed: Found even number {output_array[i]} at index {i} in the 'odd' partition.")
                 return False

        return True # Ordering property holds


    # --- Test Cases ---
    test_cases = [
        {"input": [3, 1, 2, 4], "id": "Example 1"},
        {"input": [0], "id": "Single zero"},
        {"input": [1], "id": "Single one"},
        {"input": [2, 4, 6, 8], "id": "All even"},
        {"input": [1, 3, 5, 7], "id": "All odd"},
        {"input": [0, 1, 0, 1, 0], "id": "Zeros and ones"},
        {"input": [2, 3, 1, 4, 5, 6], "id": "Mixed 1"},
        {"input": [1, 2, 3, 4, 5, 6], "id": "Alternating"},
        {"input": [], "id": "Empty list"},
        {"input": [5000, 4999, 0, 1], "id": "Max/Min values"},
    ]

    correct_count = 0
    total_tests = len(test_cases)

    # --- Running Tests ---
    for i, test in enumerate(test_cases):
        input_list = test["input"]
        # Create a copy to avoid modifying the original test case input list
        input_copy = list(input_list)
        test_id = test["id"]

        # Capture output
        old_stdout = sys.stdout
        redirected_output = io.StringIO()
        sys.stdout = redirected_output

        # Run the solution function
        try:
            # Run the user's function
            actual_output = sortArrayByParity(input_copy) # Pass the copy

            # Restore stdout
            sys.stdout = old_stdout

            # Validate the result
            is_correct = validate_output(input_list, actual_output) # Validate against original

        except Exception as e:
            # Restore stdout in case of error
            sys.stdout = old_stdout
            print(f"Test {i+1} ({test_id}): Runtime Error - {e}")
            is_correct = False

        print(f"Test {i+1} ({test_id}): {is_correct}")
        if is_correct:
            correct_count += 1

    # --- Final Summary ---
    print(f"\nResult: {correct_count} / {total_tests} tests passed.")

# Execute the testing framework
solve()