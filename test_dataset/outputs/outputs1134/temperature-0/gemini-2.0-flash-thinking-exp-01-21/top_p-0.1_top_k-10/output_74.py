def find_concatenated_words(words):
    word_set = set(words)
    concatenated_words = []
    memo = {}

    def is_concatenated(word):
        if word in memo:
            return memo[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in word_set and prefix != word:
                if suffix in word_set and suffix != word:
                    memo[word] = True
                    return True
                if is_concatenated(suffix):
                    memo[word] = True
                    return True
        memo[word] = False
        return False

    for word in words:
        if is_concatenated(word):
            concatenated_words.append(word)
    return concatenated_words

def run_tests():
    test_cases = [
        {
            "input": ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"],
            "expected_output": ["catsdogcats","dogcatsdog","ratcatdogcat"]
        },
        {
            "input": ["cat","dog","catdog"],
            "expected_output": ["catdog"]
        },
        {
            "input": [""],
            "expected_output": []
        },
        {
            "input": ["a", "b", "c", "ab", "bc", "abc"],
            "expected_output": ["ab", "bc", "abc"]
        },
        {
            "input": ["apple", "pen", "applepen", "pineapple"],
            "expected_output": ["applepen"]
        },
        {
            "input": ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"],
            "expected_output": ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        }
    ]

    correct_tests = 0
    for i, test_case in enumerate(test_cases):
        words = test_case["input"]
        expected_output = set(test_case["expected_output"])
        actual_output = set(find_concatenated_words(words))
        if actual_output == expected_output:
            print(f'Test {i+1}: True')
            correct_tests += 1
        else:
            print(f'Test {i+1}: False')
            print(f'  Input: {words}')
            print(f'  Expected: {expected_output}')
            print(f'  Actual:   {actual_output}')

    print(f"\n{correct_tests}/{len(test_cases)} correct tests")

if __name__ == '__main__':
    run_tests()