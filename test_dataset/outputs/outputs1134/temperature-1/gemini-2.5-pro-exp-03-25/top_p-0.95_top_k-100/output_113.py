import sys
import io

# Define the SparseVector class
class SparseVector:
    """
    Initializes the object with the vector nums.
    Stores the vector efficiently by only keeping track of non-zero elements and their indices.
    Uses a dictionary where keys are indices and values are the non-zero numbers.
    
    Args:
        nums (list[int]): The input vector.
    """
    def __init__(self, nums: list[int]):
        self.non_zeros = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.non_zeros[i] = num

    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        Compute the dot product between the instance of SparseVector and vec.
        It efficiently calculates the dot product by only considering non-zero elements.
        It iterates through the non-zero elements of the sparser vector (the one with fewer
        non-zero entries) and checks for matching indices in the other vector's non-zero map.

        Args:
            vec (SparseVector): The other SparseVector object to compute the dot product with.

        Returns:
            int: The dot product of the two sparse vectors.
        """
        result = 0
        
        # Optimization: Iterate over the dictionary with fewer non-zero elements.
        # This reduces the number of lookups needed.
        if len(self.non_zeros) < len(vec.non_zeros):
            # Iterate through self's non-zeros and lookup in vec's non-zeros
            for index, value in self.non_zeros.items():
                if index in vec.non_zeros:
                    result += value * vec.non_zeros[index]
        else:
            # Iterate through vec's non-zeros and lookup in self's non-zeros
            for index, value in vec.non_zeros.items():
                if index in self.non_zeros:
                    # Note: value is from vec, self.non_zeros[index] is from self
                    result += value * self.non_zeros[index] 
                    
        return result

    # Follow-up: What if only one of the vectors is sparse?
    # The current implementation using SparseVector class for both vectors handles 
    # this scenario well. If one vector is dense, its `non_zeros` dictionary 
    # would simply have more entries. The optimization to iterate over the smaller 
    # dictionary ensures efficiency by iterating over the truly sparse vector's elements.
    #
    # If the non-sparse vector was represented as a standard Python list (e.g., `dense_vec`),
    # a separate method could be written for clarity, or the `dotProduct` could check
    # the type of `vec`. An example method for dot product with a dense list:
    #
    # def dotProductWithDense(self, dense_vec: list[int]) -> int:
    #      result = 0
    #      # Iterate only through the non-zero elements of the sparse vector (self)
    #      for index, value in self.non_zeros.items():
    #          # Check bounds, although problem implies lengths match
    #          if index < len(dense_vec): 
    #              # Multiply sparse value with corresponding dense value
    #              result += value * dense_vec[index] 
    #      return result
    #
    # This approach ensures complexity depends on the number of non-zeros in the 
    # sparse vector, not the total length N, which is efficient.


# --- Testing Framework ---

def run_tests(test_cases):
    """
    Runs a series of test cases against the SparseVector class.
    Instantiates SparseVector objects, calls the dotProduct method,
    compares the output with the expected output, and prints results.

    Args:
        test_cases (list[dict]): A list of test cases, where each case is a 
                                 dictionary containing 'input' (nums1, nums2) 
                                 and 'expected' output.
    """
    correct_count = 0
    total_count = len(test_cases)
    
    for i, test_data in enumerate(test_cases):
        nums1 = test_data["input"]["nums1"]
        nums2 = test_data["input"]["nums2"]
        expected = test_data["expected"]
        
        try:
            # Instantiate SparseVectors
            v1 = SparseVector(nums1)
            v2 = SparseVector(nums2)
            
            # Compute dot product
            actual = v1.dotProduct(v2)
            
            # Compare and print result for the test case
            if actual == expected:
                print(f"True")
                correct_count += 1
            else:
                print(f"False")
                # Optional: uncomment to print details on failure
                # print(f"  Test Case {i+1} Failed:")
                # print(f"  Input nums1: {nums1}")
                # print(f"  Input nums2: {nums2}")
                # print(f"  Expected: {expected}")
                # print(f"  Actual: {actual}")
        except Exception as e:
            print(f"False") # Indicate failure if an error occurs during test
            print(f"  Error during Test Case {i+1}: {e}")


    # Print final summary
    print(f"{correct_count} / {total_count}")

# --- Main Execution Block ---

if __name__ == "__main__":
    # Define test cases based on examples and potential edge cases
    test_cases = [
        {
            "input": {"nums1": [1, 0, 0, 2, 3], "nums2": [0, 3, 0, 4, 0]},
            "expected": 8,
            "name": "Example 1"
        },
        {
            "input": {"nums1": [0, 1, 0, 0, 0], "nums2": [0, 0, 0, 0, 2]},
            "expected": 0,
            "name": "Example 2"
        },
        {
            "input": {"nums1": [0, 1, 0, 0, 2, 0, 0], "nums2": [1, 0, 0, 0, 3, 0, 4]},
            "expected": 6,
            "name": "Example 3"
        },
        {
            "input": {"nums1": [0, 0, 0], "nums2": [0, 0, 0]},
            "expected": 0,
            "name": "All Zeros"
        },
        {
            "input": {"nums1": [1, 1, 1], "nums2": [1, 1, 1]},
            "expected": 3,
            "name": "All Ones (Dense)" # Still works correctly
        },
        {
            "input": {"nums1": [100] * 10, "nums2": [1] * 10},
            "expected": 1000,
            "name": "Dense Max/Min Values"
        },
         {
            "input": {"nums1": [1] + [0]*1000, "nums2": [1] + [0]*1000},
            "expected": 1,
            "name": "Very Sparse Beginning (Large N)" # Check efficiency
        },
        {
            "input": {"nums1": [0]*1000 + [1], "nums2": [0]*1000 + [1]},
            "expected": 1,
            "name": "Very Sparse End (Large N)"
        },
         {
            "input": {"nums1": [0]*500 + [2] + [0]*500, "nums2": [0]*500 + [3] + [0]*500},
            "expected": 6,
            "name": "Very Sparse Middle (Large N)"
        },
        {
            "input": {"nums1": [1, 0, 1, 0, 1], "nums2": [0, 1, 0, 1, 0]},
            "expected": 0,
            "name": "No Overlapping Non-Zeros"
        },
        {
             "input": {"nums1": [1,0,0,0,0], "nums2": [1,1,1,1,1]},
             "expected": 1,
             "name": "One Very Sparse, One Dense" 
        },
        {
             "input": {"nums1": [1,1,1,1,1], "nums2": [0,0,0,0,1]},
             "expected": 1,
             "name": "One Dense, One Very Sparse" 
        }
    ]
    
    # Run the tests
    run_tests(test_cases)