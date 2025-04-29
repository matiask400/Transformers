def unique_occurrences(arr):
    """
    Given an array of integers arr, returns true if and only if the number of occurrences of each value in the array is unique.

    Args:
        arr: An array of integers.

    Returns:
        True if the number of occurrences of each value in the array is unique, False otherwise.
    """
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    
    occurrences = set()
    for count in counts.values():
        if count in occurrences:
            return False
        occurrences.add(count)
    
    return True

def test_unique_occurrences():
    """
    Tests the unique_occurrences function with several test cases.
    """
    test_cases = [
        ([1,2,2,1,1,3], True),
        ([1,2], False),
        ([-3,0,1,-3,1,1,1,-3,10,0], True),
        ([1,1,2,2,3,3,3], False),
        ([0,0,0,0,0], True),
        ([5], True)
    ]
    
    num_tests = len(test_cases)
    num_correct = 0
    
    for i, (arr, expected) in enumerate(test_cases):
        result = unique_occurrences(arr)
        if result == expected:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: {arr}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
    
    print(f"\nCorrect tests: {num_correct}/{num_tests}")

if __name__ == "__main__":
    test_unique_occurrences()