import sys
import io
from typing import List

def solve():
    """
    Implements the moveZeroes function and the testing framework.
    """

    def moveZeroes(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Moves all 0's to the end of the array in-place, maintaining the
        relative order of the non-zero elements. Uses a two-pointer approach.

        Args:
            nums: The list of integers to modify.
        """
        n = len(nums)
        # write_ptr points to the position where the next non-zero element should be placed.
        write_ptr = 0

        # Iterate through the array with read_ptr
        for read_ptr in range(n):
            # If the element at read_ptr is non-zero
            if nums[read_ptr] != 0:
                # If read_ptr is ahead of write_ptr, it means we found a non-zero
                # element after some zeros (or at the beginning). We need to move
                # this non-zero element to the write_ptr position.
                # We swap the elements at read_ptr and write_ptr.
                # If read_ptr and write_ptr are the same (e.g., at the beginning
                # of the array with non-zero elements), swapping does nothing,
                # which is correct.
                if read_ptr != write_ptr:
                     nums[write_ptr], nums[read_ptr] = nums[read_ptr], nums[write_ptr]
                # Increment write_ptr to point to the next position for a non-zero element.
                write_ptr += 1
        
        # After the loop, all non-zero elements are moved to the beginning
        # (up to write_ptr - 1) in their original relative order, and the
        # remaining elements from write_ptr to the end are implicitly the zeros
        # that were swapped back or were already there. No need for a second pass
        # to fill with zeros when using the swap method.


    # --- Testing Framework ---
    test_cases = [
        # Input nums, Expected output nums (after modification)
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1], [1]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([0, 0, 0, 0], [0, 0, 0, 0]),
        ([1, 0, 2, 0, 3], [1, 2, 3, 0, 0]),
        ([0, 0, 1], [1, 0, 0]),
        ([4, 2, 4, 0, 0, 3, 0, 5, 1, 0], [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]),
        ([-1, 0, 0, 3, -5, 0], [-1, 3, -5, 0, 0, 0]),
        ([2, 1], [2, 1]), # Test case from LeetCode discussion
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (input_nums, expected_output) in enumerate(test_cases):
        # Create a copy for the function to modify in-place
        # This ensures original test case input is preserved for reporting
        nums_copy = list(input_nums)
        
        # Capture standard output to prevent the function from printing anything
        # (if it were designed to print) during the test run.
        original_stdout = sys.stdout
        sys.stdout = io.StringIO()
        
        try:
            # Call the function which modifies nums_copy in-place
            moveZeroes(nums_copy)
            # The result *is* the modified nums_copy
            actual_output = nums_copy
        except Exception as e:
            # Restore stdout immediately in case of error
            sys.stdout = original_stdout
            print(f"Test {i+1}: Error - {e}")
            # Mark test as failed
            print(f"  Input: {input_nums}")
            continue # Skip comparison for this test case
        finally:
            # Restore standard output
            captured_output = sys.stdout.getvalue() # Although moveZeroes shouldn't print
            sys.stdout = original_stdout

        # Compare the modified list with the expected output
        if actual_output == expected_output:
            print(f"True") # Print True for passed test
            correct_count += 1
        else:
            print(f"False") # Print False for failed test
            # Optionally print details for failed tests
            # print(f"  Input: {input_nums}")
            # print(f"  Expected: {expected_output}")
            # print(f"  Actual: {actual_output}")
            # if captured_output:
            #      print(f"  Captured Output:\n{captured_output}")


    # Print the final summary line
    print(f"{correct_count}/{total_tests}")

# Execute the solve function that includes the tests
solve()