from typing import Optional, List
import sys
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode'=None, right:'TreeNode'=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        current = queue.pop(0)
        if current:
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
            queue.append(current.left)
            i += 1
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
            queue.append(current.right)
            i += 1
    return root

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root, -math.inf, math.inf)

def run_tests():
    tests = [
        ([2,1,3], True),
        ([5,1,4,None,None,3,6], False),
        ([1], True),
        ([10,5,15,None,None,6,20], False),
        ([2147483647], True),
        ([5,4,6,None,None,3,7], False),
    ]
    solution = Solution()
    correct = 0
    total = len(tests)
    for inp, expected in tests:
        root = build_tree(inp)
        result = solution.isValidBST(root)
        is_correct = result == expected
        print(is_correct)
        if is_correct:
            correct +=1
    print(f"{correct}/{total}")

if __name__ == "__main__":
    run_tests()