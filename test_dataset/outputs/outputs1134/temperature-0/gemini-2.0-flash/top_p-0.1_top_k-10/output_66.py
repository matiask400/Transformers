def solve():
    def num_jewels_in_stones(jewels, stones):
        jewels_set = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewels_set:
                count += 1
        return count

    def test_cases():
        test_data = [
            (("aA", "aAAbbbb"), 3),
            (("z", "ZZ"), 0),
            (("abc", "aabbcc"), 6),
            (("ABC", "abc"), 0),
            (("", "abc"), 0),
            (("abc", ""), 0),
            (("a", "a"), 1),
            (("a", "b"), 0),
            (("A", "aAAbbbb"), 1),
            (("aA", "a"), 1)
        ]

        correct_count = 0
        total_count = len(test_data)

        for i, ((jewels, stones), expected) in enumerate(test_data):
            result = num_jewels_in_stones(jewels, stones)
            if result == expected:
                print(f"Test {i+1}: True")
                correct_count += 1
            else:
                print(f"Test {i+1}: False (Expected: {expected}, Got: {result})")

        print(f"{correct_count}/{total_count}")

    test_cases()

solve()