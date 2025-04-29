def subarraysDivByK(A, K):
    count = 0
    prefix_sums = {0: 1}
    current_sum = 0
    for num in A:
        current_sum = (current_sum + num) % K
        if current_sum < 0:
            current_sum += K  # Handle negative remainders
        if current_sum in prefix_sums:
            count += prefix_sums[current_sum]
            prefix_sums[current_sum] += 1
        else:
            prefix_sums[current_sum] = 1
    return count

def test_subarraysDivByK():
    test_cases = [
        ([4, 5, 0, -2, -3, 1], 5, 7),
        ([5], 5, 1),
        ([5, 0], 5, 2),
        ([5, 0, -2, -3], 5, 4),
        ([0], 5, 1),
        ([0, -2, -3], 5, 2),
        ([-2, -3], 5, 1),
        ([5, 5, 5], 5, 6),
        ([-5, -5, -5], 5, 6),
        ([1, 2, 3], 5, 0),
        ([-1, -2, -3], 5, 0),
        ([5, -5, 5, -5], 5, 10),
        ([0, 0, 0, 0], 5, 10),
        ([1, 2, 3, 4, 5], 1, 15),
        ([1, 2, 3, 4, 5], 2, 3),
        ([2,2,2,2,2], 2, 15)
    ]
    
    num_correct = 0
    total_tests = len(test_cases)
    
    for i, (A, K, expected) in enumerate(test_cases):
        result = subarraysDivByK(A, K)
        if result == expected:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False (Input: {A}, {K}, Expected: {expected}, Got: {result})")
    
    print(f"\n{num_correct}/{total_tests} correct")

if __name__ == "__main__":
    test_subarraysDivByK()