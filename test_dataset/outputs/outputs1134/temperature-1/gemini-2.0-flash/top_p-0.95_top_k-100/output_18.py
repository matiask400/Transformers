def shortest_subarray_to_remove(arr):
    n = len(arr)
    if n <= 1:
        return 0

    # Find the length of the longest non-decreasing prefix
    left = 0
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1

    # If the array is already non-decreasing
    if left == n - 1:
        return 0

    # Find the length of the longest non-decreasing suffix
    right = n - 1
    while right > 0 and arr[right - 1] <= arr[right]:
        right -= 1

    # Remove either the prefix or the suffix
    result = min(n - left - 1, right)

    # Check all possible combinations of prefix and suffix
    i = 0
    j = right
    while i <= left and j < n:
        if arr[i] <= arr[j]:
            result = min(result, j - i - 1)
            i += 1
        else:
            j += 1

    return result

def test_shortest_subarray_to_remove():
    tests = [
        ([1, 2, 3, 10, 4, 2, 3, 5], 3),
        ([5, 4, 3, 2, 1], 4),
        ([1, 2, 3], 0),
        ([1], 0),
        ([2,2,2,1,1,1], 3),
        ([1,2,3,4,5], 0),
        ([5,4,3,2,1,0], 5),
        ([10,9,8,1,2,3], 3),
        ([4,3,2,1,5,6,7],4),
        ([1,3,4,5,2],1),
        ([1, 2, 3, 4, 0], 1)
    ]
    
    correct_count = 0
    total_tests = len(tests)
    
    for arr, expected_output in tests:
        actual_output = shortest_subarray_to_remove(arr)
        if actual_output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Input: {arr}")
            print(f"Expected Output: {expected_output}")
            print(f"Actual Output: {actual_output}")
            
    print(f"{correct_count}/{total_tests}")

test_shortest_subarray_to_remove()