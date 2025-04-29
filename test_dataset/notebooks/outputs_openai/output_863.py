from collections import deque

# Definition for a binary tree node.
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
    n = len(lst)
    while queue and i < n:
        node = queue.popleft()
        if i < n and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < n and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root

def find_target_node(root, target_val):
    if not root:
        return None
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.val == target_val:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None

def distanceK(root, target, K):
    parent = {}
    def dfs(node, par=None):
        if node:
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)
    dfs(root)
    
    queue = deque()
    visited = set()
    queue.append((target, 0))
    visited.add(target)
    result = []
    
    while queue:
        current, dist = queue.popleft()
        if dist == K:
            result.append(current.val)
        elif dist < K:
            for neighbor in [current.left, current.right, parent[current]]:
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
    return result

# Test cases
test_cases = [
    {
        'root': [3,5,1,6,2,0,8,None,None,7,4],
        'target': 5,
        'K': 2,
        'expected': [7,4,1]
    },
    {
        'root': [1],
        'target': 1,
        'K': 3,
        'expected': []
    },
    {
        'root': [1,2,3,4,5,6,7],
        'target': 3,
        'K': 1,
        'expected': [1,6,7]
    },
    {
        'root': [0,1,None,3,2],
        'target': 2,
        'K': 1,
        'expected': [3]
    },
    {
        'root': [1,2,3,4,5,6,7,8,9,10,11],
        'target': 5,
        'K': 3,
        'expected': [8,9,10,11]
    }
]

correct = 0
total = len(test_cases)

for test in test_cases:
    root = build_tree(test['root'])
    target_node = find_target_node(root, test['target'])
    output = distanceK(root, target_node, test['K'])
    expected_set = set(test['expected'])
    output_set = set(output)
    if output_set == expected_set:
        print('True')
        correct +=1
    else:
        print('False')

print(f"{correct}/{total}")