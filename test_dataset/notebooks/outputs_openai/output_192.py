def run_tests():
    test_cases = [
        (
            "the day is sunny the the\nthe sunny is is",
            ["the 4", "is 3", "sunny 2", "day 1"]
        ),
        (
            "hello world hello",
            ["hello 2", "world 1"]
        ),
        (
            "one two three four five",
            ["one 1", "two 1", "three 1", "four 1", "five 1"]
        ),
        (
            "",
            []
        ),
        (
            "test test test test",
            ["test 4"]
        )
    ]
    
    correct = 0
    total = len(test_cases)
    
    for input_text, expected in test_cases:
        word_counts = {}
        for word in input_text.split():
            word_counts[word] = word_counts.get(word, 0) + 1
        sorted_words = sorted(word_counts.items(), key=lambda x: -x[1])
        actual = [f"{word} {count}" for word, count in sorted_words]
        result = actual == expected
        print(result)
        if result:
            correct += 1
    
    print(f"{correct}/{total}")

run_tests()