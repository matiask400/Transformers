class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    Merges k sorted linked lists into one sorted linked list.

    Args:
        lists: A list of k sorted linked lists.

    Returns:
        The merged sorted linked list.
    """
    import heapq

    dummy = ListNode()
    curr = dummy
    heap = []

    # Add the first node of each list to the heap
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

    # Iterate through the heap and merge the lists
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next

def test_mergeKLists():
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1, 2, 3], [4, 5, 6]], [1, 2, 3, 4, 5, 6]),
        ([[1, 1, 1], [2, 2, 2], [3, 3, 3]], [1, 1, 1, 2, 2, 2, 3, 3, 3]),
        ([[1, 4, 5], [1, 3, 4], [2, 6], [7, 8, 9]], [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9]),
    ]
    passed = 0
    for input_lists, expected_vals in test_cases:
        input_lists = [
            ListNode() if not l else ListNode()
            for l in input_lists
        ]
        for i, l in enumerate(input_lists):
            curr = l
            for val in input_lists[i]:
                curr.next = ListNode(val)
                curr = curr.next
            input_lists[i] = input_lists[i].next

        result = mergeKLists(input_lists)
        actual_vals = []
        while result:
            actual_vals.append(result.val)
            result = result.next

        print(f"Test case: input_lists = {input_lists}, expected = {expected_vals}, actual = {actual_vals} - {actual_vals == expected_vals}")
        if actual_vals == expected_vals:
            passed += 1
    print(f"Passed {passed} out of {len(test_cases)} tests")

test_mergeKLists()