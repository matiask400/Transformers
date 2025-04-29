class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeToDoublyList(root):
    if not root:
        return None

    first = None
    last = None

    def inorder(node):
        nonlocal first, last
        if not node:
            return

        inorder(node.left)

        if last:
            last.right = node
            node.left = last
        else:
            first = node

        last = node

        inorder(node.right)

    inorder(root)

    last.right = first
    first.left = last

    return first

def test_treeToDoublyList():
    def create_bst(arr):
        if not arr:
            return None
        
        arr.sort()
        
        def build_tree(arr):
            if not arr:
                return None
            
            mid = len(arr) // 2
            root = Node(arr[mid])
            root.left = build_tree(arr[:mid])
            root.right = build_tree(arr[mid+1:])
            return root
        
        return build_tree(arr)

    def doubly_list_to_array(head):
        if not head:
            return []
        
        result = []
        current = head
        
        seen = set()
        
        while current and current not in seen:
            result.append(current.val)
            seen.add(current)
            current = current.right
            
        return result

    test_cases = [
        ([4, 2, 5, 1, 3], [1, 2, 3, 4, 5]),
        ([2, 1, 3], [1, 2, 3]),
        ([], []),
        ([1], [1]),
        ([5,3,6,2,4,None,7,1], [1, 2, 3, 4, 5, 6, 7])
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (input_arr, expected_arr) in enumerate(test_cases):
        root = create_bst(input_arr)
        result_head = treeToDoublyList(root)
        result_arr = doubly_list_to_array(result_head)

        if result_arr == expected_arr:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: {input_arr}")
            print(f"  Expected: {expected_arr}")
            print(f"  Got: {result_arr}")

    print(f"\nCorrect: {correct_count}/{total_count}")

test_treeToDoublyList()