import re
import collections

def solve():
    """
    Solves the most frequent non-banned word problem and runs tests.
    """

    def mostCommonWord(paragraph: str, banned: list[str]) -> str:
        """
        Finds the most frequent word in the paragraph that is not in the banned list.

        Args:
            paragraph: The input string paragraph.
            banned: A list of banned words.

        Returns:
            The most frequent non-banned word in lowercase.
        """
        # 1. Preprocessing: lowercase, remove punctuation, split into words
        # Replace non-word characters (anything not a letter or number) with space,
        # convert to lowercase, and split into words.
        # \w+ matches sequences of alphanumeric characters (words)
        words = re.findall(r'\w+', paragraph.lower())

        # 2. Create a set of banned words for efficient O(1) average time lookup
        banned_set = set(banned)

        # 3. Count frequencies of non-banned words
        word_counts = collections.Counter()
        for word in words:
            if word not in banned_set:
                word_counts[word] += 1

        # 4. Find the most frequent word
        # The problem guarantees at least one non-banned word and a unique answer.
        # Counter.most_common(1) returns a list with one tuple: [(word, count)]
        if not word_counts:
             # This case should not happen based on problem constraints
             # (guaranteed at least one non-banned word)
             # If it could happen, we might return "" or raise an error.
             # Given the constraints, we expect word_counts to be non-empty.
             return ""

        # Return the word part of the most common tuple
        return word_counts.most_common(1)[0][0]

        # Alternative using max:
        # if not word_counts:
        #     return ""
        # return max(word_counts, key=word_counts.get)


    # Test framework
    def run_tests():
        """
        Runs predefined test cases against the mostCommonWord function.
        """
        tests = [
            # Test Case 1: Example 1
            (("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]), "ball"),
            # Test Case 2: Example 2
            (("a.", []), "a"),
            # Test Case 3: Multiple occurrences, different cases, punctuation
            (("a, a, a, a, b,b,b,c, c", ["a"]), "b"),
            # Test Case 4: Single word paragraph, no banned words
            (("Bob", []), "bob"),
            # Test Case 5: Single word paragraph with punctuation, banned list present but irrelevant
            (("Bob!", ["hit"]), "bob"),
            # Test Case 6: Paragraph with only non-banned words and punctuation
            (("This is a test. Test it well!", []), "test"),
            # Test Case 7: Punctuation attached to words
            (("word,word!word? another;word.", ["word"]), "another"),
             # Test Case 8: Empty banned list, mixed case
            (("The Quick Brown Fox Jumps Over The Lazy Dog.", []), "the"),
            # Test Case 9: All words banned except one
            (("one two three four", ["one", "two", "four"]), "three"),
            # Test Case 10: More complex punctuation and spacing
            (("  leading spaces; multiple words...  trailing spaces??", []), "spaces"),

        ]

        correct_count = 0
        total_tests = len(tests)

        for i, (inputs, expected_output) in enumerate(tests):
            paragraph, banned = inputs
            # Make a copy of banned list if the function modifies it (it doesn't here)
            # banned_copy = list(banned)
            actual_output = mostCommonWord(paragraph, banned)
            result = actual_output == expected_output
            print(f"Test {i+1}: {result}")
            if result:
                correct_count += 1
            else:
                print(f"  Input: paragraph='{paragraph}', banned={banned}")
                print(f"  Expected: '{expected_output}'")
                print(f"  Actual:   '{actual_output}'")


        print(f"\n{correct_count}/{total_tests} tests passed.")

    # Execute the tests
    run_tests()

# Run the solution function
solve()