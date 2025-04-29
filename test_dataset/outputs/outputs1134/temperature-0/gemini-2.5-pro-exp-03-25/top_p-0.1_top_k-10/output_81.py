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
    None values indicate missing nodes.
    """
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while i < len(nodes):
        current_node = queue.popleft()

        # Process left child
        if nodes[i] is not None:
            left_child = TreeNode(nodes[i])
            current_node.left = left_child
            queue.append(left_child)
        i += 1

        if i >= len(nodes):
            break

        # Process right child
        if nodes[i] is not None:
            right_child = TreeNode(nodes[i])
            current_node.right = right_child
            queue.append(right_child)
        i += 1

    return root

class Solution:
    """
    Contains the logic to print the binary tree according to the specified rules.
    """
    def get_height(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the height of the binary tree.
        Height of an empty tree is 0. Height of a single node tree is 1.
        """
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        """
        Generates the 2D string array representation of the binary tree.
        """
        if not root:
            return []

        height = self.get_height(root)
        m = height
        # Column number n = 2^height - 1
        n = (1 << height) - 1 # Equivalent to 2**height - 1

        # Initialize the result array with empty strings
        ans = [["" for _ in range(n)] for _ in range(m)]

        def fill(node: Optional[TreeNode], r: int, c_left: int, c_right: int):
            """
            Recursive helper function to place node values in the result array.
            Places 'node' at row 'r' in the middle of columns 'c_left' to 'c_right'.
            """
            if not node:
                return

            # Calculate the middle column index for the current range
            c_mid = (c_left + c_right) // 2

            # Place the node's value (as string)
            ans[r][c_mid] = str(node.val)

            # Recursively fill for the left and right subtrees
            # Left subtree goes in row r+1, columns c_left to c_mid-1
            fill(node.left, r + 1, c_left, c_mid - 1)
            # Right subtree goes in row r+1, columns c_mid+1 to c_right
            fill(node.right, r + 1, c_mid + 1, c_right)

        # Start the filling process from the root node
        # Root is at row 0, spanning all columns from 0 to n-1
        fill(root, 0, 0, n - 1)

        return ans

# --- Testing Framework ---

def run_tests():
    """
    Runs predefined test cases against the Solution.printTree method.
    """
    solver = Solution()
    test_cases = [
        # Format: (input_list_representation, expected_output_matrix)
        (
            [1, 2],
            [["", "1", ""],
             ["2", "", ""]]
        ),
        (
            [1, 2, 3, None, 4],
            [["", "", "", "1", "", "", ""],
             ["", "2", "", "", "", "3", ""],
             ["", "", "4", "", "", "", ""]]
        ),
        (
            [1, 2, 5, 3, None, None, None, 4],
            [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""],
             ["",  "",  "", "2", "", "", "", "",  "",  "",  "", "5", "", "", ""],
             ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""],
             ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
        ),
        (
            [1],
            [["1"]]
        ),
        (
            [], # Empty tree
            []
        ),
        (
            [1, 2, 3],
             [["", "1", ""],
              ["2", "", "3"]]
        ),
         (
            [5,3,6,2,4,None,7],
            [["", "", "", "5", "", "", ""],
             ["", "3", "", "", "", "6", ""],
             ["2", "", "4", "", "7", "", ""]]
         )

    ]

    correct_count = 0
    print("Running Tests...")
    for i, (input_list, expected) in enumerate(test_cases):
        root = build_tree(input_list)
        result = solver.printTree(root)
        passed = (result == expected)
        print(f"Test {i + 1}: {passed}")
        if not passed:
             print(f"  Input: {input_list}")
             print(f"  Expected: {expected}")
             print(f"  Got: {result}")
        if passed:
            correct_count += 1

    print(f"\n{correct_count} / {len(test_cases)} tests passed.")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()