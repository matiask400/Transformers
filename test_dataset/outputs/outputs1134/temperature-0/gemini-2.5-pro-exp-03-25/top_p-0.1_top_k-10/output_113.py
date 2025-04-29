import sys
import io

class SparseVector:
    """
    Represents a sparse vector and provides a method for dot product calculation.
    """
    def __init__(self, nums: list[int]):
        """
        Initializes the SparseVector object.
        Stores non-zero elements and their indices efficiently.
        """
        self.non_zeros = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.non_zeros[i] = num

    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        Computes the dot product between this SparseVector and another SparseVector.

        Args:
            vec: Another SparseVector object.

        Returns:
            The dot product of the two vectors.
        """
        dot_product_sum = 0
        
        # Iterate through the non-zero elements of the smaller dictionary 
        # for potentially better performance.
        if len(self.non_zeros) < len(vec.non_zeros):
            smaller_dict = self.non_zeros
            larger_dict = vec.non_zeros
        else:
            smaller_dict = vec.non_zeros
            larger_dict = self.non_zeros
            
        for index, value1 in smaller_dict.items():
            # Check if the index also exists in the other vector's non-zero elements
            if index in larger_dict:
                value2 = larger_dict[index]
                dot_product_sum += value1 * value2
                
        return dot_product_sum

# --- Testing Framework ---

def run_tests():
    """
    Runs predefined test cases against the SparseVector implementation.
    """
    test_cases = [
        ([1, 0, 0, 2, 3], [0, 3, 0, 4, 0], 8),
        ([0, 1, 0, 0, 0], [0, 0, 0, 0, 2], 0),
        ([0, 1, 0, 0, 2, 0, 0], [1, 0, 0, 0, 3, 0, 4], 6),
        ([1, 0, 0, 0, 0], [0, 0, 0, 0, 1], 0),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1], 5),
        ([0, 0, 0, 0, 0], [1, 2, 3, 4, 5], 0),
        ([1, 2, 3, 4, 5], [0, 0, 0, 0, 0], 0),
        ([100] * (10**5), [1] * (10**5), 100 * (10**5)), # Test large dense vectors
        ([0] * (10**5 - 1) + [100], [1] + [0] * (10**5 - 1), 0), # Test large sparse vectors
        ([1] + [0] * (10**5 - 1), [1] + [0] * (10**5 - 1), 1), # Test large sparse vectors (match)
    ]

    correct_count = 0
    total_tests = len(test_cases)

    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    for i, (nums1, nums2, expected) in enumerate(test_cases):
        try:
            v1 = SparseVector(nums1)
            v2 = SparseVector(nums2)
            result = v1.dotProduct(v2)
            passed = (result == expected)
            print(passed) # Print True or False for each test
            if passed:
                correct_count += 1
        except Exception as e:
            print(f"Test case {i+1} failed with error: {e}")
            print(False)

    # Restore stdout
    sys.stdout = old_stdout
    # Print captured output
    print(captured_output.getvalue(), end="")

    # Print summary
    print(f"{correct_count}/{total_tests}")

if __name__ == "__main__":
    run_tests()

# --- Follow-up Discussion ---
# What if only one of the vectors is sparse?
#
# The current implementation using dictionaries (hash maps) is already quite efficient
# even if one vector is dense (many non-zero elements) and the other is sparse.
#
# Let's analyze the `dotProduct` method:
# 1. It identifies the dictionary with fewer non-zero entries (`smaller_dict`).
# 2. It iterates through the indices and values (`index`, `value1`) of this `smaller_dict`.
# 3. For each `index`, it performs a lookup (`index in larger_dict`) in the other dictionary (`larger_dict`). This lookup is O(1) on average for hash maps.
# 4. If the index exists, it multiplies the values and adds to the sum.
#
# If `self` is sparse and `vec` is dense:
# - `self.non_zeros` will be small.
# - `vec.non_zeros` will be large (potentially containing almost all indices).
# - The loop will iterate `k` times, where `k` is the number of non-zero elements in `self`.
# - Each iteration involves an O(1) average time lookup in `vec.non_zeros`.
# - The total time complexity is roughly O(k), which is efficient because `k` is small for a sparse vector.
#
# If `self` is dense and `vec` is sparse:
# - `self.non_zeros` will be large.
# - `vec.non_zeros` will be small.
# - The loop will iterate `m` times, where `m` is the number of non-zero elements in `vec`.
# - Each iteration involves an O(1) average time lookup in `self.non_zeros`.
# - The total time complexity is roughly O(m), which is efficient because `m` is small for a sparse vector.
#
# Therefore, the current implementation efficiently handles the case where one or both vectors are sparse by iterating only over the non-zero elements of the *sparser* vector. No significant changes are strictly necessary for this follow-up scenario if the input `vec` is guaranteed to also be a `SparseVector` object.
#
# If the input `vec` could be a standard Python list (representing a potentially dense vector) instead of a `SparseVector` object, we might add a check or overload the method:
#
#