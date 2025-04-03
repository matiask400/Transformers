import sys
from collections import deque
import math # Used for float('inf')

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to build a tree from a list (level-order traversal, None indicates missing node)
def build_tree(nodes):
    """Builds a binary tree from a list representation (level-order)."""
    if not nodes:
        return None
    
    it = iter(nodes)
    root_val = next(it)
    if root_val is None:
         return None
         
    root = TreeNode(root_val)
    q = deque([root])
    
    while q:
        curr = q.popleft()
        try:
            left_val = next(it)
            if left_val is not None:
                curr.left = TreeNode(left_val)
                q.append(curr.left)
            
            right_val = next(it)
            if right_val is not None:
                curr.right = TreeNode(right_val)
                q.append(curr.right)
        except StopIteration:
            break # No more nodes in the list
            
    return root

class Solution:
    """
    Finds the minimum absolute difference between values of any two nodes in a BST.
    Uses in-order traversal to leverage the sorted property of BSTs.
    """
    def __init__(self):
        # Initialize minimum difference to positive infinity
        self.min_diff = float('inf')
        # Initialize the value of the previously visited node to None
        self.prev_val = None

    def inorder_traversal(self, node):
        """Performs in-order traversal and updates min_diff."""
        if node is None:
            return

        # Traverse left subtree
        self.inorder_traversal(node.left)

        # Process current node
        if self.prev_val is not None:
            # Calculate difference with the previous node's value
            diff = node.val - self.prev_val
            # Update minimum difference if the current difference is smaller
            self.min_diff = min(self.min_diff, diff)
        
        # Update the previous node's value to the current node's value
        self.prev_val = node.val

        # Traverse right subtree
        self.inorder_traversal(node.right)

    def getMinimumDifference(self, root: TreeNode) -> int:
        """
        Calculates the minimum absolute difference in the BST.
        Resets state variables before starting the traversal.
        """
        # Reset state for potentially multiple calls on the same Solution object
        self.min_diff = float('inf')
        self.prev_val = None
        
        # Start the in-order traversal from the root
        self.inorder_traversal(root)
        
        # Return the minimum difference found
        return self.min_diff

# Function to run tests
def run_tests():
    """Runs test cases against the Solution."""
    solution = Solution() # Instantiate the solution class

    # List of test cases: (input_list_representation, expected_output)
    test_cases = [
        ([1, None, 3, None, None, 2], 1), # Example 1
        ([4, 2, 6, 1, 3], 1),             # Standard BST
        ([5, 1, 48, None, None, 12, 49], 1), # More complex BST
        ([236, 104, 701, None, 227, None, 911], 9), # LeetCode example
        ([0, None, 2236, 1024, 2776, None, None, None, 1280], 52), # Large values
        ([90, 69, None, 49, 89, None, 52], 1), # Another BST structure
        ([543, 384, 652, None, 445, None, 699], 47), # Test case with larger diff
        ([2, 1, 3], 1), # Simple 3-node tree
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (input_list, expected_output) in enumerate(test_cases):
        # Build the tree from the list representation
        root = build_tree(input_list)
        
        # Calculate the actual output using the solution method
        # The Solution object's state is reset inside getMinimumDifference
        actual_output = solution.getMinimumDifference(root)
        
        # Compare actual output with expected output
        passed = actual_output == expected_output
        
        # Print result for each test
        print(f"Test {i+1}: {passed}")
        
        if passed:
            correct_count += 1

    # Print final summary
    print(f"\n{correct_count} / {total_tests} tests passed.")

# Execute the tests when the script is run
if __name__ == '__main__':
    run_tests()