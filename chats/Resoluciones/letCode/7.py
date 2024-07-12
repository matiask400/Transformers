def strongPasswordChecker(password: str) -> int:
    n = len(password)
    
    has_lower = any('a' <= c <= 'z' for c in password)
    has_upper = any('A' <= c <= 'Z' for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    missing_types = 3 - (has_lower + has_upper + has_digit)
    
    replace = 0
    oned = twod = 0
    i = 2
    
    while i < n:
        if password[i] == password[i - 1] == password[i - 2]:
            length = 2
            while i < n and password[i] == password[i - 1]:
                length += 1
                i += 1
            
            replace += length // 3
            if length % 3 == 0:
                oned += 1
            elif length % 3 == 1:
                twod += 1
        else:
            i += 1
    
    if n < 6:
        return max(missing_types, 6 - n)
    
    elif n <= 20:
        return max(missing_types, replace)
    
    else:
        delete = n - 20
        
        replace -= min(delete, oned * 1) // 1
        replace -= min(max(delete - oned, 0), twod * 2) // 2
        replace -= max(delete - oned - 2 * twod, 0) // 3
        
        return delete + max(missing_types, replace)

# Example usage
password = "a"
print(strongPasswordChecker(password))  # Output should be the minimum number of steps required
