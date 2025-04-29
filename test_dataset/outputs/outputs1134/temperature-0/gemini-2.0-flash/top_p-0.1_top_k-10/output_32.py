def subarraysDivByK(A, K):
    count = 0
    prefix_sums = {0: 1}
    current_sum = 0
    for num in A:
        current_sum = (current_sum + num) % K
        if current_sum < 0:
            current_sum += K
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
        ([1,2,3,4,5], 5, 4),
        ([1,2,3,4,5], 1, 15),
        ([1,2,3,4,5], 6, 0),
        ([5,5,5,5,5], 5, 15),
        ([-5,-5,-5,-5,-5], 5, 15),
        ([1, -1], 5, 0),
        ([5, -5], 5, 3),
        ([10, -5], 5, 3),
        ([10, 5], 5, 3),
        ([1,2,3,4,5,6,7,8,9,10], 5, 11)
    ]
    
    correct_count = 0
    total_count = len(test_cases)
    
    for i, (A, K, expected) in enumerate(test_cases):
        result = subarraysDivByK(A, K)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Got: {result})")
            
    print(f"\nCorrect: {correct_count}/{total_count}")

if __name__ == "__main__":
    test_subarraysDivByK()