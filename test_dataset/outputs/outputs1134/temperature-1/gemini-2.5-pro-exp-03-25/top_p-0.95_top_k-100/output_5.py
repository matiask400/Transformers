import sys 
# Setting higher recursion depth for potentially deep stacks if needed, though unlikely here.
# sys.setrecursionlimit(2000) 

def solve():
    """
    Solves the Large Group Positions problem. Finds intervals of consecutive identical characters
    of length 3 or more in a given string. Contains the core logic and the test runner.
    """

    def largeGroupPositions(s: str) -> list[list[int]]:
        """
        Finds all large groups (3 or more consecutive identical characters) in string s.

        Args:
            s: The input string of lowercase English letters. 
               Constraints: 1 <= s.length <= 1000, s contains lower-case English letters only.

        Returns:
            A list of lists, where each inner list is [start, end] representing
            the interval of a large group, sorted by start index.
        """
        result = []
        n = len(s)
        
        # Optimization: No large groups possible if length < 3
        if n < 3: 
            return []

        start = 0 # Start index of the current potential group
        
        # Iterate through the string, checking for group boundaries
        # We iterate up to n (inclusive) to handle the last group easily.
        for i in range(1, n + 1):
            # A group ends if:
            # 1. We reach the end of the string (i == n)
            # 2. The current character s[i] is different from the previous one s[i-1]
            if i == n or s[i] != s[i-1]:
                # The group that started at index 'start' ended at index 'i-1'.
                # Calculate its length.
                length = i - start
                
                # If the group is large (length >= 3), record its interval [start, end].
                if length >= 3:
                    result.append([start, i - 1])
                
                # Start the next potential group at the current index i.
                # This works even when i == n, as the loop terminates immediately after.
                start = i
        
        # The result list is naturally sorted by start index because we process 
        # groups from left to right as we find them.
        return result

    # --- Test Runner ---
    def run_tests():
        """
        Runs predefined test cases against the largeGroupPositions function and prints results
        in the specified format.
        """
        test_cases = [
            # Provided Examples
            ("abbxxxxzzy", [[3, 6]]),
            ("abc", []),
            ("abcdddeeeeaabbbcd", [[3, 5], [6, 9], [12, 14]]),
            ("aba", []),
            
            # Additional Test Cases
            ("aaa", [[0, 2]]),             # Single large group at the beginning
            ("aaabbb", [[0, 2], [3, 5]]),  # Two adjacent large groups
            ("aaabbaaa", [[0, 2], [5, 7]]),# Large groups separated by non-large group
            ("a", []),                      # Single character string (length < 3)
            ("aa", []),                     # Two character string (length < 3)
            ("bbbaaa", [[0, 2], [3, 5]]),  # Multiple large groups
            # ("" handled by length check) # Empty string (Constraint: length >= 1)
            ("eeee", [[0,3]]),              # String is one large group
            ("xyz", []),                    # No repeating characters
            ("zyyyyxxxxw", [[1,4], [5,8]]),  # Multiple large groups
            ("aaaaabbbbbccccc", [[0, 4], [5, 9], [10, 14]]), # Multiple adjacent large groups
            ("abbcccddddeeeeeffffff", [[2,4], [5,8], [9,13], [14,19]]) # Increasing length large groups
        ]
        
        correct_count = 0
        total_tests = len(test_cases)

        for i, (s_input, expected_output) in enumerate(test_cases):
            # Run the function with the test input
            actual_output = largeGroupPositions(s_input)
            
            # Compare the actual output with the expected output
            passed = actual_output == expected_output
            
            # Print the result for each test as True or False
            print(f"{passed}")
            
            # Count correctly passed tests
            if passed:
                correct_count += 1

        # Print the final summary: number of correct tests / total tests
        print(f"{correct_count}/{total_tests}")

    # Execute the tests
    run_tests()

# Ensures the solve() function is called when the script is executed directly
if __name__ == "__main__":
    solve()