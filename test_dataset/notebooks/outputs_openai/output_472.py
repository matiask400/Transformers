def findAllConcatenatedWords(words):
    words_set = set(words)
    words_sorted = sorted(words, key=lambda x: len(x))
    concatenated = []

    for word in words_sorted:
        if not word:
            continue
        dp = [False] * (len(word) + 1)
        dp[0] = True
        for i in range(1, len(word)+1):
            for j in range(max(0, i - 1000), i):  # since word length <=1000
                if dp[j] and word[j:i] in words_set:
                    dp[i] = True
                    break
        if dp[len(word)]:
            concatenated.append(word)
        words_set.add(word)
    return concatenated

def run_tests():
    test_cases = [
        {
            'words': ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"],
            'expected': ["catsdogcats","dogcatsdog","ratcatdogcat"]
        },
        {
            'words': ["cat","dog","catdog"],
            'expected': ["catdog"]
        }
    ]
    correct = 0
    total = len(test_cases)
    for tc in test_cases:
        output = findAllConcatenatedWords(tc['words'])
        expected = tc['expected']
        result = output == expected
        print(result)
        if result:
            correct +=1
    print(f"{correct}/{total}")

run_tests()