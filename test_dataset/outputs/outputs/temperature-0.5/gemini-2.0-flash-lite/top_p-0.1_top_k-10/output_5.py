import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: list[ListNode]) -> ListNode:
    """
    Merges k sorted linked lists into one sorted linked list.

    Args:
        lists: A list of sorted linked lists.

    Returns:
        The merged sorted linked list.
    """
    # Use a min-heap to efficiently merge the lists
    heap = []
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))  # (value, list_index, node)

    dummy_head = ListNode()
    current = dummy_head

    while heap:
        val, list_index, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.val, list_index, node.next))

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

def test_merge_k_lists():
    """Tests the mergeKLists function."""
    tests = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1, 2, 3], [], [4, 5, 6]], [1, 2, 3, 4, 5, 6]),
        ([[1], [2], [3]], [1, 2, 3]),
        ([[-1, 5, 10, 11], [0, 2, 6, 12], [1, 3, 7, 13]], [-1, 0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 13])
    ]
    correct_tests = 0
    for lists_input, expected_output in tests:
        lists_of_linked_lists = []
        for lst in lists_input:
            lists_of_linked_lists.append(list_to_linked_list(lst))
        result_linked_list = mergeKLists(lists_of_linked_lists)
        result_list = linked_list_to_list(result_linked_list)
        if result_list == expected_output:
            print(True)
            correct_tests += 1
        else:
            print(False)
    print(f"{correct_tests}/{len(tests)}")

if __name__ == '__main__':
    test_merge_k_lists()