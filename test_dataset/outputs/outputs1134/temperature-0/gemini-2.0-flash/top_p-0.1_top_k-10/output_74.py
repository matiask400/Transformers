def find_concatenated_words(words):
    """
    Finds all concatenated words in the given list of words.

    A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

    Args:
        words: A list of strings (without duplicates).

    Returns:
        A list of concatenated words.
    """

    word_set = set(words)
    concatenated_words = []

    def is_concatenated(word):
        if not word:
            return False
        
        dp = [False] * (len(word) + 1)
        dp[0] = True

        for i in range(1, len(word) + 1):
            for j in range(i):
                if dp[j] and word[j:i] in word_set:
                    if word[j:i] != word or len(word) == len(word[j:i]):
                        dp[i] = True
                        break
        return dp[len(word)]

    for word in words:
        if is_concatenated(word):
            concatenated_words.append(word)

    return concatenated_words


def test_find_concatenated_words():
    """
    Tests the find_concatenated_words function with several test cases.
    """

    test_cases = [
        {
            "input": ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"],
            "expected": ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
        },
        {
            "input": ["cat", "dog", "catdog"],
            "expected": ["catdog"]
        },
        {
            "input": ["a", "b", "ab", "abc"],
            "expected": ["ab"]
        },
        {
            "input": ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"],
            "expected": ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        },
        {
            "input": [],
            "expected": []
        },
        {
            "input": [""],
            "expected": []
        },
        {
            "input": ["a", "aa"],
            "expected": ["aa"]
        }
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        input_words = test_case["input"]
        expected_output = test_case["expected"]
        actual_output = find_concatenated_words(input_words)

        if sorted(actual_output) == sorted(expected_output):
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: {input_words}")
            print(f"  Expected: {expected_output}")
            print(f"  Actual: {actual_output}")

    print(f"\nCorrect tests: {num_correct}/{total_tests}")


if __name__ == "__main__":
    test_find_concatenated_words()