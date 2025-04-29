import sys 

def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    """
    Checks if searchWord is a prefix of any word in the sentence.

    Args:
        sentence: A string consisting of words separated by single spaces.
        searchWord: The prefix string to search for.

    Returns:
        The 1-indexed position of the first word in the sentence that has
        searchWord as a prefix. Returns -1 if no such word is found.
    """
    words = sentence.split(' ')
    for i, word in enumerate(words):
        # The startswith() method checks if a string starts with the specified prefix.
        if word.startswith(searchWord):
            # Return the 1-based index
            return i + 1
    # If the loop finishes without finding a match, return -1
    return -1

def run_tests():
    """
    Runs predefined test cases against the isPrefixOfWord function and prints the results.
    """
    test_cases = [
        # Example 1
        {"input": {"sentence": "i love eating burger", "searchWord": "burg"}, "expected": 4},
        # Example 2
        {"input": {"sentence": "this problem is an easy problem", "searchWord": "pro"}, "expected": 2},
        # Example 3
        {"input": {"sentence": "i am tired", "searchWord": "you"}, "expected": -1},
        # Example 4
        {"input": {"sentence": "i use triple pillow", "searchWord": "pill"}, "expected": 4},
        # Example 5
        {"input": {"sentence": "hello from the other side", "searchWord": "they"}, "expected": -1},
        # Additional Test Cases
        {"input": {"sentence": "hellohello hellohellohello", "searchWord": "ell"}, "expected": -1}, # Prefix must be at the start
        {"input": {"sentence": "a", "searchWord": "a"}, "expected": 1},               # Single word, exact match
        {"input": {"sentence": "abc", "searchWord": "d"}, "expected": -1},            # Single word, no match
        {"input": {"sentence": "burg burger burgh", "searchWord": "burg"}, "expected": 1}, # First word matches
        {"input": {"sentence": "corona dream", "searchWord": "cd"}, "expected": -1}, # Not a prefix
        {"input": {"sentence": "leetcode", "searchWord": "leet"}, "expected": 1}, # Single word sentence, prefix match
        {"input": {"sentence": "leet code", "searchWord": "leet"}, "expected": 1}, # First word prefix match
        {"input": {"sentence": " code leet", "searchWord": "leet"}, "expected": 2}, # Second word prefix match
    ]

    passed_count = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        sentence = test_case["input"]["sentence"]
        searchWord = test_case["input"]["searchWord"]
        expected = test_case["expected"]
        
        result = isPrefixOfWord(sentence, searchWord)
        
        if result == expected:
            print("True")
            passed_count += 1
        else:
            # To make output exactly match the request, only print True/False per test
            print("False") 
            # Optional detailed failure message:
            # print(f"Test {i+1}: False (Input: sentence='{sentence}', searchWord='{searchWord}', Expected: {expected}, Got: {result})")

    print(f"{passed_count}/{total_tests}")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()