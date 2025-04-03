def solve():
    def max_four_person_groups(n, reservedSeats):
        reserved = {}
        for row, seat in reservedSeats:
            if row not in reserved:
                reserved[row] = set()
            reserved[row].add(seat)

        count = 0
        for row in range(1, n + 1):
            available = True
            if row in reserved:
                seats = reserved[row]
                
                # Check for groups in the range 2-5
                if 2 not in seats and 3 not in seats and 4 not in seats and 5 not in seats:
                    count += 1
                    available = False
                
                # Check for groups in the range 6-9
                if 6 not in seats and 7 not in seats and 8 not in seats and 9 not in seats:
                    count += 1
                    available = False
                    
                # Check for groups split by the aisle (4-7)
                if available and 4 not in seats and 5 not in seats and 6 not in seats and 7 not in seats:
                    count += 1
            else:
                count += 2

        return count
    
    test_cases = [
        (3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]], 4),
        (2, [[2,1],[1,8],[2,6]], 2),
        (4, [[4,3],[1,4],[4,6],[1,7]], 4),
        (1, [], 2),
        (1, [[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9]], 0),
        (5, [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],
            [2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[2,9],[2,10],
            [3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],[3,9],[3,10],
            [4,1],[4,2],[4,3],[4,4],[4,5],[4,6],[4,7],[4,8],[4,9],[4,10],
            [5,1],[5,2],[5,3],[5,4],[5,5],[5,6],[5,7],[5,8],[5,9],[5,10]],0),
        (4, [[1,5],[2,3],[3,8],[4,10]], 6)
    ]
    
    correct_count = 0
    total_count = len(test_cases)
    
    for n, reservedSeats, expected in test_cases:
        result = max_four_person_groups(n, reservedSeats)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
    
    print(f"{correct_count}/{total_count}")
    
solve()