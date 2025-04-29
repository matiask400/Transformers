def numSubarraysWithSum(A, S):
    """
    In an array A of 0s and 1s, how many non-empty subarrays have sum S?

    Example 1:
    Input: A = [1,0,1,0,1], S = 2
    Output: 4
    Explanation: 
    The 4 subarrays are bolded below:
    [1,0,1,0,1]
    [1,0,1,0,1]
    [1,0,1,0,1]
    [1,0,1,0,1]
    Note:
    A.length <= 30000
    0 <= S <= A.length
    A[i] is either 0 or 1.
    """
    n = len(A)
    count = 0
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += A[j]
            if current_sum == S:
                count += 1
    return count

def test_numSubarraysWithSum():
    test_cases = [
        ([1,0,1,0,1], 2, 4),
        ([0,0,0,0,0], 0, 15),
        ([0,0,1,0,0,0], 0, 10),
        ([1,0,1,0,1], 3, 1),
        ([1,0,0,0,0,1,0,0,1], 2, 15)
    ]
    
    num_tests = len(test_cases)
    num_correct = 0
    
    for i, (A, S, expected) in enumerate(test_cases):
        actual = numSubarraysWithSum(A, S)
        if actual == expected:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False (Input: {A}, {S}, Expected: {expected}, Actual: {actual})")
    
    print(f"\nCorrect: {num_correct}/{num_tests}")

if __name__ == "__main__":
    test_numSubarraysWithSum()