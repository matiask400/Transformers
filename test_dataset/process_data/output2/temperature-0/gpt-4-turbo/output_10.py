def is_match(s, p):
    import re
    pattern = re.compile(p)
    match = pattern.fullmatch(s)
    return bool(match)

# Test cases
print(is_match('aa', 'a') == False)  # Output: True
print(is_match('aa', 'a*') == True)  # Output: True
print(is_match('ab', '.*') == True)  # Output: True