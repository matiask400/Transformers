def findMinArrowShots(points):
    if not points:
        return 0
    points.sort(key=lambda x: x[1])
    arrows = 1
    current_end = points[0][1]
    for p in points[1:]:
        if p[0] > current_end:
            arrows += 1
            current_end = p[1]
    return arrows

# Define test cases as (input, expected_output)
test_cases = [
    ([[10,16],[2,8],[1,6],[7,12]], 2),
    ([[1,2],[3,4],[5,6],[7,8]], 4),
    ([[1,2],[2,3],[3,4],[4,5]], 2),
    ([], 0),
    ([[1,2]], 1),
    ([[-10,-8], [0,5], [6,10], [5,6]], 2),
    ([[1, 10], [2, 3], [4, 5], [6, 7], [8, 9]], 2),
    ([[1,2],[2,2],[2,3]],1),
    ([[1,5], [2,3], [3,4], [4,5]],1),
    ([[1,2147483647],[2,2147483647]],1)
]

correct = 0
total = len(test_cases)

for idx, (inp, expected) in enumerate(test_cases, 1):
    result = findMinArrowShots(inp)
    is_correct = result == expected
    print(is_correct)
    if is_correct:
        correct +=1

print(f"{correct}/{total}")