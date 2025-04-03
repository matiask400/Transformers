def unique_occurrences(arr):
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1

    occurrence_counts = list(counts.values())
    return len(occurrence_counts) == len(set(occurrence_counts))

def run_tests():
    test_cases = [
        ([1,2,2,1,1,3], True),
        ([1,2], False),
        ([-3,0,1,-3,1,1,1,-3,10,0], True),
        ([1,1,1,2,2,2,3,3], False),
        ([10,20,20,10,10,30,50,10,20], False),
        ([1,2,3,4,5], True),
        ([1], True),
        ([], True) # Empty array should return true as there are no occurrences to compare
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, (input_arr, expected_output) in enumerate(test_cases):
        actual_output = unique_occurrences(input_arr)
        if actual_output == expected_output:
            print(True)
            correct_tests += 1
        else:
            print(False)

    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()