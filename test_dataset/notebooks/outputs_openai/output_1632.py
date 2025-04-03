from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

def matrixRankTransform(matrix):
    m, n = len(matrix), len(matrix[0])
    answer = [[0]*n for _ in range(m)]
    value_to_positions = defaultdict(list)
    for i in range(m):
        for j in range(n):
            value_to_positions[matrix[i][j]].append((i,j))
    rows = [0]*m
    cols = [0]*n
    for value in sorted(value_to_positions):
        uf = UnionFind()
        positions = value_to_positions[value]
        for i,j in positions:
            uf.union(i, ~j)
        groups = defaultdict(list)
        for i,j in positions:
            groups[uf.find(i)].append((i,j))
        rank_updates = {}
        for group in groups.values():
            max_rank = 0
            for i,j in group:
                max_rank = max(max_rank, rows[i], cols[j])
            for i,j in group:
                answer[i][j] = max_rank + 1
                rank_updates[i] = max(rank_updates.get(i, 0), max_rank + 1)
                rank_updates[~j] = max(rank_updates.get(~j, 0), max_rank + 1)
        for key, val in rank_updates.items():
            if key >=0:
                rows[key] = max(rows[key], val)
            else:
                cols[~key] = max(cols[~key], val)
    return answer

def run_tests():
    test_cases = [
        {
            "matrix": [[1,2],[3,4]],
            "expected": [[1,2],[2,3]]
        },
        {
            "matrix": [[7,7],[7,7]],
            "expected": [[1,1],[1,1]]
        },
        {
            "matrix": [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]],
            "expected": [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
        },
        {
            "matrix": [[7,3,6],[1,4,5],[9,8,2]],
            "expected": [[5,1,4],[1,2,3],[6,3,1]]
        }
    ]
    total = len(test_cases)
    correct = 0
    for test in test_cases:
        output = matrixRankTransform(test["matrix"])
        is_correct = output == test["expected"]
        print(is_correct)
        if is_correct:
            correct +=1
    print(f"{correct}/{total}")

if __name__ == "__main__":
    run_tests()