import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    """
    Represents a node in a binary tree.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Builds a binary tree from a list representation (level-order).
    'None' values in the list represent missing nodes.
    """
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while i < len(nodes):
        current_node = queue.popleft()

        # Process left child
        if i < len(nodes) and nodes[i] is not None:
            left_child = TreeNode(nodes[i])
            current_node.left = left_child
            queue.append(left_child)
        i += 1

        # Process right child
        if i < len(nodes) and nodes[i] is not None:
            right_child = TreeNode(nodes[i])
            current_node.right = right_child
            queue.append(right_child)
        i += 1

    return root

class Solution:
    """
    Contains the solution method for validating a BST.
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if the given binary tree is a valid Binary Search Tree (BST).

        Args:
            root: The root node of the binary tree.

        Returns:
            True if the tree is a valid BST, False otherwise.
        """
        
        def _validate(node: Optional[TreeNode], lower_bound: float, upper_bound: float) -> bool:
            """
            Helper function to recursively validate the BST property.

            Args:
                node: The current node being checked.
                lower_bound: The minimum allowed value for this node (exclusive).
                upper_bound: The maximum allowed value for this node (exclusive).

            Returns:
                True if the subtree rooted at 'node' satisfies the BST property
                within the given bounds, False otherwise.
            """
            # An empty tree (or subtree) is a valid BST.
            if not node:
                return True

            # Check if the current node's value is within the allowed bounds.
            if not (lower_bound < node.val < upper_bound):
                return False

            # Recursively check the left and right subtrees with updated bounds.
            # Left child's upper bound becomes the current node's value.
            # Right child's lower bound becomes the current node's value.
            is_left_valid = _validate(node.left, lower_bound, node.val)
            is_right_valid = _validate(node.right, node.val, upper_bound)

            # Both subtrees must be valid BSTs.
            return is_left_valid and is_right_valid

        # Start the validation from the root with infinite bounds.
        return _validate(root, float('-inf'), float('inf'))

# --- Testing ---
def run_tests():
    """
    Runs predefined test cases against the Solution.isValidBST method.
    """
    solution = Solution()
    
    test_cases = [
        # Input: root = [2,1,3] -> Output: true
        {"input": [2, 1, 3], "expected": True},
        
        # Input: root = [5,1,4,null,null,3,6] -> Output: false
        # Explanation: Root is 5, right child is 4. 4 is not > 5.
        {"input": [5, 1, 4, None, None, 3, 6], "expected": False},
        
        # Input: root = [1] -> Output: true
        {"input": [1], "expected": True},

        # Input: root = [] -> Output: true (empty tree is valid)
        {"input": [], "expected": True},

        # Input: root = [5,4,6,null,null,3,7] -> Output: false
        # Explanation: Node 3 is in the right subtree of 5, but 3 < 5.
        {"input": [5, 4, 6, None, None, 3, 7], "expected": False},
        
        # Input: root = [3,1,5,0,2,4,6] -> Output: true
        {"input": [3, 1, 5, 0, 2, 4, 6], "expected": True},

        # Input: root = [Integer Min Value] -> Output: true
        {"input": [-2147483648], "expected": True},
        
        # Input: root = [Integer Max Value] -> Output: true
        {"input": [2147483647], "expected": True},
        
        # Input: root = [Integer Min Value, null, Integer Max Value] -> Output: true
        {"input": [-2147483648, None, 2147483647], "expected": True},

        # Input: root = [0, -1] -> Output: true
        {"input": [0, -1], "expected": True},
        
        # Input: root = [3,null,30,10,null,null,15,null,45] -> Output: false
        # Explanation: Node 10 is in right subtree of 3, 10 > 3. Node 15 is in right subtree of 10, 15 > 10.
        # However, 10 should be less than 30.
        {"input": [3, None, 30, 10, None, None, 15, None, 45], "expected": False},
        
        # Input: root = [1, 1] -> Output: false
        # Explanation: Left child must be strictly less.
        {"input": [1, 1], "expected": False},

        # Input: root = [10, 5, 15, null, null, 6, 20] -> Output: false
        # Explanation: Node 6 is in the right subtree of 10, but 6 is not > 10.
        {"input": [10, 5, 15, None, None, 6, 20], "expected": False},
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test in enumerate(test_cases):
        root_list = test["input"]
        expected_output = test["expected"]
        
        # Build the tree
        root_node = build_tree(root_list)
        
        # Get the actual output
        actual_output = solution.isValidBST(root_node)
        
        # Compare results
        result = actual_output == expected_output
        print(f"Test {i + 1}: {result}")
        if result:
            correct_tests += 1

    print(f"\nResult: {correct_tests} / {total_tests} correct tests.")

# Run the tests when the script is executed
if __name__ == "__main__":
    run_tests()