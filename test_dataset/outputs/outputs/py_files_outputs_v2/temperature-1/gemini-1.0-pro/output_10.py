if __name__ == '__main__':
    test_cases = [('aa', 'a', False), ('aa', 'a*', True), ('ab', '.*', True), ('aab', 'c*a*b', True), ('mississippi', 'mis*is*p*.', False)]

    for i, (s, p, expected_output) in enumerate(test_cases):
        actual_output = isMatch(s, p)
        print(f'Test Case {i + 1}: Input: s = "{s}", p = "{p}", Output: {actual_output}, Expected Output: {expected_output}, Result: {actual_output == expected_output}')

def isMatch(s, p):
    s_len, p_len = len(s), len(p)
    s_ptr, p_ptr = 0, 0
    while True:
        if s_ptr == s_len:
            if p_ptr == p_len:
                return True
            elif p_ptr < p_len and p[p_ptr] == '*':
                p_ptr += 1
                continue
            else:
                return False
        if p_ptr == p_len:
            return False
        elif p[p_ptr] == '.':
            s_ptr += 1
            p_ptr += 1
            continue
        elif p[p_ptr] == '*':
            if s_ptr < s_len and (s[s_ptr] == p[p_ptr - 1] or p[p_ptr - 1] == '.'):
                s_ptr += 1
                continue
            elif p_ptr - 2 >= 0 and p[p_ptr - 2] == '*':
                p_ptr -= 1
                continue
            else:
                return False
        elif s[s_ptr] == p[p_ptr]:
            s_ptr += 1
            p_ptr += 1
            continue
        else:
            return False
    return False