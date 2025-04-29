class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    """
    Merges k sorted linked lists into one sorted linked list.

    Args:
        lists: A list of k sorted linked lists.

    Returns:
        The head of the merged sorted linked list.
    """
    import heapq

    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))

    dummy = ListNode()
    curr = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next

def linked_list_to_list(head):
    """
    Converts a linked list to a Python list.

    Args:
        head: The head of the linked list.

    Returns:
        A Python list representing the linked list.
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def list_to_linked_list(lst):
    """
    Converts a Python list to a linked list.

    Args:
        lst: The Python list.

    Returns:
        The head of the linked list.
    """
    dummy_head = ListNode(0)
    current = dummy_head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

def test_merge_k_lists():
    """
    Tests the merge_k_lists function.
    """
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1],[2],[3]], [1,2,3])
    ]

    num_passed = 0
    total_tests = len(test_cases)

    for lists_of_lists, expected_list in test_cases:
        linked_lists = []
        for lst in lists_of_lists:
            if lst:
                linked_lists.append(list_to_linked_list(lst))
            else:
                linked_lists.append(None)
        
        result_list = linked_list_to_list(merge_k_lists(linked_lists))

        if result_list == expected_list:
            print("True")
            num_passed += 1
        else:
            print("False")

    print(f"{num_passed}/{total_tests}")


if __name__ == '__main__':
    test_merge_k_lists()