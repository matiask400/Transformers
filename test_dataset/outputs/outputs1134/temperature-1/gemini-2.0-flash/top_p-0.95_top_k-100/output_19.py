def min_length(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            break
        
        char = s[l]
        
        l_new = l
        while l_new <= r and s[l_new] == char:
            l_new += 1
            
        r_new = r
        while r_new >= l and s[r_new] == char:
            r_new -= 1
            
        if l_new > r_new:
            return 0
        
        l, r = l_new, r_new
    
    return r - l + 1

def test_min_length():
    test_cases = [
        ("ca", 2),
        ("cabaabac", 0),
        ("aabccabba", 3),
        ("a", 1),
        ("aa", 0),
        ("aaa", 0),
        ("abc", 3),
        ("aaaaabbbbb", 0),
        ("aaaaabbbbba", 1),
        ("aaaaabbbbbac", 3),
        ("aaaaabbbbacc", 5),
        ("aaaaabbbbaccc", 7),
        ("aaaaabbbbacccc", 9),
        ("aaaaabbbbaccccc", 11),
        ("cccccbaabaccccc", 5),
        ("c", 1),
        ("cc", 0),
        ("ccc", 0),
        ("abcd", 4),
        ("aacaacaa", 6)
    ]
    
    correct_count = 0
    for s, expected in test_cases:
        result = min_length(s)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Input: {s}, Expected: {expected}, Got: {result}")
            
    print(f"{correct_count}/{len(test_cases)}")

if __name__ == "__main__":
    test_min_length()