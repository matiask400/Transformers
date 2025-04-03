def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def assign_bikes(workers, bikes):
    n = len(workers)
    m = len(bikes)
    dist_list = []
    for i in range(n):
        for j in range(m):
            dist = manhattan_distance(workers[i], bikes[j])
            dist_list.append((dist, i, j))

    dist_list.sort()

    ans = [0] * n
    worker_assigned = [False] * n
    bike_assigned = [False] * m

    for dist, worker_index, bike_index in dist_list:
        if not worker_assigned[worker_index] and not bike_assigned[bike_index]:
            ans[worker_index] = bike_index
            worker_assigned[worker_index] = True
            bike_assigned[bike_index] = True

    return ans

def test_assign_bikes(workers, bikes, expected_output):
    output = assign_bikes(workers, bikes)
    if output == expected_output:
        print("True")
        return True
    else:
        print("False")
        return False

if __name__ == '__main__':
    correct_tests = 0
    total_tests = 0

    workers1 = [[0,0],[2,1]]
    bikes1 = [[1,2],[3,3]]
    expected_output1 = [1,0]
    total_tests += 1
    if test_assign_bikes(workers1, bikes1, expected_output1):
        correct_tests += 1

    workers2 = [[0,0],[1,1],[2,0]]
    bikes2 = [[1,0],[2,2],[2,1]]
    expected_output2 = [0,2,1]
    total_tests += 1
    if test_assign_bikes(workers2, bikes2, expected_output2):
        correct_tests += 1

    workers3 = [[0,0]]
    bikes3 = [[1,0]]
    expected_output3 = [0]
    total_tests += 1
    if test_assign_bikes(workers3, bikes3, expected_output3):
        correct_tests += 1

    workers4 = [[0,0],[0,1]]
    bikes4 = [[0,2],[0,3]]
    expected_output4 = [0,1]
    total_tests += 1
    if test_assign_bikes(workers4, bikes4, expected_output4):
        correct_tests += 1

    workers5 = [[0,0],[10,10]]
    bikes5 = [[9,9],[11,11]]
    expected_output5 = [0,1]
    total_tests += 1
    if test_assign_bikes(workers5, bikes5, expected_output5):
        correct_tests += 1

    print(f"{correct_tests}/{total_tests}")