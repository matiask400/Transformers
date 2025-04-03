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

def run_test(commands, inputs, expected_output):
    word_filter = None
    test_results = []
    for i in range(len(commands)):
        command = commands[i]
        input_val = inputs[i]
        expected_val = expected_output[i]

        if command == "WordFilter":
            word_filter = WordFilter(input_val[0])
            output_val = None
        elif command == "f":
            output_val = word_filter.f(input_val[0], input_val[1])
        else:
            raise ValueError("Unknown command")

        if output_val == expected_val:
            test_results.append(True)
            print('True')
        else:
            test_results.append(False)
            print('False')
            print(f"Input: commands={commands[i:i+1]}, inputs={inputs[i:i+1]}")
            print(f"Expected: {expected_val}, Got: {output_val}")

    correct_count = sum(test_results)
    total_count = len(test_results)
    print(f"{correct_count}/{total_count}")

# Example 1
commands1 = ["WordFilter", "f"]
inputs1 = [[["apple"]], ["a", "e"]]
expected_output1 = [None, 0]
run_test(commands1, inputs1, expected_output1)

# Test case 2
commands2 = ["WordFilter", "f"]
inputs2 = [[["apple", "banana"]], ["a", "a"]]
expected_output2 = [None, -1]
run_test(commands2, inputs2, expected_output2)

# Test case 3
commands3 = ["WordFilter", "f"]
inputs3 = [[["apple", "banana"]], ["b", "a"]]
expected_output3 = [None, 1]
run_test(commands3, inputs3, expected_output3)

# Test case 4
commands4 = ["WordFilter", "f"]
inputs4 = [[["apple", "banana"]], ["ap", "le"]]
expected_output4 = [None, 0]
run_test(commands4, inputs4, expected_output4)

# Test case 5
commands5 = ["WordFilter", "f"]
inputs5 = [[["apple", "banana"]], ["ban", "na"]]
expected_output5 = [None, 1]
run_test(commands5, inputs5, expected_output5)

# Test case 6
commands6 = ["WordFilter", "f"]
inputs6 = [[["apple", "banana"]], ["x", "y"]]
expected_output6 = [None, -1]
run_test(commands6, inputs6, expected_output6)

# Test case 7
commands7 = ["WordFilter", "f"]
inputs7 = [[["apple", "apple"]], ["ap", "le"]]
expected_output7 = [None, 1]
run_test(commands7, inputs7, expected_output7)

# Test case 8 - more complex example
commands8 = ["WordFilter", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f"]
inputs8 = [[["cabaabaaaa","ccbcababac","bacbcabbca","bacbaabbab","bccbacbcba","cabccbacbc","bccbacbbca","bacbcabbca","cababbacbc","bacbababac","bccbababca","cabccbacac","bacbacabca","cbcbcbabaa","cbcbababbc"]], ["bccbacbcba", "a"], ["ab", "abc"], ["bac", "cab"], ["bacbc", "ca"], ["ba", "bcabbca"], ["bac", "abbca"], ["bacbcabbca", "bcabbca"], ["a", "aa"], ["cabaaba", "abaaaa"], ["cabaabaa", "aaaa"]]
expected_output8 = [None, 4, -1, -1, 7, 7, 7, 7, -1, 0, 0]
run_test(commands8, inputs8, expected_output8)