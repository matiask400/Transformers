class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    if not nodes:
        return None

    def helper(index):
        if index >= len(nodes) or nodes[index] is None:
            return None
        node = TreeNode(nodes[index])
        node.left = helper(2 * index + 1)
        node.right = helper(2 * index + 2)
        return node

    return helper(0)

def find_target_node(root, target_val):
    if not root:
        return None
    if root.val == target_val:
        return root
    left_search = find_target_node(root.left, target_val)
    if left_search:
        return left_search
    return find_target_node(root.right, target_val)

def distance_k(root, target, K):
    parent_map = {}
    def build_parent_map(node, parent):
        if not node:
            return
        parent_map[node] = parent
        build_parent_map(node.left, node)
        build_parent_map(node.right, node)
    build_parent_map(root, None)

    queue = [(target, 0)]
    visited = {target}
    result = []

    while queue:
        current_node, distance = queue.pop(0)
        if distance == K:
            result.append(current_node.val)
        if distance > K:
            continue

        neighbors = []
        if current_node.left:
            neighbors.append(current_node.left)
        if current_node.right:
            neighbors.append(current_node.right)
        if parent_map[current_node]:
            neighbors.append(parent_map[current_node])

        for neighbor in neighbors:
            if neighbor and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    return result

def run_tests():
    test_cases = [
        {
            "root": [3,5,1,6,2,0,8,None,None,7,4],
            "target": 5,
            "K": 2,
            "expected_output": [7, 4, 1]
        },
        {
            "root": [0,1,None,None,2,None,3,None,4],
            "target": 2,
            "K": 1,
            "expected_output": [1, 3]
        },
        {
            "root": [0,1,None,None,2,None,3,None,4],
            "target": 0,
            "K": 2,
            "expected_output": [2]
        },
        {
            "root": [0,1,None,None,2,None,3,None,4],
            "target": 4,
            "K": 0,
            "expected_output": [4]
        },
        {
            "root": [0,1,None,None,2,None,3,None,4],
            "target": 0,
            "K": 4,
            "expected_output": [4]
        },
        {
            "root": [0,1,None,None,2,None,3,None,4],
            "target": 0,
            "K": 1,
            "expected_output": [1]
        },
        {
            "root": [1,2,3,4,5,None,None,None,None,6,7],
            "target": 2,
            "K": 2,
            "expected_output": [6, 7, 3]
        },
         {
            "root": [1],
            "target": 1,
            "K": 3,
            "expected_output": []
        },
        {
            "root": [1,2,3],
            "target": 2,
            "K": 1,
            "expected_output": [1, 3]
        },
        {
            "root": [1,2,3,4,5],
            "target": 3,
            "K": 1,
            "expected_output": [1]
        }

    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        root_nodes = test_case["root"]
        target_val = test_case["target"]
        K = test_case["K"]
        expected_output = sorted(test_case["expected_output"])

        root_tree = build_tree(root_nodes)
        target_node = find_target_node(root_tree, target_val)

        if target_node:
            actual_output = sorted(distance_k(root_tree, target_node, K))
        else:
            actual_output = []


        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: root={root_nodes}, target={target_val}, K={K}")
            print(f"  Expected Output: {expected_output}")
            print(f"  Actual Output:   {actual_output}")

    print(f"\nCorrect tests: {correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()