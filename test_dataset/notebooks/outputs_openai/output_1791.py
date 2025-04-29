def findCenter(edges):
    # Extract the first two edges
    a, b = edges[0]
    c, d = edges[1]
    # Check which node is common
    if a == c or a == d:
        return a
    return b

def run_tests():
    test_cases = [
        {
            "edges": [[1,2],[2,3],[4,2]],
            "expected": 2
        },
        {
            "edges": [[1,2],[5,1],[1,3],[1,4]],
            "expected": 1
        },
        {
            "edges": [[10,20],[20,30],[40,20],[20,50]],
            "expected": 20
        },
        {
            "edges": [[7,8],[8,9],[8,10],[8,11]],
            "expected": 8
        },
        {
            "edges": [[3,1],[3,2]],
            "expected": 3
        },
        {
            "edges": [[100000,1],[100000,2],[100000,3]],
            "expected": 100000
        },
        {
            "edges": [[4,5],[5,6],[5,7],[5,8],[5,9]],
            "expected": 5
        },
        {
            "edges": [[2,1],[2,3],[2,4],[2,5],[2,6],[2,7]],
            "expected": 2
        },
        {
            "edges": [[1,2],[1,3],[1,4]],
            "expected": 1
        },
        {
            "edges": [[6,4],[6,1],[6,5]],
            "expected": 6
        }
    ]
    
    correct = 0
    total = len(test_cases)
    for idx, test in enumerate(test_cases):
        result = findCenter(test["edges"])
        if result == test["expected"]:
            print(True)
            correct += 1
        else:
            print(False)
    print(f"{correct}/{total}")

if __name__ == "__main__":
    run_tests()