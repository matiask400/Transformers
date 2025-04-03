import collections
import sys
# Increase recursion depth limit for deep trees if needed, though BFS avoids deep recursion
# sys.setrecursionlimit(2000) 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Helper function to build a tree from a list (level-order traversal with None for missing nodes)
def list_to_tree(nodes):
    """
    Builds a binary tree from a list representation (level order).
    `None` values in the list indicate empty branches.
    """
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()
        
        # Process left child
        if nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        
        if i >= len(nodes):
            break
            
        # Process right child
        if nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
        
    return root

# Helper function to find a node with a specific value in the tree
def find_target_node(root: TreeNode, target_val: int) -> TreeNode:
    """
    Finds the TreeNode object with the given value using BFS.
    Returns None if not found (though the problem guarantees it exists).
    """
    if not root:
        return None
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node.val == target_val:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None # Should not be reached given problem constraints

class Solution:
    """
    Solves the problem of finding nodes at distance K from a target node in a binary tree.
    """
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> list[int]:
        """
        Finds all nodes exactly K distance away from the target node.

        Args:
            root: The root node of the binary tree.
            target: The target node from which to measure distance.
            K: The target distance.

        Returns:
            A list of values of nodes at distance K from the target.
        """
        if not root or not target:
            return []
        
        # 1. Build parent map using BFS (or DFS) to allow upward traversal
        # Map: child_node -> parent_node
        parent_map = {root: None}
        queue_parents = collections.deque([root])
        
        while queue_parents:
            node = queue_parents.popleft()
            if node.left:
                parent_map[node.left] = node
                queue_parents.append(node.left)
            if node.right:
                parent_map[node.right] = node
                queue_parents.append(node.right)
                
        # 2. Perform BFS starting from the target node to find nodes at distance K
        # Queue stores tuples: (node, distance_from_target)
        queue_bfs = collections.deque([(target, 0)])
        # Keep track of visited nodes to avoid cycles and redundant work
        visited = {target} 
        result = []
        
        while queue_bfs:
            current_node, distance = queue_bfs.popleft()
            
            # If we found a node at the target distance K, add its value
            if distance == K:
                result.append(current_node.val)
                # Optimization: No need to explore further from this node,
                # as its neighbors will be > K distance away.
                continue 

            # If distance > K, stop exploring this path (already too far)
            # This is implicitly handled by the optimization above or 
            # by not adding neighbors if distance >= K, but good to keep in mind.
            # if distance > K: # Not strictly needed with the `distance == K` check/continue
            #    continue

            # Explore neighbors: left child, right child, and parent
            neighbors = []
            if current_node.left:
                neighbors.append(current_node.left)
            if current_node.right:
                neighbors.append(current_node.right)
            
            parent = parent_map.get(current_node) # Use .get() for safety, though root's parent is None
            if parent:
                neighbors.append(parent)
                
            # Add unvisited neighbors to the queue
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue_bfs.append((neighbor, distance + 1))
                    
        return result

# --- Testing Framework ---
def run_tests():
    """
    Runs predefined test cases against the Solution class.
    """
    solver = Solution()
    
    tests = [
        # Example 1
        {
            "root_list": [3,5,1,6,2,0,8,None,None,7,4], 
            "target_val": 5, 
            "K": 2, 
            "expected": [7, 4, 1]
        },
        # K = 0
        {
            "root_list": [1], 
            "target_val": 1, 
            "K": 0, 
            "expected": [1]
        },
        # Target is leaf
        {
            "root_list": [0,1,None,3,2], 
            "target_val": 2, 
            "K": 1, 
            "expected": [1]
        },
        # Target is root
        {
            "root_list": [0,1,2,3,4,5,6], 
            "target_val": 0, 
            "K": 2, 
            "expected": [3, 4, 5, 6] # Corrected expected output
        },
        # Linear tree (right skewed)
        {
             "root_list": [0,None,1,None,2,None,3,None,4], 
             "target_val": 0, 
             "K": 3, 
             "expected": [3]
        },
        # Empty tree
        {
            "root_list": [], 
            "target_val": 5, # Value doesn't matter
            "K": 2, 
            "expected": []
        },
        # K larger than tree height/depth
        {
            "root_list": [3,5,1,6,2,0,8,None,None,7,4], 
            "target_val": 5, 
            "K": 4, 
            "expected": []
        },
        # Another case
        {
            "root_list": [0,2,1,None,None,3],
            "target_val": 3,
            "K": 3,
            "expected": [2]
        },
        # K=1 case
         {
            "root_list": [3,5,1,6,2,0,8,None,None,7,4], 
            "target_val": 5, 
            "K": 1, 
            "expected": [3, 6, 2]
        },
    ]

    correct_count = 0
    total_tests = len(tests)

    for i, test in enumerate(tests):
        root_list = test["root_list"]
        target_val = test["target_val"]
        K = test["K"]
        expected = sorted(test["expected"]) # Sort for consistent comparison

        root = list_to_tree(root_list)
        
        # Handle empty tree case before finding target
        if not root:
             target_node = None
             result = [] # Directly set result for empty tree
        else:
            target_node = find_target_node(root, target_val)
            # Problem guarantees target exists if tree is non-empty
            if target_node is None: 
                 # This case should ideally not happen based on problem constraints
                 print(f"Test {i+1} Skipped: Target node {target_val} not found (unexpected).")
                 result = [] # Or handle as error
                 passed = (result == expected) # Check if expected was []
            else:
                 result_unsorted = solver.distanceK(root, target_node, K)
                 result = sorted(result_unsorted) # Sort output for comparison


        passed = (result == expected)
        print(passed)
        if passed:
            correct_count += 1
        # Optional: Print details on failure
        # else:
        #     print(f"Test {i+1} Failed:")
        #     print(f"  Input root: {test['root_list']}")
        #     print(f"  Input target: {test['target_val']}")
        #     print(f"  Input K: {test['K']}")
        #     print(f"  Output: {result}")
        #     print(f"  Expected: {expected}")
            
    print(f"{correct_count}/{total_tests}")

# Execute the tests
if __name__ == "__main__":
    run_tests()