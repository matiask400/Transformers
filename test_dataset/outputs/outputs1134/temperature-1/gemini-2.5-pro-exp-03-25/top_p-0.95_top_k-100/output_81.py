import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        """
        Prints a binary tree into an m*n 2D string array based on specified rules.
        """

        # 1. Calculate the height of the tree
        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            # Note: Height definition here seems to be number of levels (root is level 1)
            # rather than number of edges from root to deepest leaf.
            # The problem statement implies m = height, and examples match this.
            # LeetCode definition of height is usually max edges, so height = levels - 1.
            # Let's stick to the problem's apparent definition: number of levels.
            return 1 + max(get_height(node.left), get_height(node.right))

        height = get_height(root)
        if height == 0:
            return []

        # 2. Calculate the width of the matrix
        # Width n = 2^height - 1
        m = height
        n = (1 << height) - 1 # Equivalent to 2**height - 1

        # 3. Initialize the m*n matrix with empty strings
        res = [["" for _ in range(n)] for _ in range(m)]

        # 4. Recursive function to fill the matrix
        def fill(node: Optional[TreeNode], r: int, c_left: int, c_right: int):
            if not node:
                return

            # Calculate the middle column index for the current node
            c_mid = (c_left + c_right) // 2

            # Place the node's value (as string) in the matrix
            res[r][c_mid] = str(node.val)

            # Recursively fill for the left and right subtrees
            # Left child goes to row r+1, in the middle of columns [c_left, c_mid - 1]
            fill(node.left, r + 1, c_left, c_mid - 1)
            # Right child goes to row r+1, in the middle of columns [c_mid + 1, c_right]
            fill(node.right, r + 1, c_mid + 1, c_right)

        # 5. Start the filling process from the root
        # Root is at row 0, spanning the full column width [0, n-1]
        fill(root, 0, 0, n - 1)

        return res

# Helper function to build a binary tree from a list (level order traversal with None for nulls)
def build_tree_from_list(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    
    val = nodes[0]
    if val is None: # Should not happen for root if list is not empty, but good practice
        return None
        
    root = TreeNode(val)
    queue = collections.deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()
        
        # Process left child
        if i < len(nodes):
            left_val = nodes[i]
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
            i += 1
        
        # Process right child
        if i < len(nodes):
            right_val = nodes[i]
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
            i += 1
            
    return root

# --- Test Runner ---
def run_tests():
    solver = Solution()
    tests = [
        # Example 1
        {'input_list': [1, 2], 
         'expected': [["", "1", ""], 
                      ["2", "", ""]]},
        # Example 2
        {'input_list': [1, 2, 3, None, 4], 
         'expected': [["", "", "", "1", "", "", ""], 
                      ["", "2", "", "", "", "3", ""], 
                      ["", "", "4", "", "", "", ""]] },
        # Example 3
        {'input_list': [1, 2, 5, 3, None, None, None, 4], 
         'expected': [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""], 
                      ["",  "",  "", "2", "", "", "", "",  "",  "",  "", "5", "", "", ""], 
                      ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""], 
                      ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]},
        # Custom Test: Empty tree
        {'input_list': [], 
         'expected': []},
        # Custom Test: Single node tree
        {'input_list': [1], 
         'expected': [["1"]]},
        # Custom Test: Full binary tree of height 3
        {'input_list': [1, 2, 3, 4, 5, 6, 7], 
         'expected': [["", "", "", "1", "", "", ""], 
                      ["", "2", "", "", "", "3", ""], 
                      ["4", "5", "6", "7", "", "", ""]]}, # Note: BFS order doesn't fill like this, fixed expected
         'expected': [["", "", "", "1", "", "", ""],
                      ["", "2", "", "", "", "3", ""],
                      ["4", "5", "6", "7"]]}, # Corrected based on structure
        # Custom Test: Skewed tree (right)
        {'input_list': [1, None, 2, None, None, None, 3], 
         'expected': [["", "", "", "1", "", "", ""], 
                      ["", "", "", "", "", "2", ""], 
                      ["", "", "", "", "", "", "3"]]},
         # Custom Test: Skewed tree (left)
        {'input_list': [1, 2, None, 3, None, 4, None], 
         'expected': [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""], 
                     ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "", "", "", ""], 
                     ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""], 
                     ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]},

    ]

    correct_count = 0
    total_tests = len(tests)

    for i, test in enumerate(tests):
        input_list = test['input_list']
        expected_output = test['expected']
        
        root = build_tree_from_list(input_list)
        actual_output = solver.printTree(root)
        
        passed = actual_output == expected_output
        print(f"{passed}")
        if passed:
            correct_count += 1
        # Optional: print details on failure
        # else:
        #     print(f"Test {i+1} Failed:")
        #     print(f"  Input List: {input_list}")
        #     print(f"  Expected: {expected_output}")
        #     print(f"  Actual:   {actual_output}")


    print(f"\n{correct_count}/{total_tests}") # Final score

# Execute the tests
if __name__ == "__main__":
    run_tests()