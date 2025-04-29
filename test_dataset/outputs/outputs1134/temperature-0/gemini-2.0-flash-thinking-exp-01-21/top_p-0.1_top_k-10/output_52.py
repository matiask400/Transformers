class WordFilter:
    def __init__(self, words):
        self.words = words

    def f(self, prefix, suffix):
        max_index = -1
        for i in range(len(self.words)):
            word = self.words[i]
            if word.startswith(prefix) and word.endswith(suffix):
                max_index = i
        return max_index

def run_tests():
    test_cases = [
        {
            "operations": ["WordFilter", "f"],
            "input": [[["apple"]], ["a", "e"]],
            "expected_output": [None, 0]
        },
        {
            "operations": ["WordFilter", "f"],
            "input": [[["apple", "banana"]], ["a", "e"]],
            "expected_output": [None, 0]
        },
        {
            "operations": ["WordFilter", "f"],
            "input": [[["apple", "banana"]], ["b", "a"]],
            "expected_output": [None, 1]
        },
        {
            "operations": ["WordFilter", "f"],
            "input": [[["apple", "banana", "apply"]], ["ap", "e"]],
            "expected_output": [None, 0]
        },
        {
            "operations": ["WordFilter", "f"],
            "input": [[["apple", "banana", "apply"]], ["ap", "y"]],
            "expected_output": [None, 2]
        },
        {
            "operations": ["WordFilter", "f"],
            "input": [[["apple", "banana", "apply"]], ["ba", "a"]],
            "expected_output": [None, 1]
        },
        {
            "operations": ["WordFilter", "f"],
            "input": [[["apple", "banana", "apply"]], ["z", "z"]],
            "expected_output": [None, -1]
        },
        {
            "operations": ["WordFilter", "f"],
            "input": [[["cabaabaaaa","ccbcababac","bacbcabbca","bacbaabbca","bbbaaabaaa","bacbbacbaa","caabccacca","acbccbccab","cccaaabab","ccaaccaaab"]], ["cba","aba"]],
            "expected_output": [None, -1]
        },
        {
            "operations": ["WordFilter", "f"],
            "input": [[["cabaabaaaa","ccbcababac","bacbcabbca","bacbaabbca","bbbaaabaaa","bacbbacbaa","caabccacca","acbccbccab","cccaaabab","ccaaccaaab"]], ["bac","baa"]],
            "expected_output": [None, 4]
        }
    ]

    correct_tests = 0
    total_tests = 0

    for test_case in test_cases:
        operations = test_case["operations"]
        inputs = test_case["input"]
        expected_output = test_case["expected_output"]

        word_filter = None
        actual_output = []

        for i in range(len(operations)):
            operation = operations[i]
            input_val = inputs[i]
            exp_output = expected_output[i]

            if operation == "WordFilter":
                word_filter = WordFilter(input_val[0])
                actual_output.append(None)
            elif operation == "f":
                result = word_filter.f(input_val[0], input_val[1])
                actual_output.append(result)
                if result == exp_output:
                    print("True")
                    correct_tests += 1
                else:
                    print("False")
            total_tests += 1

    print(f"{correct_tests}/{total_tests-len(test_cases)}") # Subtract the WordFilter init operations

run_tests()