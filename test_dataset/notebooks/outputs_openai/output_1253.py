def reconstructMatrix(upper, lower, colsum):
    n = len(colsum)
    A0 = [0]*n
    A1 = [0]*n
    for i in range(n):
        if colsum[i] == 2:
            A0[i] = 1
            A1[i] = 1
            upper -= 1
            lower -= 1
    for i in range(n):
        if colsum[i] == 1:
            if upper > 0:
                A0[i] = 1
                upper -= 1
            else:
                A1[i] = 1
                lower -= 1
    if upper == 0 and lower == 0:
        return [A0, A1]
    else:
        return []

test_cases = [
    (2, 1, [1,1,1], [[1,1,0], [0,0,1]]),
    (2, 3, [2,2,1,1], []),
    (5, 5, [2,1,2,0,1,0,1,2,0,1], [[1,1,1,0,1,0,0,1,0,0], [1,0,1,0,0,0,1,1,0,1]])
]

correct = 0
total = len(test_cases)

for upper, lower, colsum, expected in test_cases:
    output = reconstructMatrix(upper, lower, colsum)
    if output == expected:
        print('True')
        correct += 1
    else:
        print('False')

print(f"{correct}/{total}")