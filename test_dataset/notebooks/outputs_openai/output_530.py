class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    if not nodes:
        return None
    from collections import deque
    it = iter(nodes)
    root = TreeNode(next(it))
    queue = deque([root])
    while True:
        try:
            current = queue.popleft()
            left_val = next(it)
            if left_val is not None:
                current.left = TreeNode(left_val)
                queue.append(current.left)
            right_val = next(it)
            if right_val is not None:
                current.right = TreeNode(right_val)
                queue.append(current.right)
        except StopIteration:
            break
    return root

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.prev = None
        self.min_diff = float('inf')
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return self.min_diff

tests = [
    # (input list, expected output)
    ([1, None, 3, 2], 1),
    ([4,2,6,1,3],1),
    ([90,69,None,49,89,None,52],1),
    ([1,0,48,None,None,12,49],1),
    ([236,104,701,None,227,None,911],9),
    ([1,3,4,7,10,12,15],1),
    ([1,2],1),
    ([1,None,2,None,3],1),
    ([5,3,8,2,4,7,9],1),
    ([10,5,15,3,7,13,18],2),
]

solution = Solution()
correct = 0
total = len(tests)
for idx, (tree_list, expected) in enumerate(tests):
    root = build_tree(tree_list)
    result = solution.minDiffInBST(root)
    if result == expected:
        print(True)
        correct +=1
    else:
        print(False)
print(f"{correct}/{total}")