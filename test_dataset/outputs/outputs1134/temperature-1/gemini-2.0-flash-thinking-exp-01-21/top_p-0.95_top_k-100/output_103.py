class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closestKValues(root, target, k):
    def inorder_traversal(node, values):
        if not node:
            return
        inorder_traversal(node.left, values)
        values.append(node.val)
        inorder_traversal(node.right, values)

    values = []
    inorder_traversal(root, values)

    values.sort(key=lambda x: abs(x - target))

    return values[:k]

def build_bst(nodes):
    if not nodes:
        return None

    def insert(root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
        return root

    root = TreeNode(nodes[0])
    for i in range(1, len(nodes)):
        insert(root, nodes[i])
    return root

def run_tests():
    test_cases = [
        {
            "root": [4, 2, 5, 1, 3],
            "target": 3.714286,
            "k": 2,
            "expected_output": [4, 3]
        },
        {
            "root": [1],
            "target": 0.000000,
            "k": 1,
            "expected_output": [1]
        },
        {
            "root": [4, 2, 5, 1, 3],
            "target": 3,
            "k": 2,
            "expected_output": [3, 4]
        },
        {
            "root": [4, 2, 5, 1, 3],
            "target": 6,
            "k": 2,
            "expected_output": [5, 4]
        },
        {
            "root": [10, 5, 15, 3, 7, 13, 18, 1, None, 6],
            "target": 6.5,
            "k": 4,
            "expected_output": [7, 6, 5, 7] # or any order of these 4, like [5, 6, 7, 7] in case of duplicates, but there are no duplicates here in values, so [7, 6, 5, 3] or [5, 6, 7, 3] is correct. Actually [7, 6, 5, 7] is not right. It should be [7, 6, 5, 10] or [6, 7, 5, 10] or any permutation of these. Let's assume output order does not matter, just set of values must match. Actually, for input [10, 5, 15, 3, 7, 13, 18, 1, None, 6], target = 6.5, k=4, nodes are [1, 3, 5, 6, 7, 10, 13, 15, 18]. diff with 6.5: [5.5, 3.5, 1.5, 0.5, 0.5, 3.5, 6.5, 8.5, 11.5]. Sorted diff: [0.5, 0.5, 1.5, 3.5, 3.5, 5.5, 6.5, 8.5, 11.5]. Corresponding values [6, 7, 5, 3, 10, 1, 13, 15, 18]. First 4: [6, 7, 5, 3]. Let's check again.
            "expected_output": [6, 7, 5, 3]
        },
        {
            "root": [10, 5, 15, 3, 7, 13, 18, 1, None, 6],
            "target": 11,
            "k": 3,
            "expected_output": [10, 13, 7] # or [13, 10, 7] or any order. Diff with 11: [1, 4, 9, 8, 4, 2, 7, 10, None, 5]. Values: [1, 3, 5, 6, 7, 10, 13, 15, 18]. Diffs: [10, 8, 6, 5, 4, 1, 2, 4, 7]. Sorted Diffs: [1, 2, 4, 4, 5, 6, 7, 8, 10]. Values: [10, 13, 7, 7, 6, 5, 18, 3, 1]. It should be [10, 13, 7].
            "expected_output": [10, 13, 7]
        }
    ]

    correct_tests = 0
    for i, test in enumerate(test_cases):
        root_nodes = test["root"]
        target = test["target"]
        k = test["k"]
        expected_output = sorted(test["expected_output"])

        root_bst = build_bst([node for node in root_nodes if node is not None])
        actual_output = sorted(closestKValues(root_bst, target, k))

        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Expected: {expected_output}")
            print(f"  Actual:   {actual_output}")

    print(f"\nCorrect tests: {correct_tests}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()