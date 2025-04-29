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

def construct_bst(nodes):
    if not nodes:
        return None
    root = Node(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current_node = queue.pop(0)
        if nodes[i] is not None:
            current_node.left = Node(nodes[i])
            queue.append(current_node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current_node.right = Node(nodes[i])
            queue.append(current_node.right)
        i += 1
    return root

def doubly_list_to_array(head):
    if not head:
        return []
    result = []
    curr = head
    while True:
        result.append(curr.val)
        curr = curr.right
        if curr == head:
            break
    return result

def run_test(input_tree, expected_output):
    root = construct_bst(input_tree)
    head = treeToDoublyList(root)
    output_list = doubly_list_to_array(head)
    return output_list == expected_output

if __name__ == '__main__':
    test_cases = [
        ([4,2,5,1,3], [1,2,3,4,5]),
        ([2,1,3], [1,2,3]),
        ([], []),
        ([1], [1]),
        ([10,5,15,2,8,12,20,1,None,6,9,11,13,18,25], [1, 2, 5, 6, 8, 9, 10, 11, 12, 13, 15, 18, 20, 25]),
        ([5,3,6,2,4,None,7,1,None,None,None,None,8], [1, 2, 3, 4, 5, 6, 7, 8]),
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, (input_tree, expected_output) in enumerate(test_cases):
        if run_test(input_tree, expected_output):
            print(f'Test {i+1}: True')
            correct_tests += 1
        else:
            print(f'Test {i+1}: False')

    print(f'Correct tests: {correct_tests}/{total_tests}')