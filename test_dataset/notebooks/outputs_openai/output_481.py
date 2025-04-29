def count_ones_in_magic_string(N):
    if N == 0:
        return 0
    S = [1, 2, 2]
    if N <= len(S):
        return S[:N].count(1)
    pointer = 2
    current = 1
    count_of_1s = S[:N].count(1)
    while len(S) < N:
        num = S[pointer]
        for _ in range(num):
            if len(S) >= N:
                break
            S.append(current)
            if current == 1:
                count_of_1s += 1
        current = 3 - current
        pointer += 1
    return count_of_1s

def run_tests():
    test_cases = [
        (6, 3),
        (1, 1),
        (3, 1),
        (4, 2),
        (10, 5),
        (12, 5),
        (13, 6),
        (0, 0),
        (15, 7),
        (20, 9),
        (30, 14),
        (100, 44),
        (1000, 444),
        (100000, 66666),
    ]
    passed = 0
    for idx, (input_val, expected) in enumerate(test_cases):
        output = count_ones_in_magic_string(input_val)
        if output == expected:
            print("True")
            passed +=1
        else:
            print("False")
    print(f"{passed}/{len(test_cases)}")

run_tests()