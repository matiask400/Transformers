s = 'abcabcbb'
print(length_of_longest_substring(s) == 3)
s = 'bbbbb'
print(length_of_longest_substring(s) == 1)
s = 'pwwkew'
print(length_of_longest_substring(s) == 3)
s = ''
print(length_of_longest_substring(s) == 0)

def length_of_longest_substring(s: str) -> int:
    if not s:  
        return 0
    char_idx_map = dict()      
    max_length = start = 0
    n= len(s)
    for end in range(n): 
        c = s[end]
        if c in char_idx_map:
            if char_idx_map[c] >= start: 
                start = char_idx_map[c] + 1
        char_idx_map[c] = end
        max_length = max(max_length, end - start + 1)
    return max_length