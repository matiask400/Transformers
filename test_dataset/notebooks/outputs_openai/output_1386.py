def maxNumberOfFamilies(n, reservedSeats):
    from collections import defaultdict
    reserved = defaultdict(set)
    for r, s in reservedSeats:
        reserved[r].add(s)
    
    total = 0
    for row in reserved:
        seats = reserved[row]
        # Check each possible block
        left = all(seat not in seats for seat in [2,3,4,5])
        right = all(seat not in seats for seat in [6,7,8,9])
        middle = all(seat not in seats for seat in [4,5,6,7])
        if left and right:
            total += 2
        elif left or right or middle:
            total +=1
    return total + 2*(n - len(reserved))

def run_tests():
    test_cases = [
        (3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]], 4),
        (2, [[2,1],[1,8],[2,6]], 2),
        (4, [[4,3],[1,4],[4,6],[1,7]], 4),
    ]
    correct = 0
    for n, reservedSeats, expected in test_cases:
        result = maxNumberOfFamilies(n, reservedSeats)
        if result == expected:
            print(True)
            correct +=1
        else:
            print(False)
    print(f"{correct}/{len(test_cases)}")

run_tests()