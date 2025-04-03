def solve():
    def get_moments_all_blue(light):
        n = len(light)
        turned_on_bulbs = set()
        count = 0
        max_bulb_on = 0
        for bulb_index in light:
            turned_on_bulbs.add(bulb_index)
            max_bulb_on = max(max_bulb_on, bulb_index)
            if len(turned_on_bulbs) == max_bulb_on:
                count += 1
        return count

    test_cases = [
        ([2, 1, 3, 5, 4], 3),
        ([3, 2, 4, 1, 5], 2),
        ([4, 1, 2, 3], 1),
        ([2, 1, 4, 3, 6, 5], 3),
        ([1, 2, 3, 4, 5, 6], 6),
    ]

    num_correct_tests = 0
    total_tests = len(test_cases)

    for i, (light, expected_output) in enumerate(test_cases):
        actual_output = get_moments_all_blue(light)
        if actual_output == expected_output:
            print(True)
            num_correct_tests += 1
        else:
            print(False)

    print(f"{num_correct_tests}/{total_tests}")

if __name__ == '__main__':
    solve()