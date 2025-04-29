import sys
import io
from collections import defaultdict

def subarraySum(nums: list[int], k: int) -> int:
    """
    Given an array of integers nums and an integer k, return the total 
    number of continuous subarrays whose sum equals to k.

    Args:
        nums: A list of integers.
        k: The target sum.

    Returns:
        The total number of continuous subarrays summing to k.
    """
    count = 0
    current_sum = 0
    # Use a hash map (dictionary in Python) to store the frequency of prefix sums.
    # The key is the prefix sum, and the value is its frequency.
    # Initialize with prefix sum 0 having a frequency of 1 to handle subarrays
    # that start from the beginning of the array.
    prefix_sum_counts = defaultdict(int)
    prefix_sum_counts[0] = 1

    for num in nums:
        current_sum += num
        
        # We are looking for a previous prefix sum `prev_sum` such that:
        # current_sum - prev_sum = k
        # Rearranging, we get:
        # prev_sum = current_sum - k
        # If `current_sum - k` exists in our map, it means there are subarrays
        # ending at the current position whose sum is k. The number of such
        # subarrays is equal to the frequency of that `prev_sum`.
        if (current_sum - k) in prefix_sum_counts:
            count += prefix_sum_counts[current_sum - k]
            
        # Update the frequency of the current prefix sum in the map.
        prefix_sum_counts[current_sum] += 1
        
    return count

# --- Testing Framework ---

