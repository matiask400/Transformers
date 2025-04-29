def find_concatenated_words(words):
    """
    Finds all concatenated words in the given list of words.

    A concatenated word is defined as a string that is comprised entirely of at
    least two shorter words in the given array.

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
                    dp[i] = True
                    break
        
        return dp[len(word)]
    
    for word in words:
        word_set.remove(word)
        if is_concatenated(word):
            concatenated_words.append(word)
        word_set.add(word)

    return concatenated_words


def test_find_concatenated_words():
    test_cases = [
        {
            "input": ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"],
            "expected": ["catsdogcats", "dogcatsdog", "ratcatdogcat"],
        },
        {
            "input": ["cat", "dog", "catdog"],
            "expected": ["catdog"],
        },
        {
            "input": ["a", "b", "ab", "abc"],
            "expected": ["ab"],
        },
        {
            "input": [],
            "expected": [],
        },
        {
            "input": [""],
            "expected": [],
        },
        {
            "input": ["aa","a","aaa"],
            "expected": ["aaa"]
        },
        {
            "input": ["abcd","bc","cd","ab","bcd"],
            "expected": ["abcd"]
        },
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        input_words = test_case["input"]
        expected_output = test_case["expected"]
        actual_output = find_concatenated_words(input_words)
        
        actual_output.sort()
        expected_output.sort()

        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: {input_words}")
            print(f"  Expected: {expected_output}")
            print(f"  Actual: {actual_output}")

    print(f"\nCorrect: {num_correct}/{total_tests}")


if __name__ == "__main__":
    test_find_concatenated_words()