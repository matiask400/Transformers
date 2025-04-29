def run_tests():
    test_cases = [
        # (graph, expected_output)
        ([[1,1,0],[0,1,0],[1,1,1]], 1),
        ([[1,0,1],[1,1,0],[0,1,1]], -1),
        ([[1,0],[0,1]], -1),
        ([[1,0,0],[0,1,0],[0,0,1]], -1),
        ([[1,0,1,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], -1),
        ([[1,0,0],[0,1,0],[0,0,1]], -1),
        ([[1,1,1],[0,1,1],[0,0,1]], -1),
        ([[1,0,0],[0,1,0],[0,0,1],[0,0,0]], 3),
        ([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], -1),
        ([[1,0,0,0],[0,1,0,0],[0,0,1,0],[1,1,1,1]], -1),
    ]
    
    correct = 0
    total = len(test_cases)
    
    for graph, expected in test_cases:
        class CelebrityFinder:
            def __init__(self, graph):
                self.graph = graph
                self.n = len(graph)
                self.calls = 0  # To count the number of knows calls if needed

            def knows(self, a, b):
                self.calls += 1
                return self.graph[a][b] == 1

            def findCelebrity(self):
                n = self.n
                candidate = 0
                for i in range(1, n):
                    if self.knows(candidate, i):
                        candidate = i
                for i in range(n):
                    if i != candidate:
                        if self.knows(candidate, i) or not self.knows(i, candidate):
                            return -1
                return candidate
        
        finder = CelebrityFinder(graph)
        result = finder.findCelebrity()
        if result == expected:
            print(True)
            correct += 1
        else:
            print(False)
    
    print(f"{correct}/{total}")

run_tests()