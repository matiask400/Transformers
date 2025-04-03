def shortest_subarray_to_remove(arr):
    n = len(arr)
    min_len = n
    for i in range(n + 1):
        for j in range(i, n + 1):
            prefix = arr[:i]
            suffix = arr[j:]
            combined = prefix + suffix
            is_sorted = True
            for k in range(1, len(combined)):
                if combined[k] < combined[k-1]:
                    is_sorted = False
                    break
            if is_sorted:
                removed_len = j - i
                min_len = min(min_len, removed_len)
    return min_len

def run_tests():
    test_cases = [
        ([1,2,3,10,4,2,3,5], 3),
        ([5,4,3,2,1], 4),
        ([1,2,3], 0),
        ([1], 0),
        ([1,2,3,4,5], 0),
        ([5,4,3,2,1,0], 5),
        ([1,3,2,4,5], 1),
        ([1,2,3,4,1], 1),
        ([1,2,3,4,5,0], 1),
        ([0,1,2,3,4,5], 0),
        ([1,1,1,1,1], 0),
        ([1,1,2,2,3,3], 0),
        ([3,2,1,4,5], 3),
        ([1,2,3,4,5,4,3,2,1], 4),
        ([1,2,3,4,5,6,7,8,9,10,1,2,3], 10),
        ([10,9,8,7,6,5,4,3,2,1,1,2,3], 9),
        ([1,2,3,4,5,10,9,8,7,6,5,4,3,2,1], 7)
    ]
    correct_count = 0
    for i, (arr, expected_output) in enumerate(test_cases):
        output = shortest_subarray_to_remove(arr)
        if output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
    print(f"Correct tests: {correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()