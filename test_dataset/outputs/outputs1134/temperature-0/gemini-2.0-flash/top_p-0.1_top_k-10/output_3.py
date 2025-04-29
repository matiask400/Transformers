def largestMerge(word1: str, word2: str) -> str:
    """
    Given two strings word1 and word2. You want to construct a string merge in the following way: while either word1 or word2 are non-empty, choose one of the following options:
    If word1 is non-empty, append the first character in word1 to merge and delete it from word1.
    For example, if word1 = "abc" and merge = "dv", then after choosing this operation, word1 = "bc" and merge = "dva".
    If word2 is non-empty, append the first character in word2 to merge and delete it from word2.
    For example, if word2 = "abc" and merge = "", then after choosing this operation, word2 = "bc" and merge = "a".
    Return the lexicographically largest merge you can construct.
    A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b. For example, "abcd" is lexicographically larger than "abcc" because the first position they differ is at the fourth character, and d is greater than c.
    """
    merge = ""
    i = 0
    j = 0
    while i < len(word1) and j < len(word2):
        if word1[i:] > word2[j:]:
            merge += word1[i]
            i += 1
        else:
            merge += word2[j]
            j += 1
    merge += word1[i:]
    merge += word2[j:]
    return merge

def test_largestMerge():
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
            "word1": "aaaa",
            "word2": "aa",
            "expected": "aaaaaa"
        },
        {
            "word1": "a",
            "word2": "b",
            "expected": "ba"
        },
        {
            "word1": "b",
            "word2": "a",
            "expected": "ba"
        },
        {
            "word1": "",
            "word2": "abc",
            "expected": "abc"
        },
        {
            "word1": "abc",
            "word2": "",
            "expected": "abc"
        },
        {
            "word1": "gugu",
            "word2": "gugu",
            "expected": "gugugugu"
        }
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, test_case in enumerate(test_cases):
        word1 = test_case["word1"]
        word2 = test_case["word2"]
        expected = test_case["expected"]
        actual = largestMerge(word1, word2)

        if actual == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: word1 = {word1}, word2 = {word2}")
            print(f"  Expected: {expected}")
            print(f"  Actual: {actual}")

    print(f"\nCorrect: {correct_count}/{total_count}")

if __name__ == "__main__":
    test_largestMerge()