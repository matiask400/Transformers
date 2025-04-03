def is_prefix_of_word(sentence: str, searchWord: str) -> int:
    """
    Given a `sentence` that consists of some words separated by a single space, and a `searchWord`.

    You have to check if `searchWord` is a prefix of any word in `sentence`.

    Return the index of the word in `sentence` where `searchWord` is a prefix of this word (1-indexed).

    If `searchWord` is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

    A prefix of a string `S` is any leading contiguous substring of `S`.
    """
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
            "sentence": "hello hellohello hellohellohello",
            "searchWord": "ell",
            "expected": 1
        },
        {
            "sentence": "a",
            "searchWord": "a",
            "expected": 1
        },
        {
            "sentence": "a b",
            "searchWord": "a",
            "expected": 1
        },
        {
            "sentence": "a b",
            "searchWord": "b",
            "expected": 2
        },
        {
            "sentence": "a b",
            "searchWord": "c",
            "expected": -1
        }
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, test_case in enumerate(test_cases):
        sentence = test_case["sentence"]
        searchWord = test_case["searchWord"]
        expected = test_case["expected"]
        actual = is_prefix_of_word(sentence, searchWord)

        if actual == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Actual: {actual})")

    print(f"\nCorrect: {correct_count}/{total_count}")

if __name__ == "__main__":
    test_is_prefix_of_word()