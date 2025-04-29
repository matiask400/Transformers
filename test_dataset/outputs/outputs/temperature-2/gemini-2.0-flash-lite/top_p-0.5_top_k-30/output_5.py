from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merges k sorted linked lists into one sorted linked list.

    Args:
        lists: A list of sorted linked lists.

    Returns:
        The merged sorted linked list.
    """
    all_nodes = []
    for head in lists:
        current = head
        while current:
            all_nodes.append(current.val)
            current = current.next

    all_nodes.sort()

    if not all_nodes:
        return None

    dummy_head = ListNode()
    current = dummy_head
    for val in all_nodes:
        current.next = ListNode(val)
        current = current.next

    return dummy_head.next

def list_to_linked_list(lst):
    """Converts a list to a linked list."""
    dummy_head = ListNode()
    current = dummy_head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

def linked_list_to_list(head):
    """Converts a linked list to a list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def run_tests():
    """Runs the tests and prints the results."""
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1, 2, 3], [4, 5, 6]], [1, 2, 3, 4, 5, 6]),
        ([[1, 2], [3, 4, 5], [6]], [1, 2, 3, 4, 5, 6]),
        ([[1], [2], [3]], [1, 2, 3]),
        ([[5, 6, 7], [1, 2, 3, 4]], [1, 2, 3, 4, 5, 6, 7])
    ]
    correct_tests = 0
    for i, (lists_input, expected_output) in enumerate(test_cases):
        lists_linked_list = []
        for lst in lists_input:
            lists_linked_list.append(list_to_linked_list(lst))
        result_linked_list = mergeKLists(lists_linked_list)
        result_list = linked_list_to_list(result_linked_list)
        if result_list == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
    print(f"Correct tests: {correct_tests}/{len(test_cases)}")

run_tests()