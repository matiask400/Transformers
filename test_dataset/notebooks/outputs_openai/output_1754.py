def largest_merge(word1, word2):
    merge = []
    i, j = 0, 0
    while i < len(word1) or j < len(word2):
        if word1[i:] > word2[j:]:
            merge.append(word1[i])
            i += 1
        else:
            merge.append(word2[j])
            j += 1
    return ''.join(merge)

def run_tests():
    test_cases = [
        {
            "word1": "cabaa",
            "word2": "bcaaa",
            "expected": "cbcabaaaaa"
        },
        {
            "word1": "abcabc",
            "word2": "abdcaba",
            "expected": "abdcabcabcaba"
        },
        {
            "word1": "abc",
            "word2": "abdcaba",
            "expected": "abdcababc"
        },
        {
            "word1": "aaa",
            "word2": "aaa",
            "expected": "aaaaaa"
        },
        {
            "word1": "abcde",
            "word2": "fghij",
            "expected": "fghijabcde"
        },
        {
            "word1": "zxabc",
            "word2": "zxabd",
            "expected": "zxzxabdabc"
        },
        {
            "word1": "gattaca",
            "word2": "gattaca",
            "expected": "gattacagattaca"
        },
        {
            "word1": "abc",
            "word2": "xyz",
            "expected": "xyzabc"
        },
        {
            "word1": "mnop",
            "word2": "mnop",
            "expected": "mnopmnop"
        },
        {
            "word1": "kmt",
            "word2": "kmtk",
            "expected": "kmtkmtk"
        }
    ]
    
    correct = 0
    total = len(test_cases)
    
    for idx, test in enumerate(test_cases):
        word1 = test["word1"]
        word2 = test["word2"]
        expected = test["expected"]
        result = largest_merge(word1, word2)
        if result == expected:
            print("True")
            correct += 1
        else:
            print("False")
    
    print(f"{correct}/{total}")

# Run the tests
run_tests()