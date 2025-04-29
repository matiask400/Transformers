def solve():
    def get_min_length(s):
        s_list = list(s)
        while True:
            if not s_list:
                return 0
            if len(s_list) <= 1:
                return len(s_list)

            prefix_char = s_list[0]
            prefix_end = 0
            for i in range(len(s_list)):
                if s_list[i] == prefix_char:
                    prefix_end += 1
                else:
                    break

            suffix_char = s_list[-1]
            suffix_start = len(s_list)
            for i in range(len(s_list) - 1, -1, -1):
                if s_list[i] == suffix_char:
                    suffix_start -= 1
                else:
                    break

            if prefix_char == suffix_char and prefix_end + (len(s_list) - suffix_start) <= len(s_list):
                if prefix_end <= suffix_start: # no intersection or just touch
                    s_list = s_list[prefix_end:suffix_start]
                else:
                    break
            else:
                break
        return len(s_list)

    test_cases = [
        ("ca", 2),
        ("cabaabac", 0),
        ("aabccabba", 3),
        ("a", 1),
        ("", 0),
        ("aaa", 1),
        ("bbb", 1),
        ("ccc", 1),
        ("aaabbbccc", 3),
        ("aabbcc", 2),
        ("abc", 3),
        ("aaaaa", 1),
        ("bbbbb", 1),
        ("ccccc", 1),
        ("abababa", 7),
        ("abcabcabc", 9),
        ("cccaaa", 4),
        ("aaaccc", 4),
        ("aabbbaa", 3),
        ("aabbbbaaa", 0),
        ("aabbbbcccaaa", 0),
        ("aabbbbcccdddaaa", 7),
        ("aabbbbcccddddeeeaaa", 10),
        ("aabbbbcccddddeeefffaaa", 13),
        ("aabbbbcccddddeeeffffgggaaa", 16),
        ("aabbbbcccddddeeeffffggghhhaaa", 19),
        ("aabbbbcccddddeeeffffggghhhiiiaaa", 22),
        ("aabbbbcccddddeeeffffggghhhiiiijjjaaa", 25),
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkaaa", 28),
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkklll", 30),
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmm", 33),
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnn", 36),
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnooo", 39),
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppp", 42),
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqq", 45),
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrr", 48),
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrsss", 51),
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrsssttt", 54),
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuu", 57),
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvv", 60),
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwww", 63),
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxx", 66),
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyy", 69),
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz", 72),
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111", 75), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222", 78), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333", 81), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444", 84), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555", 87), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666", 90), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666777", 93), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666777888", 96), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666777888999", 99), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666777888999000", 102), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666777888999000aaa", 102), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666777888999000aaabbbccc", 102), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666777888999000aaabbbcccabc", 105), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666777888999000aaabbbcccabca", 105), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666777888999000aaabbbcccabcab", 105), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666777888999000aaabbbcccabcabc", 105), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666777888999000aaabbbcccabcabcabc", 105), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666777888999000aaabbbcccabcabcabca", 105), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666777888999000aaabbbcccabcabcabcab", 105), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666777888999000aaabbbcccabcabcabcabc", 105), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666777888999000aaabbbcccabcabcabcabca", 105), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666777888999000aaabbbcccabcabcabcabcab", 105), # should only consider a,b,c
        ("aabbbbcccddddeeeffffggghhhiiiijjjkkkllllmmmmnnnoooppppqqqrrrssstttuuuvvvwwwwxxxyyyzzz111222333444555666777888999000aaabbbcccabcabcabcabcabc", 105), # should only consider a,b,c
    ]

    correct_count = 0
    for input_str, expected_output in test_cases:
        output = get_min_length(input_str)
        if output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")
    print(f"{correct_count}/{len(test_cases)}")

solve()