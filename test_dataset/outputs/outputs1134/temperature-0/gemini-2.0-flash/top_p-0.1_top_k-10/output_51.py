def solve():
    def trailing_zeros(x):
        count = 0
        i = 5
        while x // i >= 1:
            count += x // i
            i *= 5
        return count

    def count_x(K):
        count = 0
        x = 0
        while True:
            zeros = trailing_zeros(x)
            if zeros == K:
                count += 1
            elif zeros > K:
                break
            x += 1
            if x > 1000:
                break
        
        low = 0
        high = 5 * (K + 1)
        
        first = -1
        while low <= high:
            mid = (low + high) // 2
            zeros = trailing_zeros(mid)
            if zeros == K:
                first = mid
                high = mid - 1
            elif zeros < K:
                low = mid + 1
            else:
                high = mid - 1
        
        if first == -1:
            return 0
        
        low = 0
        high = 5 * (K + 1)
        
        last = -1
        while low <= high:
            mid = (low + high) // 2
            zeros = trailing_zeros(mid)
            if zeros == K:
                last = mid
                low = mid + 1
            elif zeros < K:
                low = mid + 1
            else:
                high = mid - 1
        
        return last - first + 1

    def test_cases():
        tests = [
            (0, 5),
            (1, 5),
            (2, 5),
            (3, 5),
            (4, 5),
            (5, 0),
            (6, 5),
            (7, 5),
            (8, 5),
            (9, 5),
            (10, 5),
            (11, 0),
            (12, 5),
            (13, 5),
            (14, 5),
            (15, 5),
            (16, 5),
            (17, 0),
            (18, 5),
            (19, 5),
            (20, 5),
            (21, 5),
            (22, 5),
            (23, 0),
            (24, 5),
            (25, 5),
            (26, 5),
            (27, 5),
            (28, 5),
            (29, 0),
            (30, 5),
            (31, 5),
            (32, 5),
            (33, 5),
            (34, 5),
            (35, 0),
            (36, 5),
            (37, 5),
            (38, 5),
            (39, 5),
            (40, 5),
            (41, 0),
            (42, 5),
            (43, 5),
            (44, 5),
            (45, 5),
            (46, 5),
            (47, 0),
            (48, 5),
            (49, 5),
            (50, 5),
            (51, 5),
            (52, 5),
            (53, 0),
            (54, 5),
            (55, 5),
            (56, 5),
            (57, 5),
            (58, 5),
            (59, 0),
            (60, 5),
            (61, 5),
            (62, 5),
            (63, 5),
            (64, 5),
            (65, 0),
            (66, 5),
            (67, 5),
            (68, 5),
            (69, 5),
            (70, 5),
            (71, 0),
            (72, 5),
            (73, 5),
            (74, 5),
            (75, 5),
            (76, 5),
            (77, 0),
            (78, 5),
            (79, 5),
            (80, 5),
            (81, 5),
            (82, 5),
            (83, 0),
            (84, 5),
            (85, 5),
            (86, 5),
            (87, 5),
            (88, 5),
            (89, 0),
            (90, 5),
            (91, 5),
            (92, 5),
            (93, 5),
            (94, 5),
            (95, 0),
            (96, 5),
            (97, 5),
            (98, 5),
            (99, 5),
            (100, 5)
        ]
        
        correct_count = 0
        total_tests = len(tests)
        
        for K, expected in tests:
            result = count_x(K)
            if result == expected:
                print("True")
                correct_count += 1
            else:
                print("False")
        
        print(f"{correct_count}/{total_tests}")

    test_cases()

solve()