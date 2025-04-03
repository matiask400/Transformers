class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def distanceK(root, target, K):
    """
    Finds all nodes that are a distance K from the target node in a binary tree.

    Args:
        root: The root of the binary tree.
        target: The target node.
        K: The distance from the target node.

    Returns:
        A list of the values of all nodes that have a distance K from the target node.
    """

    def build_graph(node, parent):
        if node:
            graph[node] = []
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
            build_graph(node.left, node)
            build_graph(node.right, node)

    graph = {}
    build_graph(root, None)

    queue = [(target, 0)]
    visited = {target}
    result = []

    while queue:
        node, dist = queue.pop(0)
        if dist == K:
            result.append(node.val)
        if dist > K:
            break
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, dist + 1))
                visited.add(neighbor)

    return result


def test_distanceK():
    """
    Tests the distanceK function with various test cases.
    """
    def construct_tree(nodes):
        if not nodes:
            return None

        def build_tree_helper(index):
            if index >= len(nodes) or nodes[index] is None:
                return None

            node = TreeNode(nodes[index])
            node.left = build_tree_helper(2 * index + 1)
            node.right = build_tree_helper(2 * index + 2)
            return node

        root = build_tree_helper(0)
        return root
    
    def find_node(root, target_val):
        if not root:
            return None
        if root.val == target_val:
            return root
        
        left_search = find_node(root.left, target_val)
        if left_search:
            return left_search
        
        return find_node(root.right, target_val)

    test_cases = [
        (
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
            5,
            2,
            [7, 4, 1],
        ),
        (
            [0, 2, 1, None, None, 3],
            3,
            3,
            [0]
        ),
         (
            [0,1,None,None,2,None,3,None,4],
            2,
            1,
            [1,3]
        ),
        (
            [0,1,None,None,2,None,3,None,4],
            0,
            4,
            [4]
        ),
        (
            [0,1,None,None,2,None,3,None,4],
            0,
            0,
            [0]
        )
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, (tree_data, target_val, k, expected) in enumerate(test_cases):
        root = construct_tree(tree_data)
        target = find_node(root, target_val)
        
        if root and target:
            result = distanceK(root, target, k)
            result.sort()
            expected.sort()
            if result == expected:
                print(f"Test {i+1}: True")
                num_correct += 1
            else:
                print(f"Test {i+1}: False")
        else:
             print(f"Test {i+1}: False")

    print(f"{num_correct}/{total_tests}")


if __name__ == "__main__":
    test_distanceK()