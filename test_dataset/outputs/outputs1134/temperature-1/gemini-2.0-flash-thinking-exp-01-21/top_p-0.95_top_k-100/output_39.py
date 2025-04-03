def shortest_reference_string(words):
    suffixes_words = set()
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[j].endswith(words[i]):
                suffixes_words.add(words[i])
    words_to_encode = []
    for word in words:
        if word not in suffixes_words:
            words_to_encode.append(word)
    s = ""
    for word in words_to_encode:
        s += word + "#"
    return len(s)

def run_tests():
    test_cases = [
        {
            "input": ["time", "me", "bell"],
            "expected_output": 10
        },
        {
            "input": ["t"],
            "expected_output": 2
        },
        {
            "input": ["cat", "cattle", "battle"],
            "expected_output": 13
        },
        {
            "input": ["mass", "as", "hero", "superhero"],
            "expected_output": 10
        },
        {
            "input": ["kuda", "ku"],
            "expected_output": 6
        }
    ]
    num_correct = 0
    for i, test_case in enumerate(test_cases):
        input_words = test_case["input"]
        expected_output = test_case["expected_output"]
        actual_output = shortest_reference_string(input_words)
        if actual_output == expected_output:
            print(True)
            num_correct += 1
        else:
            print(False)
    print(f"{num_correct}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()