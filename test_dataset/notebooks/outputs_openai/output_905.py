def separate_even_odd(A):
    evens = [x for x in A if x % 2 == 0]
    odds = [x for x in A if x % 2 != 0]
    return evens + odds

def run_tests():
    test_cases = [
        {
            "input": [3, 1, 2, 4],
            "expected_outputs": [
                [2, 4, 3, 1],
                [4, 2, 3, 1],
                [2, 4, 1, 3],
                [4, 2, 1, 3]
            ]
        },
        {
            "input": [0],
            "expected_outputs": [[0]]
        },
        {
            "input": [1, 3, 5],
            "expected_outputs": [[1, 3, 5]]
        },
        {
            "input": [2, 4, 6],
            "expected_outputs": [[2, 4, 6]]
        },
        {
            "input": [1, 2, 3, 4, 5, 6],
            "expected_outputs": [
                [2, 4, 6, 1, 3, 5],
                [4, 2, 6, 1, 3, 5],
                [6, 2, 4, 1, 3, 5],
                [2, 6, 4, 1, 3, 5],
                # Other permutations with evens first
            ]
        },
        {
            "input": [5, 2, 8, 1, 4],
            "expected_outputs": [
                [2, 8, 4, 5, 1],
                [8, 2, 4, 5, 1],
                [2, 4, 8, 5, 1],
                [4, 2, 8, 5, 1],
                [8, 4, 2, 5, 1],
                [4, 8, 2, 5, 1],
                # Other permutations with evens first
            ]
        }
    ]
    
    total = len(test_cases)
    correct = 0
    for case in test_cases:
        input_A = case["input"]
        expected = case["expected_outputs"]
        output = separate_even_odd(input_A)
        if output in expected:
            print(True)
            correct += 1
        else:
            print(False)
    print(f"{correct}/{total}")

if __name__ == "__main__":
    run_tests()