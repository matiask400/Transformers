class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    def isValidBSTHelper(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return isValidBSTHelper(node.left, min_val, node.val) and isValidBSTHelper(node.right, node.val, max_val)

    return isValidBSTHelper(root, float('-inf'), float('inf'))

def test_isValidBST():
    test_cases = [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([1, None, 2], True),
        ([3,1,5,0,2,4,6,None,None,None,3], False),
        ([10,5,15,None,None,6,20], False),
        ([1,1], False),
        ([0,None,1], True)
    ]

    def build_tree(arr):
        if not arr:
            return None
        
        nodes = [TreeNode(val) if val is not None else None for val in arr]
        
        for i in range(len(nodes)):
            if nodes[i] is not None:
                left_child_index = 2 * i + 1
                right_child_index = 2 * i + 2
                
                if left_child_index < len(nodes):
                    nodes[i].left = nodes[left_child_index]
                if right_child_index < len(nodes):
                    nodes[i].right = nodes[right_child_index]
        
        return nodes[0]

    correct_count = 0
    total_count = len(test_cases)

    for i, (input_arr, expected_output) in enumerate(test_cases):
        root = build_tree(input_arr)
        actual_output = isValidBST(root)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")

    print(f"{correct_count}/{total_count}")

test_isValidBST()