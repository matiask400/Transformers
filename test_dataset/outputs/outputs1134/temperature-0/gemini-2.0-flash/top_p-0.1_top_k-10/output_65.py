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
    count = 0
    for i in range(len(A)):
        current_sum = 0
        for j in range(i, len(A)):
            current_sum += A[j]
            if current_sum == S:
                count += 1
    return count

def test_numSubarraysWithSum():
    test_cases = [
        ([1,0,1,0,1], 2, 4),
        ([0,0,0,0,0], 0, 15),
        ([0,0,1,0,0], 0, 9),
        ([0,0,0,0,0], 3, 0),
        ([1,1,1,1,1], 3, 6),
        ([1,1,1,1,1], 0, 0),
        ([0,0,0,1,1,0,0,0], 2, 7)
    ]
    
    correct_count = 0
    total_count = len(test_cases)
    
    for A, S, expected in test_cases:
        result = numSubarraysWithSum(A, S)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
    
    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_numSubarraysWithSum()