import sys 

# The function to be implemented
def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    """
    Checks if searchWord is a prefix of any word in the sentence.

    Args:
        sentence: A string of words separated by single spaces.
        searchWord: The prefix to search for.

    Returns:
        The 1-indexed position of the first word in the sentence that has
        searchWord as a prefix. Returns -1 if no such word exists.
    """
    # Split the sentence into words based on single spaces.
    # According to the problem description, words are separated by a *single* space.
    words = sentence.split(' ')
    
    # Iterate through the words along with their 0-based index using enumerate.
    # enumerate provides pairs of (index, value).
    for i, word in enumerate(words):
        # The startswith() method checks if the string `word` begins with `searchWord`.
        if word.startswith(searchWord):
            # If a word is found where searchWord is a prefix, return its 1-based index.
            # The index `i` from enumerate is 0-based, so we add 1.
            return i + 1
            
    # If the loop finishes without finding any word that starts with searchWord,
    # it means no such word exists in the sentence. Return -1 as required.
    return -1

# Test runner function
def run_tests():
    """
    Runs predefined test cases against the isPrefixOfWord function
    and prints the results according to the specified format:
    - Prints 'True' for each passed test, 'False' otherwise.
    - Prints a summary line "correct_count/total_tests tests passed."
    """
    test_cases = [
        # Provided Examples
        (("i love eating burger", "burg"), 4),
        (("this problem is an easy problem", "pro"), 2),
        (("i am tired", "you"), -1),
        (("i use triple pillow", "pill"), 4),
        (("hello from the other side", "they"), -1),
        
        # Additional Test Cases
        (("hellohello hellohellohello", "ell"), -1), # Prefix must be at the start of a word, not just contain 'ell'
        (("a", "a"), 1),                         # Single letter word/prefix match
        (("abc", "d"), -1),                        # No match found
        (("ab cd ef", "a"), 1),                   # Match on the first word
        (("ab cd ef", "c"), 2),                   # Match on the second word
        (("fix the bug", "fix"), 1),              # Exact word match is also a prefix match
        (("programming is fun", "pro"), 1),       # Standard prefix case
        (("no prefix here", "pre"), 2),           # 'prefix' is the second word (index 2)
        (("word", "longersearchword"), -1),       # SearchWord is longer than the word, cannot be a prefix
        (("multiple words match", "m"), 1),       # Multiple matches ('multiple', 'match'), return the first index (1)
        (("a b c", "b"), 2),                      # Simple middle match
        (("startswith", "start"), 1),             # Basic startswith check
        (("endswith", "swith"), -1),              # Not a prefix match
    ]

    correct_count = 0
    total_tests = len(test_cases)

    # Iterate through test cases, run the function, and print results
    for i, (inputs, expected_output) in enumerate(test_cases):
        sentence, searchWord = inputs
        
        # Execute the function with the current test case inputs
        result = isPrefixOfWord(sentence, searchWord)
        
        # Compare the actual result with the expected output
        is_correct = (result == expected_output)
        
        # Print True or False for the test case based on correctness
        print(f"{is_correct}")
        
        # Increment the counter for correct tests if the result matches
        if is_correct:
            correct_count += 1

    # After running all tests, print the final summary
    print(f"\n{correct_count}/{total_tests} tests passed.")

# The standard Python entry point. Ensures that run_tests() is called 
# only when the script is executed directly.
if __name__ == "__main__":
    run_tests()