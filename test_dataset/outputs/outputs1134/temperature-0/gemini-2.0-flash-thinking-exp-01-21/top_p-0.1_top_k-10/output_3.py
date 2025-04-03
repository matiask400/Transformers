def solve():
    def largest_merge(word1: str, word2: str) -> str:
        merge = ""
        i = 0
        j = 0
        while i < len(word1) or j < len(word2):
            if i < len(word1) and j < len(word2):
                if word1[i] > word2[j]:
                    merge += word1[i]
                    i += 1
                elif word2[j] > word1[i]:
                    merge += word2[j]
                    j += 1
                else: # word1[i] == word2[j]
                    if word1[i+1:] > word2[j+1:]:
                        merge += word1[i]
                        i += 1
                    elif word2[j+1:] > word1[i+1:]:
                        merge += word2[j]
                        j += 1
                    else: # word1[i+1:] == word2[j+1:] or both are empty
                        merge += word1[i]
                        i += 1
            elif i < len(word1):
                merge += word1[i]
                i += 1
            elif j < len(word2):
                merge += word2[j]
                j += 1
        return merge

    test_cases = [
        (("cabaa", "bcaaa"), "cbcabaaaaa"),
        (("abcabc", "abdcaba"), "abdcabcabcaba"),
        (("", ""), ""),
        (("abc", ""), "abc"),
        (("", "def"), "def"),
        (("a", "b"), "ba"),
        (("b", "a"), "ba"),
        (("apple", "banana"), "bananaapple"),
        (("leetcode", "coding"), "leetcodecoding"),
        (("z", "a"), "za"),
        (("a", "z"), "za"),
        (("aba", "baa"), "baabaa"),
        (("g", "g"), "gg"),
        (("uux", "uuy"), "uuyuux"),
        (("mmr", "mmr"), "mmrmmr"),
        (("parker", "morris"), "parkermorris"),
        (("uux", "uuy"), "uuyuux"),
        (("uux", "uux"), "uuxuux"),
        (("uux", "uuz"), "uuzuux"),
        (("uuz", "uux"), "uuzuux"),
    ]

    num_correct = 0
    for i, ((word1, word2), expected_output) in enumerate(test_cases):
        actual_output = largest_merge(word1, word2)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: word1='{word1}', word2='{word2}'")
            print(f"  Expected Output: '{expected_output}'")
            print(f"  Actual Output:   '{actual_output}'")

    print(f"\n{num_correct} correct out of {len(test_cases)}")

solve()