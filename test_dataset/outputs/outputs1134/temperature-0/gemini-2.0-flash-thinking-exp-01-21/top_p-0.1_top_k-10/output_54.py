def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    words = sentence.split()
    for index, word in enumerate(words):
        if word.startswith(searchWord):
            return index + 1
    return -1

def run_tests():
    test_cases = [
        {"sentence": "i love eating burger", "searchWord": "burg", "expected": 4},
        {"sentence": "this problem is an easy problem", "searchWord": "pro", "expected": 2},
        {"sentence": "i am tired", "searchWord": "you", "expected": -1},
        {"sentence": "i use triple pillow", "searchWord": "pill", "expected": 4},
        {"sentence": "hello from the other side", "searchWord": "they", "expected": -1},
    ]
    correct_count = 0
    for i, test_case in enumerate(test_cases):
        sentence = test_case["sentence"]
        searchWord = test_case["searchWord"]
        expected = test_case["expected"]
        output = isPrefixOfWord(sentence, searchWord)
        if output == expected:
            print(True)
            correct_count += 1
        else:
            print(False)
    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()