class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: list[ListNode]) -> ListNode:
    """
    Merges k sorted linked lists into one sorted linked list.

    Args:
        lists: A list of k sorted linked lists.

    Returns:
        The head of the merged sorted linked list.
    """
    import heapq
    dummy = ListNode()
    curr = dummy
    heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(heap)
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next

def test_mergeKLists():
    test_cases = [
        ([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6]),
        ([], []),
        ([[]], []),
        ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,4,5,6,7,8,9]),
        ([[1,4,5],[1,3,4],[2,6,7,8]], [1,1,2,3,4,4,5,6,7,8]),
    ]
    passed = 0
    for lists_vals, expected_vals in test_cases:
        lists = []
        for vals in lists_vals:
            head = ListNode()
            curr = head
            for val in vals:
                curr.next = ListNode(val)
                curr = curr.next
            lists.append(head.next)

        result = mergeKLists(lists)
        actual_vals = []
        while result:
            actual_vals.append(result.val)
            result = result.next

        print(f"Test: {lists_vals} -> {expected_vals} == {actual_vals} -> {actual_vals == expected_vals}")
        if actual_vals == expected_vals:
            passed += 1
    print(f"Passed {passed} out of {len(test_cases)} tests.")

test_mergeKLists()