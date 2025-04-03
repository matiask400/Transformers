class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def str2tree(s):
    if not s:
        return None
    
    def parse(s, index):
        if index >= len(s):
            return None, index
        
        sign = 1
        if s[index] == '-':
            sign = -1
            index += 1
            
        num = 0
        while index < len(s) and s[index].isdigit():
            num = num * 10 + int(s[index])
            index += 1
        
        root = TreeNode(sign * num)
        
        if index < len(s) and s[index] == '(':
            index += 1
            root.left, index = parse(s, index)
            if index < len(s) and s[index] == ')':
                index += 1
        
        if index < len(s) and s[index] == '(':
            index += 1
            root.right, index = parse(s, index)
            if index < len(s) and s[index] == ')':
                index += 1
        
        return root, index
    
    root, _ = parse(s, 0)
    return root

def tree_to_list(root):
    res = []
    if not root:
        return res
    
    queue = [root]
    while queue:
        node = queue.pop(0)
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res

def solve():
    test_cases = [
        ("4(2(3)(1))(6(5))", [4,2,6,3,1,5]),
        ("4(2(3)(1))(6(5)(7))", [4,2,6,3,1,5,7]),
        ("-4(2(3)(1))(6(5)(7))", [-4,2,6,3,1,5,7]),
        ("1(2()(4))(3)",[1,2,3,4]),
        ("1", [1]),
        ("", [])
    ]
    
    correct_count = 0
    total_count = len(test_cases)
    
    for i, (s, expected) in enumerate(test_cases):
        root = str2tree(s)
        actual = tree_to_list(root)
        
        if actual == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Test case {i+1} failed:")
            print(f"  Input: {s}")
            print(f"  Expected: {expected}")
            print(f"  Actual: {actual}")
    
    print(f"{correct_count}/{total_count}")

solve()