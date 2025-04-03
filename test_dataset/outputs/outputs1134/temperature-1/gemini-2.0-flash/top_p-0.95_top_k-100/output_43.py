def num_times_all_blue(light):
    """
    Given a list of bulbs that are turned on, return the number of moments in which all turned on bulbs are blue.
    A bulb change color to blue only if it is on and all the previous bulbs (to the left) are turned on too.
    """
    n = len(light)
    rightmost = 0
    count = 0
    max_light = 0

    for i in range(n):
        max_light = max(max_light, light[i])
        if max_light == i + 1:
            count += 1

    return count

def test_num_times_all_blue():
    test_cases = [
        ([2, 1, 3, 5, 4], 3),
        ([3, 2, 4, 1, 5], 2),
        ([4, 1, 2, 3], 1),
        ([2, 1, 4, 3, 6, 5], 3),
        ([1, 2, 3, 4, 5, 6], 6),
        ([5, 4, 3, 2, 1], 1),
        ([1], 1),
        ([2,1], 1),
        ([1,2], 2)
    ]
    
    correct_count = 0
    total_count = len(test_cases)

    for i, (light, expected) in enumerate(test_cases):
        result = num_times_all_blue(light)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Got: {result})")

    print(f"\n{correct_count}/{total_count}")

if __name__ == '__main__':
    test_num_times_all_blue()