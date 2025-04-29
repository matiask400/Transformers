class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(lst):
    if not lst:
        return None
    nodes = [None if val is None else TreeNode(val) for val in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

def closest_k_values(root, target, k):
    result = []
    stack = []
    
    # In-order traversal to get sorted values
    def inorder(node):
        if node:
            inorder(node.left)
            stack.append(node.val)
            inorder(node.right)
    
    inorder(root)
    
    # Binary search to find the closest index
    left, right = 0, len(stack) -1
    while left < right:
        mid = left + (right - left) // 2
        if stack[mid] < target:
            left = mid +1
        else:
            right = mid
    # Initialize two pointers
    i, j = left -1, left
    # Find the k closest
    while k >0:
        if i <0:
            result.append(stack[j])
            j +=1
        elif j >= len(stack):
            result.append(stack[i])
            i -=1
        else:
            if abs(stack[i] - target) <= abs(stack[j] - target):
                result.append(stack[i])
                i -=1
            else:
                result.append(stack[j])
                j +=1
        k -=1
    return result

# Test cases
tests = [
    {
        "root": [4,2,5,1,3],
        "target": 3.714286,
        "k": 2,
        "output": [4,3]
    },
    {
        "root": [1],
        "target": 0.0,
        "k": 1,
        "output": [1]
    }
]

correct = 0
total = len(tests)

for test in tests:
    root = build_tree(test["root"])
    target = test["target"]
    k = test["k"]
    expected = sorted(test["output"])
    result = sorted(closest_k_values(root, target, k))
    if result == sorted(expected):
        print(True)
        correct +=1
    else:
        print(False)

print(f"{correct}/{total}")