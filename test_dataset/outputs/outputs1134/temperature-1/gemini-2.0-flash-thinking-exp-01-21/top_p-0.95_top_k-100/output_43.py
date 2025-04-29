def solve():
    def get_blue_moment_count(light):
        n = len(light)
        bulbs_on_count = 0
        blue_moments = 0
        max_bulb_on = 0
        for k in range(n):
            bulb_index_to_turn_on = light[k]
            bulbs_on_count += 1
            max_bulb_on = max(max_bulb_on, bulb_index_to_turn_on)
            if bulbs_on_count == max_bulb_on:
                blue_moments += 1
        return blue_moments

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
        actual_output = get_blue_moment_count(light)
        if actual_output == expected_output:
            print(True)
            num_correct_tests += 1
        else:
            print(False)

    print(f"{num_correct_tests}/{total_tests}")

if __name__ == '__main__':
    solve()