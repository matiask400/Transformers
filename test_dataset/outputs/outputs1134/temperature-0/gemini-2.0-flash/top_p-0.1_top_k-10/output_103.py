import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closestKValues(root, target, k):
    """
    Finds the k values in the BST that are closest to the target.

    Args:
        root: The root of the binary search tree.
        target: The target value.
        k: The number of closest values to return.

    Returns:
        A list of the k values in the BST that are closest to the target.
    """

    heap = []

    def inorder(node):
        if not node:
            return

        inorder(node.left)
        diff = abs(node.val - target)
        if len(heap) < k:
            heapq.heappush(heap, (-diff, node.val))
        elif diff < -heap[0][0]:
            heapq.heappop(heap)
            heapq.heappush(heap, (-diff, node.val))
        inorder(node.right)

    inorder(root)
    result = [val for _, val in heap]
    return result

def test_closestKValues():
    """
    Tests the closestKValues function.
    """

    # Test case 1
    root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
    target1 = 3.714286
    k1 = 2
    expected1 = [4, 3]
    result1 = closestKValues(root1, target1, k1)
    passed1 = sorted(result1) == sorted(expected1)
    print(f"Test Case 1: {passed1}")

    # Test case 2
    root2 = TreeNode(1)
    target2 = 0.000000
    k2 = 1
    expected2 = [1]
    result2 = closestKValues(root2, target2, k2)
    passed2 = sorted(result2) == sorted(expected2)
    print(f"Test Case 2: {passed2}")

    # Test case 3
    root3 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
    target3 = 3
    k3 = 2
    expected3 = [3, 2]
    result3 = closestKValues(root3, target3, k3)
    passed3 = sorted(result3) == sorted(expected3)
    print(f"Test Case 3: {passed3}")

    # Test case 4
    root4 = TreeNode(10, TreeNode(5, TreeNode(2), TreeNode(7)), TreeNode(15, None, TreeNode(20)))
    target4 = 12
    k4 = 3
    expected4 = [10, 15, 7]
    result4 = closestKValues(root4, target4, k4)
    passed4 = sorted(result4) == sorted(expected4)
    print(f"Test Case 4: {passed4}")

    # Test case 5
    root5 = TreeNode(1)
    target5 = 1
    k5 = 1
    expected5 = [1]
    result5 = closestKValues(root5, target5, k5)
    passed5 = sorted(result5) == sorted(expected5)
    print(f"Test Case 5: {passed5}")

    num_correct = sum([passed1, passed2, passed3, passed4, passed5])
    total_tests = 5
    print(f"\nCorrect tests: {num_correct}/{total_tests}")

if __name__ == "__main__":
    test_closestKValues()