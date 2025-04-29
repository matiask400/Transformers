from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    while queue and i < len(lst):
        current = queue.popleft()
        if i < len(lst):
            val = lst[i]
            if val is not None:
                current.left = TreeNode(val)
                queue.append(current.left)
            i += 1
        if i < len(lst):
            val = lst[i]
            if val is not None:
                current.right = TreeNode(val)
                queue.append(current.right)
            i += 1
    return root

def serialize_tree(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

def pruneTree(root):
    def containsOne(node):
        if not node:
            return False
        left = containsOne(node.left)
        right = containsOne(node.right)
        if not left:
            node.left = None
        if not right:
            node.right = None
        return node.val == 1 or left or right
    return root if containsOne(root) else None

test_cases = [
    ([1, None, 0, 0, 1], [1, None, 0, None, 1]),
    ([1,0,1,0,0,0,1], [1, None,1, None,1]),
    ([1,1,0,1,1,0,1,0], [1,1,0,1,1,None,1])
]

correct = 0
total = len(test_cases)

for inp, expected in test_cases:
    root = build_tree(inp)
    pruned = pruneTree(root)
    output = serialize_tree(pruned)
    if output == expected:
        print('True')
        correct +=1
    else:
        print('False')

print(f"{correct}/{total}")