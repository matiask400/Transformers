import collections
import sys
# Setting higher recursion depth for deep trees, although BFS avoids deep recursion.
# sys.setrecursionlimit(2000) 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def distanceK(root: TreeNode, target: TreeNode, K: int) -> list[int]:
    """
    Finds all nodes at distance K from the target node in a binary tree.

    Args:
        root: The root node of the binary tree.
        target: The target node from which to measure distance.
        K: The target distance.

    Returns:
        A list of values of nodes at distance K from the target node.
    """
    if not root:
        return []

    # 1. Build an undirected graph representation (adjacency list) from the tree.
    #    We use node values as keys since they are unique and hashable.
    graph = collections.defaultdict(list)
    queue_build = collections.deque([root])
    
    # Use BFS to traverse the tree and build the graph
    while queue_build:
        node = queue_build.popleft()
        if node.left:
            graph[node.val].append(node.left.val)
            graph[node.left.val].append(node.val)
            queue_build.append(node.left)
        if node.right:
            graph[node.val].append(node.right.val)
            graph[node.right.val].append(node.val)
            queue_build.append(node.right)

    # 2. Perform BFS starting from the target node to find nodes at distance K.
    result = []
    # Queue stores tuples of (node_value, distance_from_target)
    queue_bfs = collections.deque([(target.val, 0)]) 
    # Keep track of visited nodes to avoid cycles and redundant work
    visited = {target.val}

    while queue_bfs:
        curr_val, distance = queue_bfs.popleft()

        # If we found a node at the exact distance K, add it to the result.
        if distance == K:
            result.append(curr_val)
            # Optimization: No need to explore further from this node if we only need distance K
            # If we needed nodes *up to* distance K, we wouldn't continue here.
            continue 
        
        # If the current distance is less than K, explore neighbors.
        # (The check `distance == K` above implicitly handles `distance > K` 
        # by not exploring further from nodes already at distance K)
        # We could add an explicit `if distance > K: continue` but it's not strictly necessary.
        
        # Explore neighbors in the graph
        for neighbor_val in graph[curr_val]:
            if neighbor_val not in visited:
                visited.add(neighbor_val)
                queue_bfs.append((neighbor_val, distance + 1))

    return result

# --- Helper function to build tree from list (Level Order) ---
def build_tree(nodes: list) -> TreeNode:
    """Builds a binary tree from a list representation (level order)."""
    if not nodes:
        return None
    
    val_iter = iter(nodes)
    root_val = next(val_iter)
    if root_val is None:
        return None
        
    root = TreeNode(root_val)
    q = collections.deque([root])
    
    while q:
        node = q.popleft()
        try:
            left_val = next(val_iter)
            if left_val is not None:
                node.left = TreeNode(left_val)
                q.append(node.left)
            
            right_val = next(val_iter)
            if right_val is not None:
                node.right = TreeNode(right_val)
                q.append(node.right)
        except StopIteration:
            break
            
    return root

# --- Helper function to find target node by value ---
def find_node(root: TreeNode, target_val: int) -> TreeNode:
    """Finds a node with the given value in the tree."""
    if not root:
        return None
    if root.val == target_val:
        return root
    
    # Search recursively
    found_left = find_node(root.left, target_val)
    if found_left:
        return found_left
    return find_node(root.right, target_val)

