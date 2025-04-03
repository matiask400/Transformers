class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_bst(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    for i in range(1, len(nodes)):
        insert_bst(root, nodes[i])
    return root

def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        if root.left:
            insert_bst(root.left, val)
        else:
            root.left = TreeNode(val)
    else:
        if root.right:
            insert_bst(root.right, val)
        else:
            root.right = TreeNode(val)

def closestKValues(root, target, k):
    values = []
    def inorder_traversal(node):
        if not node:
            return
        inorder_traversal(node.left)
        values.append(node.val)
        inorder_traversal(node.right)
    inorder_traversal(root)
    values.sort(key=lambda x: abs(x - target))
    return values[:k]

def run_tests():
    test_cases = [
        {
            "root": [4, 2, 5, 1, 3],
            "target": 3.714286,
            "k": 2,
            "expected": [4, 3]
        },
        {
            "root": [1],
            "target": 0.000000,
            "k": 1,
            "expected": [1]
        },
        {
            "root": [4,2,5,1,3],
            "target": 3,
            "k": 2,
            "expected": [3, 2]
        },
        {
            "root": [4,2,5,1,3],
            "target": 6,
            "k": 2,
            "expected": [5, 4]
        },
        {
            "root": [4,2,5,1,3],
            "target": 0,
            "k": 2,
            "expected": [1, 2]
        },
        {
            "root": [10,5,15,3,7,12,18],
            "target": 11,
            "k": 3,
            "expected": [10, 12, 15]
        },
        {
            "root": [10,5,15,3,7,12,18],
            "target": 16,
            "k": 3,
            "expected": [15, 18, 12]
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test in enumerate(test_cases):
        root_nodes = test["root"]
        target = test["target"]
        k = test["k"]
        expected = sorted(test["expected"])

        root_bst = build_bst(root_nodes)
        actual = sorted(closestKValues(root_bst, target, k))

        if actual == expected:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: root={root_nodes}, target={target}, k={k}")
            print(f"  Expected: {expected}")
            print(f"  Actual:   {actual}")

    print(f"\nCorrect tests: {correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()