def run_tests():
    test_cases = [
        # Example 1
        {'input': {'nums': [1, 1, 1], 'k': 2}, 'expected': 2},
        # Example 2
        {'input': {'nums': [1, 2, 3], 'k': 3}, 'expected': 2},
        # Additional Test Cases
        {'input': {'nums': [1], 'k': 1}, 'expected': 1},
        {'input': {'nums': [1], 'k': 0}, 'expected': 0},
        {'input': {'nums': [1, -1, 5, -2, 3], 'k': 3}, 'expected': 4}, # [1,-1,5,-2], [5,-2], [3], [-1, 5, -2, 3] -> No, [-1,5,-2,3] is not 3. [1,-1,5,-2] = 3, [5,-2] = 3, [3]=3. Let's recheck: sums=[1, 0, 5, 3, 6]. map={0:1}. n=1: cur=1. check 1-3=-2. map={0:1, 1:1}. n=-1: cur=0. check 0-3=-3. map={0:2, 1:1}. n=5: cur=5. check 5-3=2. map={0:2, 1:1, 5:1}. n=-2: cur=3. check 3-3=0. count+=map[0]=2. map={0:2, 1:1, 5:1, 3:1}. n=3: cur=6. check 6-3=3. count+=map[3]=1. count=3. map={0:2, 1:1, 5:1, 3:1, 6:1}. Final count = 3. Subarrays: [1, -1, 5, -2], [5, -2], [3]. Let's trace again.
        # nums = [1, -1, 5, -2, 3], k = 3
        # count=0, current_sum=0, map={0:1}
        # num=1:  cur=1. check cur-k = 1-3=-2. map[-2]? No. map={0:1, 1:1}
        # num=-1: cur=0. check cur-k = 0-3=-3. map[-3]? No. map={0:2, 1:1}
        # num=5:  cur=5. check cur-k = 5-3=2.  map[2]? No.  map={0:2, 1:1, 5:1}
        # num=-2: cur=3. check cur-k = 3-3=0.  map[0]? Yes=2. count=0+2=2. map={0:2, 1:1, 5:1, 3:1}  (Found subarrays ending here: [1,-1,5,-2] sum=3; [5,-2] sum=3)
        # num=3:  cur=6. check cur-k = 6-3=3.  map[3]? Yes=1. count=2+1=3. map={0:2, 1:1, 5:1, 3:1, 6:1}  (Found subarray ending here: [3] sum=3)
        # Final count = 3. Expected should be 3, not 4.
        {'input': {'nums': [1, -1, 5, -2, 3], 'k': 3}, 'expected': 3},
        {'input': {'nums': [28, 54, 7, -70, 22, 65, -6], 'k': 100}, 'expected': 1}, # [28, 54, 7, -70, 22, 65, -6] -> Subarray [28, 54, 7, -70, 22, 65, -6]? No. sum(28..-6)=100. Subarray [28, 54, 7, -70, 22, 65] = 106. Subarray [54, 7, -70, 22, 65, -6] = 72. Subarray [28, 54, 7]=89. [7, -70, 22, 65, -6] = 18. [22, 65, -6] = 81. [65,-6] = 59. [28, 54, 7, -70, 22, 65, -6]. Sums: 28, 82, 89, 19, 41, 106, 100. map={0:1}. n=28: cur=28. check 28-100=-72. map={0:1, 28:1}. n=54: cur=82. check 82-100=-18. map={0:1, 28:1, 82:1}. n=7: cur=89. check 89-100=-11. map={0:1, 28:1, 82:1, 89:1}. n=-70: cur=19. check 19-100=-81. map={0:1, 28:1, 82:1, 89:1, 19:1}. n=22: cur=41. check 41-100=-59. map={0:1, ..., 19:1, 41:1}. n=65: cur=106. check 106-100=6. map={0:1, ..., 41:1, 106:1}. n=-6: cur=100. check 100-100=0. map[0]? Yes=1. count=0+1=1. map={0:1, ..., 106:1, 100:1}. Final count=1. Correct. The subarray is the entire array itself.
        {'input': {'nums': [0, 0, 0, 0, 0], 'k': 0}, 'expected': 15}, # Subarrays: [0] (5 times), [0,0] (4 times), [0,0,0] (3 times), [0,0,0,0] (2 times), [0,0,0,0,0] (1 time). 5+4+3+2+1 = 15.
        # sums: 0, 0, 0, 0, 0. map={0:1}
        # n=0: cur=0. check 0-0=0. map[0]=1. count=1. map={0:2}.
        # n=0: cur=0. check 0-0=0. map[0]=2. count=1+2=3. map={0:3}.
        # n=0: cur=0. check 0-0=0. map[0]=3. count=3+3=6. map={0:4}.
        # n=0: cur=0. check 0-0=0. map[0]=4. count=6+4=10. map={0:5}.
        # n=0: cur=0. check 0-0=0. map[0]=5. count=10+5=15. map={0:6}.
        # Final count = 15. Correct.
        {'input': {'nums': [-1, -1, 1], 'k': 0}, 'expected': 1}, # Subarray [-1, 1]
        # sums: -1, -2, -1. map={0:1}
        # n=-1: cur=-1. check -1-0=-1. map[-1]? No. map={0:1, -1:1}
        # n=-1: cur=-2. check -2-0=-2. map[-2]? No. map={0:1, -1:1, -2:1}
        # n= 1: cur=-1. check -1-0=-1. map[-1]? Yes=1. count=0+1=1. map={0:1, -1:2, -2:1}
        # Final count = 1. Correct.
        {'input': {'nums': [1, 2, 1, 2, 1], 'k': 3}, 'expected': 4}, # [1,2], [2,1], [1,2], [2,1]
        # sums: 1, 3, 4, 6, 7. map={0:1}
        # n=1: cur=1. check 1-3=-2. map={0:1, 1:1}
        # n=2: cur=3. check 3-3=0. map[0]=1. count=1. map={0:1, 1:1, 3:1}
        # n=1: cur=4. check 4-3=1. map[1]=1. count=1+1=2. map={0:1, 1:1, 3:1, 4:1}
        # n=2: cur=6. check 6-3=3. map[3]=1. count=2+1=3. map={0:1, 1:1, 3:1, 4:1, 6:1}
        # n=1: cur=7. check 7-3=4. map[4]=1. count=3+1=4. map={0:1, 1:1, 3:1, 4:1, 6:1, 7:1}
        # Final count = 4. Correct.
    ]

    correct_count = 0
    total_tests = len(test_cases)

    # Capture stdout
    old_stdout = sys.stdout
    
    for i, test in enumerate(test_cases):
        sys.stdout = io.StringIO() # Redirect stdout to suppress function print
        
        nums_input = test['input']['nums']
        k_input = test['input']['k']
        expected_output = test['expected']
        
        # Make a copy if the function modifies the input list, though this one doesn't
        # nums_copy = list(nums_input) 
        
        try:
            actual_output = subarraySum(nums_input, k_input)
            result = actual_output == expected_output
            correct_count += result
        except Exception as e:
            result = False
            print(f"Test Case {i+1} raised an exception: {e}") # Print exception to captured output

        captured_output = sys.stdout.getvalue() # Get captured print output
        sys.stdout = old_stdout # Restore stdout

        print(f"{result}") # Print True/False for the test outcome
        # Optionally print more details on failure
        # if not result:
        #    print(f"  Input: nums={nums_input}, k={k_input}")
        #    print(f"  Expected: {expected_output}")
        #    print(f"  Actual: {actual_output}")
        # if captured_output:
        #    print(f"  Function printed: {captured_output.strip()}")


    print(f"{correct_count}/{total_tests}")

# Execute the tests
if __name__ == "__main__":
    run_tests()