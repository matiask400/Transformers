def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    words = sentence.split(" ")
    for i in range(len(words)):
        if words[i].startswith(searchWord):
            return i + 1
    return -1

def test_isPrefixOfWord():
    test_cases = [
        {"sentence": "i love eating burger", "searchWord": "burg", "expected_output": 4},
        {"sentence": "this problem is an easy problem", "searchWord": "pro", "expected_output": 2},
        {"sentence": "i am tired", "searchWord": "you", "expected_output": -1},
        {"sentence": "i use triple pillow", "searchWord": "pill", "expected_output": 4},
        {"sentence": "hello from the other side", "searchWord": "they", "expected_output": -1},
        {"sentence": "hellohello", "searchWord": "o", "expected_output": 1},
        {"sentence": "burg burger", "searchWord": "burg", "expected_output": 1},
        {"sentence": "prefix wordprefix", "searchWord": "prefix", "expected_output": 1},
        {"sentence": "word prefix", "searchWord": "prefix", "expected_output": 2},
        {"sentence": "word wordprefix", "searchWord": "prefix", "expected_output": -1},
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        sentence = test_case["sentence"]
        searchWord = test_case["searchWord"]
        expected_output = test_case["expected_output"]
        actual_output = isPrefixOfWord(sentence, searchWord)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")

    print(f"\n{correct_tests}/{total_tests}")

if __name__ == '__main__':
    test_isPrefixOfWord()