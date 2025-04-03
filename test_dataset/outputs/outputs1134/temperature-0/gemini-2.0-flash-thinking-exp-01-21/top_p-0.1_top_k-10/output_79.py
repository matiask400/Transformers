def solve():
    def get_lexicographically_smallest_string(n, k):
        res = ['a'] * n
        diff = k - n
        for i in range(n - 1, -1, -1):
            if diff == 0:
                break
            add = min(diff, 25)
            res[i] = chr(ord('a') + add)
            diff -= add
        return "".join(res)

    def test_get_lexicographically_smallest_string():
        test_cases = [
            ((3, 27), "aay"),
            ((5, 73), "aaszz"),
            ((1, 1), "a"),
            ((2, 2), "aa"),
            ((2, 26 + 1), "az"),
            ((3, 26 * 3), "zzz"),
            ((4, 4), "aaaa"),
            ((4, 104), "zzzz"),
            ((4, 5), "aaab"),
            ((4, 6), "aaac"),
            ((4, 7), "aaad"),
            ((4, 29), "aaaz"),
            ((4, 30), "aabz"),
            ((4, 52), "aazz"),
            ((4, 53), "abzz"),
            ((4, 78), "azzz"),
            ((4, 79), "bzzz"),
            ((4, 100), "xyzz"),
            ((4, 101), "yzzz"),
            ((4, 102), "yzzz"),
            ((4, 103), "yzzz"),
            ((4, 104), "zzzz"),
            ((10, 260), "zzzzzzzzzz"),
            ((10, 10), "aaaaaaaaaa"),
            ((10, 11), "aaaaaaaaab"),
            ((10, 35), "aaaaaaaaaz"),
            ((10, 36), "aaaaaaaabz"),
            ((10, 50), "aaaaaaaazz"),
            ((10, 100), "aaaaaaaczz"),
            ((10, 150), "aaaaaaezzz"),
            ((10, 200), "aaaaaizzzz"),
            ((10, 250), "aaaazzzzzz"),
            ((10, 259), "aaazzzzzzy"),
            ((10, 260), "zzzzzzzzzz"),
        ]

        correct_count = 0
        for i, ((n, k), expected_output) in enumerate(test_cases):
            actual_output = get_lexicographically_smallest_string(n, k)
            if actual_output == expected_output:
                print(f"Test {i+1}: True")
                correct_count += 1
            else:
                print(f"Test {i+1}: False")
        print(f"{correct_count}/{len(test_cases)}")

    test_get_lexicographically_smallest_string()

solve()