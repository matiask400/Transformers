import sys

# Function definition
def removePalindromeSub(s: str) -> int:
    """
    Calculates the minimum number of steps to make the given string empty
    by removing palindromic subsequences.

    A subsequence of a string is obtained by deleting zero or more characters
    without changing the order of the remaining characters.
    A palindrome is a string that reads the same forwards and backward.
    The input string s consists only of 'a' and 'b'.

    Args:
        s: The input string consisting only of 'a' and 'b'. 
           (Constraint: 1 <= s.length <= 1000)

    Returns:
        The minimum number of steps (which will be 1 or 2 for non-empty strings
        made of 'a's and 'b's). Returns 1 if the string is already a 
        palindrome, and 2 otherwise.
    """
    # Constraint guarantees s is not empty (s.length >= 1).
    
    # Check if the string is a palindrome.
    # A string is a palindrome if it reads the same forwards and backward.
    # Python's slicing s[::-1] reverses the string.
    if s == s[::-1]:
        # If the string itself is a palindrome, it forms a palindromic subsequence.
        # We can remove the entire string in one step.
        return 1
    else:
        # If the string is not a palindrome, we need to determine the minimum steps.
        # Crucially, the string only contains 'a' and 'b'.
        # Consider the subsequence formed by all 'a's in the string. 
        # This subsequence (e.g., "aaaa") is always a palindrome.
        # Consider the subsequence formed by all 'b's in the string.
        # This subsequence (e.g., "bbbb") is also always a palindrome.
        #
        # Therefore, if the string s is not a palindrome itself, we can always 
        # remove all 'a's in one step (as a palindromic subsequence) and then 
        # remove all 'b's in a second step (as another palindromic subsequence).
        # This guarantees that any non-palindrome string composed only of 'a's 
        # and 'b's can be emptied in at most 2 steps.
        # Since we already handled the 1-step case (s is a palindrome), 
        # the minimum steps for a non-palindrome must be 2.
        return 2

# Test framework
def run_tests():
    """Runs the test cases."""
    test_cases = [
        # Provided examples
        ("ababa", 1),
        ("abb", 2),
        ("baabb", 2),
        
        # Edge cases and simple cases
        ("a", 1),         # Palindrome
        ("b", 1),         # Palindrome
        ("aa", 1),        # Palindrome
        ("bb", 1),        # Palindrome
        ("ab", 2),        # Not a palindrome
        ("ba", 2),        # Not a palindrome
        
        # All same character (always palindromes)
        ("aaaaa", 1),
        ("bbbbb", 1),
        
        # Mixed non-palindromes
        ("bbaaa", 2),
        ("aabbb", 2),
        ("bbaabbaab", 2), # Longer non-palindrome
        
        # Longer palindromes
        ("abaaba", 1),
        ("aabbaa", 1),
        ("racecar", None), # Example with other chars (not allowed by constraints, test logic handles) -> Should not happen based on constraints
        
        # Longer non-palindromes with alternating chars
        ("ababababab", 2), 
        ("bababababa", 2), 
        
        # Single character string repeated (palindrome)
        ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 1),
        
        # Mixed string near max length (non-palindrome)
        ("ba" * 499 + "b", 2),
        
        # Mixed string near max length (palindrome)
        ("ab" * 250 + "a" + "ba" * 250 , 1) # Length 1 + 500 + 500 = 1001 - adjust slightly
        
    ]
    
    # Adjusting the last test case to fit length constraint 1000
    test_cases.append(("a" * 500 + "b" * 500, 2)) # Non-palindrome, length 1000
    test_cases.append(("a" * 500 + "a" * 500, 1)) # Palindrome, length 1000
    test_cases.append(("ab" * 500, 2)) # Non-palindrome, length 1000


    # Filter out invalid test cases based on constraints if needed (e.g., 'racecar')
    valid_test_cases = []
    for s, expected in test_cases:
        if expected is None: # Skip tests not conforming to constraints
            continue 
        if not isinstance(s, str) or not (1 <= len(s) <= 1000):
             print(f"Skipping invalid test input (length constraint): {s}")
             continue
        if not all(c in 'ab' for c in s):
             print(f"Skipping invalid test input (character constraint): {s}")
             continue
        valid_test_cases.append((s, expected))


    correct_count = 0
    total_tests = len(valid_test_cases)

    for i, (input_s, expected_output) in enumerate(valid_test_cases):
        # Calculate the result using the implemented function
        result = removePalindromeSub(input_s)
        
        # Check if the result matches the expected output
        is_correct = (result == expected_output)
        
        # Print True or False for the test case
        print(f"{is_correct}") 
        
        if is_correct:
            correct_count += 1

    # Print the final summary: number of correct tests / total number of tests
    print(f"{correct_count}/{total_tests}")

# Execute the tests when the script is run directly
if __name__ == "__main__":
    run_tests()