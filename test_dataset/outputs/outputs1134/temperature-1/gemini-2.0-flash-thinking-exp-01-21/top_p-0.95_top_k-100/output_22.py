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
        ([10, 20, 20], True)
    ]
    correct_tests = 0
    for i, (arr, expected_output) in enumerate(test_cases):
        actual_output = unique_occurrences(arr)
        if actual_output == expected_output:
            print(True)
            correct_tests += 1
        else:
            print(False)
    print(f"{correct_tests}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()