class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumRootToLeaf(root):
    def dfs(node, current_number):
        if not node:
            return 0

        current_number = (current_number << 1) | node.val

        if not node.left and not node.right:
            return current_number

        return dfs(node.left, current_number) + dfs(node.right, current_number)

    return dfs(root, 0)

def test_sumRootToLeaf():
    test_cases = [
        ([1,0,1,0,1,0,1], 22),
        ([0], 0),
        ([1], 1),
        ([1,1], 3),
        ([1,0],2),
        ([0,1],1),
        ([1,0,0,1,1,0,0,1,1,0,1,0,0,0,0],145)
    ]
    
    correct_count = 0
    total_tests = len(test_cases)
    
    for root_values, expected_output in test_cases:
        root = construct_tree(root_values)
        actual_output = sumRootToLeaf(root)
        
        if actual_output == expected_output:
            print('True')
            correct_count += 1
        else:
            print('False')
            print(f"Input: {root_values}")
            print(f"Expected: {expected_output}, Actual: {actual_output}")
    
    print(f"{correct_count}/{total_tests}")
    
def construct_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
        
    return root
    
test_sumRootToLeaf()