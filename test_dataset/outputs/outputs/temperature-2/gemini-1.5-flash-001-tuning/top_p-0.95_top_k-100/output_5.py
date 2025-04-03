class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    """
    Merges k sorted linked lists into one sorted linked list.
    """
    import heapq

    dummyHead = ListNode()
    current = dummyHead

    # Use a min heap to track the head nodes of the lists
    heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
    heapq.heapify(heap)

    while heap:
        val, i, node = heapq.heappop(heap)

        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummyHead.next

def test_mergeKLists():
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
    ]

    passed_tests = 0

    for case in test_cases:
        lists = []
        for sublist in case[0]:
            head = ListNode(sublist[0])
            curr = head
            for val in sublist[1:]:
                curr.next = ListNode(val)
                curr = curr.next
            lists.append(head)
        
        expected = ListNode(case[1][0])
        expected_curr = expected
        for val in case[1][1:]:
            expected_curr.next = ListNode(val)
            expected_curr = expected_curr.next

        result = mergeKLists(lists)

        result_list = []
        while result:
            result_list.append(result.val)
            result = result.next

        print(f"True: {result_list == case[1]}")
        if result_list == case[1]:
            passed_tests += 1

    print(f"Passed {passed_tests}/{len(test_cases)} tests")

test_mergeKLists()