class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(root):
    """
    Prints a binary tree in a 2D string array.

    Args:
        root: The root of the binary tree.

    Returns:
        A list of lists of strings representing the printed tree.
    """

    def get_height(root):
        if not root:
            return 0
        return 1 + max(get_height(root.left), get_height(root.right))

    def get_width(height):
        return 2 ** height - 1

    def fill_array(root, array, row, left, right):
        if not root:
            return

        mid = (left + right) // 2
        array[row][mid] = str(root.val)

        fill_array(root.left, array, row + 1, left, mid - 1)
        fill_array(root.right, array, row + 1, mid + 1, right)

    height = get_height(root)
    width = get_width(height)
    array = [[""] * width for _ in range(height)]

    fill_array(root, array, 0, 0, width - 1)

    return array


def compare_trees(tree1, tree2):
  """
  Compares two trees represented as lists of lists of strings.
  """
  if len(tree1) != len(tree2):
    return False
  for i in range(len(tree1)):
    if len(tree1[i]) != len(tree2[i]):
      return False
    for j in range(len(tree1[i])):
      if tree1[i][j] != tree2[i][j]:
        return False
  return True

def test_print_tree():
    tests = []
    expected = []

    # Test case 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    tests.append(root1)
    expected.append([["", "1", ""], ["2", "", ""]])

    # Test case 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.right = TreeNode(4)
    tests.append(root2)
    expected.append([["", "", "", "1", "", "", ""], ["", "2", "", "", "", "3", ""], ["", "", "4", "", "", "", ""]])

    # Test case 3
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(5)
    root3.left.left = TreeNode(3)
    root3.left.left.left = TreeNode(4)
    tests.append(root3)
    expected.append([["", "", "", "", "", "", "", "1", "", "", "", "", "", "", ""], ["", "", "", "2", "", "", "", "", "", "", "", "5", "", "", ""], ["", "3", "", "", "", "", "", "", "", "", "", "", "", "", ""], ["4", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]])

    # Test case 4: Empty Tree
    tests.append(None)
    expected.append([])
    
    # Test case 5: Single Node
    root5 = TreeNode(1)
    tests.append(root5)
    expected.append([["1"]])

    # Test case 6: Skewed Right
    root6 = TreeNode(1)
    root6.right = TreeNode(2)
    root6.right.right = TreeNode(3)
    tests.append(root6)
    expected.append([["", "", "1"], ["", "", "", "", "2"], ["", "", "", "", "", "", "3"]])

    num_correct = 0
    for i in range(len(tests)):
        result = print_tree(tests[i])
        if compare_trees(result, expected[i]):
            print("True")
            num_correct += 1
        else:
            print("False")
    print(f"{num_correct}/{len(tests)}")

test_print_tree()