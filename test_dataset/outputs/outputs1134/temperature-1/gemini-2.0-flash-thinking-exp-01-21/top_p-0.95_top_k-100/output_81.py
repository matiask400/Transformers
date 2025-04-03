class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_height(root):
    if not root:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))

def print_binary_tree(root):
    if not root:
        return [[""]]
    height = get_height(root)
    width = 2**height - 1
    res = [[""] * width for _ in range(height)]

    def fill_array(node, r, c):
        if not node or r >= height or c < 0 or c >= width:
            return
        res[r][c] = str(node.val)
        if r + 1 < height:
            offset = 2**(height - r - 2) if height - r - 2 >= 0 else 0
            fill_array(node.left, r + 1, c - offset)
            fill_array(node.right, r + 1, c + offset)

    fill_array(root, 0, (width - 1) // 2)
    return res

def solve():
    test_cases = [
        (TreeNode(1, TreeNode(2)), [["", "1", ""], ["2", "", ""]]),
        (TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3)), [["", "", "", "1", "", "", ""], ["", "2", "", "", "", "3", ""], ["", "", "4", "", "", "", ""]]),
        (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5)), [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""], ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""], ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""], ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]),
        (None, [[""]])
    ]

    correct_tests = 0
    for i, (root, expected_output) in enumerate(test_cases):
        actual_output = print_binary_tree(root)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
            print("Expected:")
            for row in expected_output:
                print(row)
            print("Actual:")
            for row in actual_output:
                print(row)

    print(f"\n{correct_tests}/{len(test_cases)}")

if __name__ == '__main__':
    solve()