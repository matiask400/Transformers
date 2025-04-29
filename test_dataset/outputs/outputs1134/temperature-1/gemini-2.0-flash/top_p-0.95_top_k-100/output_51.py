def solve():
    def zeros(x):
        if x == 0:
            return 0
        count = 0
        i = 5
        while x // i >= 1:
            count += x // i
            i *= 5
        return count

    def count_x(k):
        low = 0
        high = 5 * (k + 1)  # Upper bound, since f(5*(k+1)) > k
        while low <= high:
            mid = (low + high) // 2
            z = zeros(mid)
            if z < k:
                low = mid + 1
            elif z > k:
                high = mid - 1
            else:
                # Find the start of the range
                start = mid
                high_temp = mid - 1
                while low <= high_temp:
                    mid_temp = (low + high_temp) // 2
                    z_temp = zeros(mid_temp)
                    if z_temp < k:
                        low = mid_temp + 1
                    else:
                        start = mid_temp
                        high_temp = mid_temp - 1

                # Find the end of the range
                end = mid
                low_temp = mid + 1
                high = 5 * (k + 1)
                while low_temp <= high:
                    mid_temp = (low_temp + high) // 2
                    z_temp = zeros(mid_temp)
                    if z_temp > k:
                        high = mid_temp - 1
                    else:
                        end = mid_temp
                        low_temp = mid_temp + 1

                return end - start + 1
        return 0

    def test_cases():
        tests = [
            (0, 5),
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0),
            (5, 0),
            (6, 5),
            (7, 0),
            (8, 0),
            (9, 0),
            (10, 0),
            (11, 0),
            (12, 0),
            (13, 0),
            (14, 0),
            (15, 0),
            (16, 0),
            (17, 0),
            (18, 0),
            (19, 0),
            (20, 0),
            (21, 0),
            (22, 0),
            (23, 0),
            (24, 0),
            (25, 0),
            (26, 5),
            (27, 0),
            (28, 0),
            (29, 0),
            (30, 0),
            (31, 0),
        ]
        
        correct = 0
        total = len(tests)

        for k, expected in tests:
            result = count_x(k)
            if result == expected:
                print("True")
                correct += 1
            else:
                print("False")
        
        print(f"{correct}/{total}")

    test_cases()

solve()