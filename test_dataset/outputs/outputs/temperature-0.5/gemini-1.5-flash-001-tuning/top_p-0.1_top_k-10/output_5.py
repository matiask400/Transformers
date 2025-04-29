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
        The merged sorted linked list.
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
        ([[1,2,3],[4,5,6]], [1,2,3,4,5,6]),
        ([[1,4,5],[1,3,4],[2,6],[7,8,9]], [1,1,2,3,4,4,5,6,7,8,9]),
    ]
    passed = 0
    for lists_vals, expected_vals in test_cases:
        lists = []
        for list_vals in lists_vals:
            list_node = ListNode()
            curr = list_node
            for val in list_vals:
                curr.next = ListNode(val)
                curr = curr.next
            lists.append(list_node.next)

        result = mergeKLists(lists)
        result_vals = []
        while result:
            result_vals.append(result.val)
            result = result.next

        print(result_vals == expected_vals, end=" ")
        if result_vals == expected_vals:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")

test_mergeKLists()