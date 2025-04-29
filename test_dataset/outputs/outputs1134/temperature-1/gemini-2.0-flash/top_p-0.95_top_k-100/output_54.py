def is_prefix_of_word(sentence, searchWord):
    words = sentence.split()
    for i, word in enumerate(words):
        if word.startswith(searchWord):
            return i + 1
    return -1

def test_is_prefix_of_word():
    test_cases = [
        {
            "sentence": "i love eating burger",
            "searchWord": "burg",
            "expected": 4
        },
        {
            "sentence": "this problem is an easy problem",
            "searchWord": "pro",
            "expected": 2
        },
        {
            "sentence": "i am tired",
            "searchWord": "you",
            "expected": -1
        },
        {
            "sentence": "i use triple pillow",
            "searchWord": "pill",
            "expected": 4
        },
        {
            "sentence": "hello from the other side",
            "searchWord": "they",
            "expected": -1
        },
        {
            "sentence": "a b c d",
            "searchWord": "a",
            "expected": 1
        },
        {
            "sentence": "hello",
            "searchWord": "he",
            "expected": 1
        },
        {
            "sentence": "hello",
            "searchWord": "hell",
            "expected": 1
        },
        {
            "sentence": "hello",
            "searchWord": "hello",
            "expected": 1
        },
        {
            "sentence": "hello",
            "searchWord": "helloo",
            "expected": -1
        },
        {
            "sentence": "hello",
            "searchWord": "el",
            "expected": -1
        }
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, test_case in enumerate(test_cases):
        sentence = test_case["sentence"]
        searchWord = test_case["searchWord"]
        expected = test_case["expected"]
        
        result = is_prefix_of_word(sentence, searchWord)
        
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Test Case {i+1} Failed: Expected {expected}, Got {result}")

    print(f"{correct_count}/{total_count}")

test_is_prefix_of_word()