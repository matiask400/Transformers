class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeToDoublyList(root):
    if not root:
        return None

    head = None
    prev = None

    def inorder(node):
        nonlocal head, prev
        if not node:
            return

        inorder(node.left)

        if not prev:
            head = node
        else:
            prev.right = node
            node.left = prev
        prev = node

        inorder(node.right)

    inorder(root)

    if head:
        head.left = prev
        prev.right = head

    return head

def bst_from_list(lst):
    if not lst:
        return None
    root = Node(lst[0])
    nodes = [root]
    i = 1
    while i < len(lst):
        node = nodes.pop(0)
        if lst[i] is not None:
            node.left = Node(lst[i])
            nodes.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = Node(lst[i])
            nodes.append(node.right)
        i += 1
    return root

def doubly_list_to_list(head):
    if not head:
        return []
    res = []
    curr = head
    while True:
        res.append(curr.val)
        curr = curr.right
        if curr == head:
            break
    return res

def run_tests():
    tests = [
        ([4,2,5,1,3], [1,2,3,4,5]),
        ([2,1,3], [1,2,3]),
        ([], []),
        ([1], [1]),
        ([5,3,6,2,4,None,None,1], [1,2,3,4,5,6]),
        ([10,5,15,2,7,12,20,1,3,6,8,11,13,18,22], [1,2,3,5,6,7,8,10,11,12,13,15,18,20,22])
    ]
    correct_count = 0
    for i, (input_tree_list, expected_output) in enumerate(tests):
        root = bst_from_list(input_tree_list)
        head = treeToDoublyList(root)
        output_list = doubly_list_to_list(head)
        if output_list == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
    print(f"Correct tests: {correct_count}/{len(tests)}")

if __name__ == '__main__':
    run_tests()