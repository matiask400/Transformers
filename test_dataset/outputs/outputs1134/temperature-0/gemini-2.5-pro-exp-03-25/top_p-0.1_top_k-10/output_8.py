import copy
import sys
import io

def moveZeroes(nums: list[int]) -> None:
    """
    Moves all 0's to the end of the list in-place, maintaining the
    relative order of the non-zero elements. Uses the swap-based
    two-pointer approach to minimize operations (swaps).

    Args:
        nums: The list of integers to modify. Modifies the list in-place.
              Does not return anything.
    """
    write_ptr = 0  # Points to the next position to place a non-zero element
    n = len(nums)

    # Iterate through the list with a read pointer
    for read_ptr in range(n):
        # If the current element is non-zero
        if nums[read_ptr] != 0:
            # If the non-zero element is not already in its correct final position
            # (i.e., read_ptr is ahead of write_ptr), swap it.
            # If read_ptr == write_ptr, the non-zero element is already
            # in its correct relative place, so no swap is needed, but
            # we still need to advance write_ptr.
            if read_ptr != write_ptr:
                # Swap the non-zero element found at read_ptr
                # with the element currently at write_ptr (which must be a zero
                # or a non-zero element that hasn't been processed yet but is
                # behind its final position)
                nums[read_ptr], nums[write_ptr] = nums[write_ptr], nums[read_ptr]
            
            # Increment write_ptr because we have placed a non-zero element
            # correctly at the 'write_ptr' index (either by swapping or because
            # it was already there).
            write_ptr += 1
    
    # After the loop, all non-zero elements are at indices 0 to write_ptr-1
    # in their original relative order, and all zeros are at indices
    # write_ptr to n-1. No explicit filling of zeros is needed with the swap method.


def solve():
    """
    Defines test cases, runs the moveZeroes function on copies of the inputs,
    compares the results with expected outputs, and prints the test outcomes.
    """
    tests = [
        # Input nums, Expected output nums
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1], [1]),
        ([1,