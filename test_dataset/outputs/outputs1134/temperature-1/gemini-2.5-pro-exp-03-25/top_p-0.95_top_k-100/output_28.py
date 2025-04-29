import re
import collections

def mostFrequentNonBanned(paragraph: str, banned: list[str]) -> str:
    """
    Finds the most frequent word in a paragraph that is not in a list of banned words.

    Args:
        paragraph: The input string paragraph.
        banned: A list of banned words (lowercase).

    Returns:
        The most frequent non-banned word in lowercase.
    """
    # 1. Preprocessing:
    #    - Convert to lowercase.
    #    - Use regex to find all sequences of word characters (\w+). 
    #      This automatically handles punctuation removal and splitting.
    words = re.findall(r'\w+', paragraph.lower())

    # 2. Create a set of banned words for efficient lookup (O(1) average time).
    banned_set = set(banned)

    # 3. Filter out banned words.
    non_banned_words = [word for word in words if word not in banned_set]

    # 4. Count the frequency of the remaining words.
    #    collections.Counter is efficient for this.
    #    It handles the case where non_banned_words might be empty (though the problem guarantees it won't be).
    word_counts = collections.Counter(non_banned_words)

    # 5. Find the most frequent word.
    #    The problem guarantees at least one non-banned word and a unique answer.
    #    most_common(1) returns a list containing the single most common element 
    #    as a tuple: [('word', count)].
    if not word_counts:
        # This case should not happen based on problem constraints, 
        # but included for robustness if constraints were different.
        return "" 
        
    # Get the word from the most common tuple
    most_frequent_word = word_counts.most_common(1)[0][0]

    return most_frequent_word

# Test harness
def solve():
    """
    Runs test cases against the mostFrequentNonBanned function.
    """
    tests = [
        # Example 1
        ({"paragraph": "Bob hit a ball, the hit BALL flew far after it was hit.", "banned": ["hit"]}, "ball"),
        # Example 2
        ({"paragraph": "a.", "banned": []}, "a"),
        # Additional Test Cases
        ({"paragraph": "Bob", "banned": []}, "bob"), # Single word, not banned
        ({"paragraph": "Bob", "banned": ["bob"]}, ""), # Single word, banned (violates guarantee, but let's see) -> Test updated based on guarantee
        ({"paragraph": "Bob bOb BoB", "banned": []}, "bob"), # Case insensitivity test
        ({"paragraph": "a, a, a, a, b,b,b,c, c", "banned": ["a"]}, "b"), # Multiple occurrences, one banned
        ({"paragraph": "Jack and Jill went to the market to buy bread and cheese. Cheese is Jack's and Jill's favorite food.", 
          "banned": ["and", "he", "the", "to", "is", "jack", "jill"]}, "cheese"), # More complex sentence, case insensitive banning
        ({"paragraph": "   leading spaces Bob? Hit? ball! ", "banned": ["hit"]}, "bob"), # Leading/trailing spaces and punctuation
        ({"paragraph": "symbols! test? with, symbols; right. next.to.words", "banned": []}, "symbols"), # Punctuation attached
        ({"paragraph": "only.,!? punct", "banned": []}, "punct"), # Mostly punctuation
        ({"paragraph": "word word word", "banned": ["word"]}, ""), # All words banned (violates guarantee) -> Test updated
        ({"paragraph": "apple banana orange apple banana apple", "banned": ["banana"]}, "apple"), # Standard case
    ]

    # Adjust tests based on guarantees (at least one non-banned word)
    tests_adjusted = [
        ({"paragraph": "Bob hit a ball, the hit BALL flew far after it was hit.", "banned": ["hit"]}, "ball"),
        ({"paragraph": "a.", "banned": []}, "a"),
        ({"paragraph": "Bob", "banned": []}, "bob"),
        ({"paragraph": "Bob bOb BoB", "banned": []}, "bob"), 
        ({"paragraph": "a, a, a, a, b,b,b,c, c", "banned": ["a"]}, "b"), 
        ({"paragraph": "Jack and Jill went to the market to buy bread and cheese. Cheese is Jack's and Jill's favorite food.", 
          "banned": ["and", "he", "the", "to", "is", "jack", "jill"]}, "cheese"), 
        ({"paragraph": "   leading spaces Bob? Hit? ball! ", "banned": ["hit"]}, "bob"), 
        ({"paragraph": "symbols! test? with, symbols; right. next.to.words", "banned": []}, "symbols"), 
        ({"paragraph": "only.,!? punct", "banned": []}, "punct"), 
        ({"paragraph": "apple banana orange apple banana apple", "banned": ["banana"]}, "apple"),
        ({"paragraph": "word word word one", "banned": ["word"]}, "one"), # Ensure non-banned exists
        ({"paragraph": "Bob is bob", "banned": ["is"]}, "bob"), # Ensure unique answer handled correctly
    ]


    correct_count = 0
    total_tests = len(tests_adjusted)

    for i, (inputs, expected_output) in enumerate(tests_adjusted):
        paragraph = inputs["paragraph"]
        banned = inputs["banned"]
        
        try:
            actual_output = mostFrequentNonBanned(paragraph, banned)
            if actual_output == expected_output:
                print(f"Test {i+1}: True")
                correct_count += 1
            else:
                print(f"Test {i+1}: False - Input: {inputs}, Expected: '{expected_output}', Got: '{actual_output}'")
        except Exception as e:
            print(f"Test {i+1}: Error - Input: {inputs}, Error: {e}")

    print(f"{correct_count}/{total_tests} tests passed.")

# Execute the test harness
solve()