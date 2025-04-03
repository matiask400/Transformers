def find_concatenated_words(words):
    word_set = set(words)
    concatenated_words = []

    def is_concatenated(word):
        if not word:
            return False
        n = len(word)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                sub_word = word[j:i]
                if dp[j] and sub_word in word_set and sub_word != word:
                    dp[i] = True
                    break
        if dp[n]:
            count = 0
            temp_dp = [False] * (n + 1)
            temp_dp[0] = True
            segmentation = [[] for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(i):
                    sub_word = word[j:i]
                    if temp_dp[j] and sub_word in word_set and sub_word != word:
                        temp_dp[i] = True
                        segmentation[i].extend(segmentation[j])
                        segmentation[i].append(sub_word)
                        if temp_dp[i]:
                            break
            if temp_dp[n]:
                parts = segmentation[n]
                if len(parts) >= 2:
                    return True
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
            "input": ["apple", "pen", "applepen", "pine", "pineapple"],
            "expected_output": ["applepen", "pineapple"]
        },
        {
            "input": ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"],
            "expected_output": ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        }
    ]

    num_correct = 0
    for i, test_case in enumerate(test_cases):
        input_words = test_case["input"]
        expected_output = sorted(test_case["expected_output"])
        actual_output = sorted(find_concatenated_words(input_words))
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False")
    print(f"{num_correct}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()