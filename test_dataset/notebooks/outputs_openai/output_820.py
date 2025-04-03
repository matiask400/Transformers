def minimum_length_encoding(words):
    unique_words = set(words)
    for word in words:
        for k in range(1, len(word)):
            suffix = word[k:]
            if suffix in unique_words:
                unique_words.discard(suffix)
    return sum(len(word) + 1 for word in unique_words)

def run_tests():
    test_cases = [
        (["time", "me", "bell"], 10),
        (["t"], 2),
        (["time", "ime", "me", "e"], 6),
        (["a", "b", "c"], 6),
        (["apple", "ple", "pple"], 6),
        (["abc", "bc", "c"], 4),
        (["cat","bat","rat"], 12),
        (["leetcode","code","leetcode"], 10),
        (["aabbcc","aabbcc","aabbcc"], 7),
        (["xyz","yz","z"], 4)
    ]
    correct = 0
    total = len(test_cases)
    for words, expected in test_cases:
        result = minimum_length_encoding(words)
        if result == expected:
            print(True)
            correct +=1
        else:
            print(False)
    print(f"{correct}/{total}")

run_tests()