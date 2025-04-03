from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    iter_vals = iter(values)
    root = TreeNode(next(iter_vals))
    queue = deque([root])
    while True:
        try:
            current = queue.popleft()
            left_val = next(iter_vals)
            if left_val is not None:
                current.left = TreeNode(left_val)
                queue.append(current.left)
            right_val = next(iter_vals)
            if right_val is not None:
                current.right = TreeNode(right_val)
                queue.append(current.right)
        except StopIteration:
            break
    return root

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], current: int) -> int:
            if not node:
                return 0
            current = (current << 1) | node.val
            if not node.left and not node.right:
                return current
            return dfs(node.left, current) + dfs(node.right, current)
        return dfs(root, 0)

def run_tests():
    solution = Solution()
    test_cases = [
        {
            "input": [1,0,1,0,1,0,1],
            "expected": 22
        },
        {
            "input": [0],
            "expected": 0
        },
        {
            "input": [1],
            "expected": 1
        },
        {
            "input": [1,1],
            "expected": 3
        }
    ]
    correct = 0
    total = len(test_cases)
    for test in test_cases:
        tree = build_tree(test["input"])
        output = solution.sumRootToLeaf(tree)
        result = output == test["expected"]
        print(result)
        if result:
            correct += 1
    print(f"{correct}/{total}")

if __name__ == "__main__":
    run_tests()