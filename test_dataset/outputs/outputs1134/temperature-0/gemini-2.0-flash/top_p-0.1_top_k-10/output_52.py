class WordFilter:

    def __init__(self, words):
        self.words = words

    def f(self, prefix, suffix):
        indices = []
        for i, word in enumerate(self.words):
            if word.startswith(prefix) and word.endswith(suffix):
                indices.append(i)
        if not indices:
            return -1
        else:
            return max(indices)

def test_word_filter():
    test_cases = [
        {
            "operations": ["WordFilter", "f"],
            "input": [[["apple"]], ["a", "e"]],
            "expected": [None, 0]
        },
        {
            "operations": ["WordFilter", "f"],
            "input": [[["apple"]], ["b", "e"]],
            "expected": [None, -1]
        },
        {
            "operations": ["WordFilter", "f"],
            "input": [[["apple", "banana", "apple"]], ["a", "e"]],
            "expected": [None, 2]
        },
        {
            "operations": ["WordFilter", "f"],
            "input": [[["apple", "banana", "apple"]], ["b", "a"]],
            "expected": [None, 1]
        },
        {
            "operations": ["WordFilter", "f"],
            "input": [[["apple", "banana", "apple"]], ["app", "e"]],
            "expected": [None, 2]
        },
        {
            "operations": ["WordFilter", "f"],
            "input": [[["apple", "banana", "apple"]], ["app", "a"]],
            "expected": [None, -1]
        },
        {
            "operations": ["WordFilter", "f"],
            "input": [[["cabaabaaaa", "ccbcababac", "caccbacaab", "bccbacbbca", "bacbcacabb", "bacbbbbaca", "bbbbbbabab", "ababbaaabb", "abaaccabcb", "bcbbbbbbba"]], ["bccbacbbca", "ab"]],
            "expected": [None, -1]
        }
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, test_case in enumerate(test_cases):
        operations = test_case["operations"]
        input_data = test_case["input"]
        expected_output = test_case["expected"]

        word_filter = None
        results = []

        for j, op in enumerate(operations):
            if op == "WordFilter":
                word_filter = WordFilter(input_data[j][0])
                results.append(None)
            elif op == "f":
                result = word_filter.f(input_data[j][0], input_data[j][1])
                results.append(result)

        if results == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

test_word_filter()