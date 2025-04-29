def magicalString(n):
    if n == 0:
        return 0
    if n <= 3:
        return 1
    s = [1, 2, 2]
    head = 2
    tail = 3
    num_ones = 1
    while tail < n:
        for i in range(s[head]):
            if s[tail - 1] == 1:
                s.append(2)
            else:
                s.append(1)
            if tail < n and s[tail] == 1:
                num_ones += 1
            tail += 1
        head += 1
    return num_ones

def test_magicalString():
    test_cases = [
        (6, 3),
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 2),
        (7, 4),
        (8, 4),
        (9, 4),
        (10, 5),
        (11, 6),
        (12, 6)
    ]
    
    correct_count = 0
    total_count = len(test_cases)
    
    for input_n, expected_output in test_cases:
        actual_output = magicalString(input_n)
        if actual_output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")
    
    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_magicalString()