# --- Test Harness ---
def run_tests():
    """Runs predefined test cases against the distanceK function."""
    tests = [
        # Example 1
        {'input': {'tree_list': [3,5,1,6,2,0,8,None,None,7,4], 'target_val': 5, 'K': 2}, 'expected': [7,4,1]},
        # K = 0
        {'input': {'tree_list': [1], 'target_val': 1, 'K': 0}, 'expected': [1]},
        # K = 1, Simple tree
        {'input': {'tree_list': [0,1,None,3,2], 'target_val': 1, 'K': 1}, 'expected': [0,3,2]},
         # Target is root, K=1
        {'input': {'tree_list': [3,5,1,6,2,0,8,None,None,7,4], 'target_val': 3, 'K': 1}, 'expected': [5,1]},
        # Target is root, K=2
        {'input': {'tree_list': [3,5,1,6,2,0,8,None,None,7,4], 'target_val': 3, 'K': 2}, 'expected': [6,2,0,8]},
        # Target is root, K=3
        {'input': {'tree_list': [3,5,1,6,2,0,8,None,None,7,4], 'target_val': 3, 'K': 3}, 'expected': [7,4]},
        # Target is leaf, K=3
        {'input': {'tree_list': [3,5,1,6,2,0,8,None,None,7,4], 'target_val': 7, 'K': 3}, 'expected': [1,6]},
        # Linear tree (right skewed)
        {'input': {'tree_list': [0,None,1,None,2,None,3], 'target_val': 3, 'K': 3}, 'expected': [0]},
         # Linear tree (right skewed), target in middle
        {'input': {'tree_list': [0,None,1,None,2,None,3], 'target_val': 1, 'K': 1}, 'expected': [0,2]},
        # Larger K, more complex tree
        {'input': {'tree_list': [0,1,2,3,4,5,6,None,None,7,8], 'target_val': 3, 'K': 3}, 'expected': [5,6,8]},
        # Empty tree list (should result in empty output)
        {'input': {'tree_list': [], 'target_val': 5, 'K': 2}, 'expected': []},
        # Single node tree, K > 0
        {'input': {'tree_list': [1], 'target_val': 1, 'K': 1}, 'expected': []},
        # Target not reachable within K steps
         {'input': {'tree_list': [3,5,1,6,2,0,8,None,None,7,4], 'target_val': 6, 'K': 4}, 'expected': [1]},
         {'input': {'tree_list': [3,5,1,6,2,0,8,None,None,7,4], 'target_val': 0, 'K': 1}, 'expected': [1]},
         {'input': {'tree_list': [3,5,1,6,2,0,8,None,None,7,4], 'target_val': 0, 'K': 2}, 'expected': [8,3]},
    ]

    correct_count = 0
    total_count = len(tests)

    for i, test in enumerate(tests):
        tree_list = test['input']['tree_list']
        target_val = test['input']['target_val']
        k = test['input']['K']
        expected = test['expected']
        
        root = build_tree(tree_list)
        
        # Handle cases where the tree is empty or target doesn't exist
        target_node = None
        if root:
             target_node = find_node(root, target_val)
        
        # If target node is required but not found (and tree isn't empty), result should be empty
        # Or if the tree itself is empty
        if not root or (root and not target_node and tree_list): 
             # Special case: if tree_list is empty, target_node will be None, 
             # and distanceK should return [], which might match expected=[]
             if not tree_list:
                 result = distanceK(None, None, k) # Call with None root/target
             else:
                 # Target value exists, but node not found (shouldn't happen with valid inputs)
                 # Or root exists but target_val isn't in it.
                 # The problem statement guarantees target is in the tree if tree is non-empty.
                 # We'll assume valid inputs per problem statement, but handle empty tree case.
                 # If target_node is None because root is None, distanceK handles it.
                 # If target_node is None because target_val not in non-empty tree, 
                 # this indicates a test setup issue or violation of problem constraints.
                 # For robustness, let's proceed assuming distanceK handles None target gracefully if needed.
                 # However, the problem guarantees target is a node in the tree.
                 # So, if target_node is None and root is not None, it's an issue.
                 # Let's call distanceK anyway, it should handle None target if it occurs.
                 # A better check might be needed if constraints were looser.
                 # Given constraints, we only need to find the node if root exists.
                 if not target_node and root:
                     print(f"Test {i+1} Warning: Target node {target_val} not found in tree, but problem guarantees it exists.")
                     # Proceeding, but result might be unexpected depending on distanceK's robustness
                     # For this problem, we expect target_node to be valid if root is valid.
                     result = [] # Assume empty result if target guaranteed but not found
                 else: # root is None or target found
                     result = distanceK(root, target_node, k)

        else:
             result = distanceK(root, target_node, k)


        # Sort both lists for comparison as order doesn't matter
        result.sort()
        expected.sort()

        # Compare results
        passed = result == expected
        print(f"Test {i+1}: {passed}")
        if not passed:
            print(f"  Input: tree={tree_list}, target={target_val}, K={k}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
        if passed:
            correct_count += 1

    print(f"\nResult: {correct_count} / {total_count} tests passed.")

# Execute the tests
if __name__ == "__main__":
    run_tests()