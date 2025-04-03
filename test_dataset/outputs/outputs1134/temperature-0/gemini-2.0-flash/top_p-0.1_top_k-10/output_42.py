def possible_bipartition(N, dislikes):
    """
    Given a set of `N` people (numbered `1, 2, ..., N`), we would like to split everyone into two groups of any size.

    Each person may dislike some other people, and they should not go into the same group. 
    Formally, if `dislikes[i] = [a, b]`, it means it is not allowed to put the people numbered `a` and `b` into the same group.

    Return `true` if and only if it is possible to split everyone into two groups in this way.
    """
    graph = [[] for _ in range(N)]
    for u, v in dislikes:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    color = [0] * N  # 0: uncolored, 1: group 1, -1: group 2

    def dfs(node, c):
        color[node] = c
        for neighbor in graph[node]:
            if color[neighbor] == 0:
                if not dfs(neighbor, -c):
                    return False
            elif color[neighbor] == c:
                return False
        return True

    for i in range(N):
        if color[i] == 0:
            if not dfs(i, 1):
                return False

    return True

def test_possible_bipartition():
    test_cases = [
        (4, [[1,2],[1,3],[2,4]], True),
        (3, [[1,2],[1,3],[2,3]], False),
        (5, [[1,2],[2,3],[3,4],[4,5],[1,5]], False),
        (1, [], True),
        (2, [[1,2]], True),
        (2, [], True),
        (10, [[1,2],[3,4],[5,6],[7,8],[9,10]], True),
        (4, [[1,2],[3,4]], True),
        (5, [[1,2],[3,4],[1,5]], True),
        (5, [[1,2],[2,3],[3,4],[4,5]], True)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for N, dislikes, expected in test_cases:
        result = possible_bipartition(N, dislikes)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_possible_bipartition()