import collections

def solve():
    """
    Solves the Sort Array By Parity problem.
    Given an array A of non-negative integers, returns an array consisting
    of all the even elements of A, followed by all the odd elements of A.
    Includes test cases and prints the results.
    """

    def sortArrayByParity(A):
        """
        Sorts the array A by parity (even numbers first, then odd numbers).

        Args:
            A: A list of non-negative integers.

        Returns:
            A list with even numbers followed by odd numbers from A.
            The relative order of even numbers among themselves, and odd numbers
            among themselves, is preserved from the original array.
        """
        evens = []
        odds = []
        for num in A:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        return evens + odds

    # More robust check function (optional, but good practice for this problem)
    # This checks if the output satisfies the condition, regardless of the
    # specific order within even/odd groups, which aligns better with the
    # problem statement "You may return any answer array that satisfies this condition."
    def check_parity_sort(original, result):
        if len(original) != len(result):
            return False
        # Ensure the same elements are present with the same frequency
        if collections.Counter(original) != collections.Counter(result):
             return False

        found_odd = False
        for x in result:
            is_even = (x % 2 == 0)
            if found_odd and is_even: # Found an even number after an odd number
                return False
            if not is_even:
                found_odd = True
        return True # If loop completes, partitioning is correct


    # Test cases: Input array and *one possible* expected output.
    # Note: The simple implementation `sortArrayByParity` above will always
    # produce the same output for a given input because it preserves relative order.
    # If using an in-place swap method, the output might vary but still be valid.
    test_cases = [
        # Input array, Expected output (produced by the specific implementation)
        ([3, 1, 2, 4], [2, 4, 3, 1]),
        ([0], [0]),
        ([1], [1]),
        ([2, 1], [2, 1]),
        ([1, 2], [2, 1]),
        ([0, 2, 4], [0, 2, 4]),
        ([1, 3, 5], [1, 3, 5]),
        ([], []),
        ([4, 1, 3, 2, 5], [4, 2, 1, 3, 5]),
        ([2, 4, 1, 3], [2, 4, 1, 3]), # Already sorted by parity
        ([1, 3, 2, 4], [2, 4, 1, 3]),
        ([0, 1, 0, 1, 0], [0, 0, 0, 1, 1]),
        ([5000, 4999, 0, 1], [5000, 0, 4999, 1]),
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (input_arr, expected_output) in enumerate(test_cases):
        # Pass a copy of the input list to the function,
        # especially important if the function modifies the list in-place.
        result = sortArrayByParity(list(input_arr))

        # Option 1: Compare with the specific expected output (as requested by prompt format)
        is_correct_specific = (result == expected_output)

        # Option 2: Use the robust check (validates any correct partitioning)
        # is_correct_robust = check_parity_sort(input_arr, result)

        # Using Option 1 for this specific prompt requirement
        is_correct = is_correct_specific

        print(f"{is_correct}")
        if is_correct:
            correct_count += 1

    print(f"{correct_count}/{total_tests}")

# Execute the solve function when the script is run
if __name__ == "__main__":
    solve()