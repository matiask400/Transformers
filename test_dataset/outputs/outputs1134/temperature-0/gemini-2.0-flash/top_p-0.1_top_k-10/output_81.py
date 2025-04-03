class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(root):
    def get_height(node):
        if not node:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))

    def fill_array(node, arr, row, left, right):
        if not node:
            return
        mid = (left + right) // 2
        arr[row][mid] = str(node.val)
        fill_array(node.left, arr, row + 1, left, mid - 1)
        fill_array(node.right, arr, row + 1, mid + 1, right)

    height = get_height(root)
    width = 2 ** height - 1
    arr = [[""] * width for _ in range(height)]
    fill_array(root, arr, 0, 0, width - 1)
    return arr

def test_print_tree():
    tests = []
    expected = []

    # Test Case 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    tests.append(root1)
    expected.append([["", "1", ""], ["2", "", ""]])

    # Test Case 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.right = TreeNode(4)
    tests.append(root2)
    expected.append([["", "", "", "1", "", "", ""], ["", "2", "", "", "", "3", ""], ["", "", "4", "", "", "", ""]])

    # Test Case 3
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(5)
    root3.left.left = TreeNode(3)
    root3.left.left.left = TreeNode(4)
    tests.append(root3)
    expected.append([["", "", "", "", "", "", "", "1", "", "", "", "", "", "", ""], ["", "", "", "2", "", "", "", "", "", "", "", "5", "", "", ""], ["", "3", "", "", "", "", "", "", "", "", "", "", "", "", ""], ["4", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]])

    # Test Case 4: Single node
    root4 = TreeNode(1)
    tests.append(root4)
    expected.append([["1"]])

    # Test Case 5: Right skewed tree
    root5 = TreeNode(1)
    root5.right = TreeNode(2)
    root5.right.right = TreeNode(3)
    tests.append(root5)
    expected.append([["", "", "1"], ["", "", "", "", "2"], ["", "", "", "", "", "", "3"]])

    num_tests = len(tests)
    correct_tests = 0

    for i in range(num_tests):
        result = print_tree(tests[i])
        if result == expected[i]:
            print("True")
            correct_tests += 1
        else:
            print("False")
            print("Expected:", expected[i])
            print("Got:", result)

    print(f"{correct_tests}/{num_tests}")

if __name__ == '__main__':
    test_print_tree()