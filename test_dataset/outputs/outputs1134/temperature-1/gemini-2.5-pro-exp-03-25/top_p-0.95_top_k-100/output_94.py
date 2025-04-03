import collections

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to build a BST from a list (level order traversal with nulls)
def build_tree(list_repr):
    if not list_repr:
        return None
    
    nodes = [(Node(val) if val is not None else None) for val in list_repr]
    kids = collections.deque(nodes[1:])
    root = nodes[0]
    
    nodes_to_process = collections.deque([root])
    
    while kids:
        curr = nodes_to_process.popleft()
        if curr is None: # Should not happen if input is valid level order for a tree
             continue

        # Left child
        if kids:
            left_child = kids.popleft()
            curr.left = left_child
            if left_child:
                nodes_to_process.append(left_child)
        
        # Right child
        if kids:
            right_child = kids.popleft()
            curr.right = right_child
            if right_child:
                nodes_to_process.append(right_child)
                
    return root

# Helper function to convert the resulting CDLL to a list for verification
def list_from_cdll(head):
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

# Helper function to verify the doubly linked list structure (optional but good)
def verify_cdll(head):
    if not head:
        return True
    
    nodes = []
    curr = head
    while True:
        nodes.append(curr)
        # Check basic successor link
        if not curr.right: return False # Must have successor
        # Check predecessor of successor
        if curr.right.left != curr: return False # Successor's predecessor must be current
        
        curr = curr.right
        if curr == head:
            break # Completed a full circle
            
    # Check basic predecessor link of head
    if not head.left: return False # Must have predecessor
    # Check successor of predecessor
    if head.left.right != head: return False # Predecessor's successor must be head
    # Check if the last node found was indeed head's predecessor
    if nodes[-1] != head.left: return False
    
    # Check sorted order
    for i in range(len(nodes) - 1):
        if nodes[i].val >= nodes[i+1].val:
            return False # Not sorted
            
    return True


# --- Core Solution ---
def treeToDoublyList(root: 'Node') -> 'Node':
    """
    Converts a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
    """
    if not root:
        return None

    # Use nonlocal variables to track the head and the previously visited node
    # during the in-order traversal.
    head = None
    prev = None

    def inorder_connect(node):
        nonlocal head, prev
        if not node:
            return

        # Traverse left subtree
        inorder_connect(node.left)

        # Process current node
        if prev is None:
            # This is the first node visited (smallest value), it becomes the head.
            head = node
        else:
            # Link previous node to current node
            prev.right = node
            node.left = prev
        
        # Update prev to the current node for the next iteration
        prev = node

        # Traverse right subtree
        inorder_connect(node.right)

    # Perform the in-order traversal to establish the doubly linked list structure
    inorder_connect(root)

    # After traversal, 'prev' points to the last node visited (largest value),
    # and 'head' points to the first node visited (smallest value).
    # Connect the last node and the first node to make it circular.
    prev.right = head
    head.left = prev

    return head


# --- Test Runner ---
def run_tests():
    test_cases = [
        ([4, 2, 5, 1, 3], [1, 2, 3, 4, 5]),
        ([2, 1, 3], [1, 2, 3]),
        ([], []),
        ([1], [1]),
        ([3, 1, 4, None, 2], [1, 2, 3, 4]), # Test with None
        ([5,3,6,2,4,None,None,1], [1,2,3,4,5,6]), # Deeper tree
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (input_list, expected_list) in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        print(f"Input BST (list): {input_list}")
        root = build_tree(input_list)
        
        # It's helpful to visualize the tree structure (optional)
        # print_tree(root) 
        
        result_head = treeToDoublyList(root)
        result_list = list_from_cdll(result_head)
        
        print(f"Expected CDLL (list): {expected_list}")
        print(f"Actual CDLL (list):   {result_list}")

        # Verify structure and order
        is_correct_struct = verify_cdll(result_head)
        is_correct_values = (result_list == expected_list)
        
        test_passed = is_correct_struct and is_correct_values

        print(f"Test Passed: {test_passed}")
        if test_passed:
            correct_count += 1
        else:
            if not is_correct_struct:
                 print("  Reason: Incorrect CDLL structure (links or circularity)")
            if not is_correct_values:
                 print("  Reason: Incorrect node values or order")
        print("-" * 20)


    print(f"\nSummary: {correct_count}/{total_tests} tests passed.")

# Optional: A simple function to print tree structure (for debugging)
def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level*4) + prefix + str(node.val))
        if node.left is not None or node.right is not None:
            if node.left:
                print_tree(node.left, level + 1, "L--- ")
            else:
                 print(" " * ((level+1)*4) + "L--- None")
            if node.right:
                print_tree(node.right, level + 1, "R--- ")
            else:
                print(" " * ((level+1)*4) + "R--- None")


# Execute the tests
if __name__ == "__main__":
    run_tests()