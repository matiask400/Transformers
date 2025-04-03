class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: TreeNode) -> bool:
    def isValidBSTHelper(node, min_val, max_val):
        if not node:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return (isValidBSTHelper(node.left, min_val, node.val) and
                isValidBSTHelper(node.right, node.val, max_val))

    return isValidBSTHelper(root, float('-inf'), float('inf'))

def test_isValidBST():
    test_cases = [
        ([2,1,3], True),
        ([5,1,4,None,None,3,6], False),
        ([1,1], False),
        ([1,None,2,2],False),
        ([0,None,-1], False),
        ([5,4,6,None,None,3,7], False),
        ([3,1,5,0,2,4,6], True),
        ([2,2,2], False)
    ]

    def build_tree(arr, index=0):
        if index >= len(arr) or arr[index] is None:
            return None
        
        node = TreeNode(arr[index])
        node.left = build_tree(arr, 2 * index + 1)
        node.right = build_tree(arr, 2 * index + 2)
        return node
    
    num_correct = 0
    total_tests = len(test_cases)

    for arr, expected_output in test_cases:
        root = build_tree(arr)
        actual_output = isValidBST(root)

        if actual_output == expected_output:
            print("True")
            num_correct += 1
        else:
            print("False")
    
    print(f"{num_correct}/{total_tests}")

if __name__ == "__main__":
    test_isValidBST()