def largestMerge(word1: str, word2: str) -> str:
    """
    You are given two strings word1 and word2. You want to construct a string merge in the following way: while either word1 or word2 are non-empty, choose one of the following options:
    If word1 is non-empty, append the first character in word1 to merge and delete it from word1.

    For example, if word1 = "abc" and merge = "dv", then after choosing this operation, word1 = "bc" and merge = "dva".

    If word2 is non-empty, append the first character in word2 to merge and delete it from word2.

    For example, if word2 = "abc" and merge = "", then after choosing this operation, word2 = "bc" and merge = "a".

    Return the lexicographically largest merge you can construct.

    A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b. For example, "abcd" is lexicographically larger than "abcc" because the first position they differ is at the fourth character, and d is greater than c.
    """
    merge = ""
    i, j = 0, 0
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
        (("cabaa", "bcaaa"), "cbcabaaaaa"),
        (("abcabc", "abdcaba"), "abdcabcabcaba"),
        (("abc", "def"), "abcdef"),
        (("aba", "ab"), "abaab"),
        (("a", "b"), "ba"),
        (("b", "a"), "ba"),
        (("leetcode", "java"), "leetcodejava"),
        (("uabwdyuh", "uabwdyuh"), "uabwdyuhuabwdyuh")
    ]
    
    num_correct = 0
    total_tests = len(test_cases)

    for (word1, word2), expected in test_cases:
        result = largestMerge(word1, word2)
        if result == expected:
            print("True")
            num_correct += 1
        else:
            print("False")
    
    print(f"{num_correct}/{total_tests}")
    
test_largestMerge()