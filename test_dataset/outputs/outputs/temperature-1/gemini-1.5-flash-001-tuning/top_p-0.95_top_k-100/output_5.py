class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    Merges k sorted linked lists into one sorted linked list.

    Args:
        lists: An array of k sorted linked lists.

    Returns:
        The head of the merged sorted linked list.
    """
    if not lists:
        return None

    import heapq
    heap = []
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))

    dummy = ListNode(0)
    curr = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


def test_mergeKLists():
    """
    Tests the mergeKLists function with various inputs.
    """
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1, 2, 3], [4, 5, 6]], [1, 2, 3, 4, 5, 6]),
        ([[1, 4, 5], [1, 3, 4], [2, 6], [0]], [0, 1, 1, 2, 3, 4, 4, 5, 6]),
        ([[1, 4, 5], [1, 3, 4], [2, 6], [0], [7, 8]], [0, 1, 1, 2, 3, 4, 4, 5, 6, 7, 8]),
    ]
    passed = 0
    for lists, expected_output in test_cases:
        # Convert lists to linked lists
        linked_lists = []
        for sublist in lists:
            if sublist:
                head = ListNode(sublist[0])
                curr = head
                for i in range(1, len(sublist)):
                    curr.next = ListNode(sublist[i])
                    curr = curr.next
                linked_lists.append(head)
            else:
                linked_lists.append(None)
        # Merge the linked lists
        merged_list = mergeKLists(linked_lists)
        # Convert merged linked list to a list for comparison
        merged_list_vals = []
        while merged_list:
            merged_list_vals.append(merged_list.val)
            merged_list = merged_list.next
        print(f'Test: {lists} - {merged_list_vals} == {expected_output} - {merged_list_vals == expected_output}')
        if merged_list_vals == expected_output:
            passed += 1
    print(f'Passed {passed} out of {len(test_cases)} tests.')


test_mergeKLists()