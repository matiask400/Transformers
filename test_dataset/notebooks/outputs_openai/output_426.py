class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_level_order(data):
    if not data:
        return None
    from collections import deque
    iter_data = iter(data)
    root_val = next(iter_data)
    if root_val is None:
        return None
    root = Node(root_val)
    queue = deque([root])
    while True:
        try:
            current = queue.popleft()
        except IndexError:
            break
        try:
            left_val = next(iter_data)
            if left_val is not None:
                current.left = Node(left_val)
                queue.append(current.left)
            else:
                current.left = None
        except StopIteration:
            break
        try:
            right_val = next(iter_data)
            if right_val is not None:
                current.right = Node(right_val)
                queue.append(current.right)
            else:
                current.right = None
        except StopIteration:
            break
    return root

def tree_to_circular_dll(root):
    if not root:
        return None

    def in_order(node):
        nonlocal first, last
        if node:
            in_order(node.left)
            if last:
                last.right = node
                node.left = last
            else:
                first = node
            last = node
            in_order(node.right)

    first, last = None, None
    in_order(root)
    first.left = last
    last.right = first
    return first

def get_list_from_circular_dll(head):
    if not head:
        return []
    result = []
    current = head
    while True:
        result.append(current.val)
        current = current.right
        if current == head:
            break
    return result

# Define tests as (input, expected_output)
tests = [
    ([4,2,5,1,3], [1,2,3,4,5]),
    ([2,1,3], [1,2,3]),
    ([], []),
    ([1], [1]),
    ([10,5,15,3,7,13,18], [3,5,7,10,13,15,18]),
    ([50,30,70,20,40,60,80,10,25,35,45,55,65,75,85], [10,20,25,30,35,40,45,50,55,60,65,70,75,80,85]),
]

correct = 0
total = len(tests)

for idx, (input_tree, expected) in enumerate(tests):
    root = build_tree_from_level_order(input_tree)
    head = tree_to_circular_dll(root)
    output = get_list_from_circular_dll(head)
    if output == expected:
        print('True')
        correct += 1
    else:
        print('False')

print(f"{correct}/{total}")