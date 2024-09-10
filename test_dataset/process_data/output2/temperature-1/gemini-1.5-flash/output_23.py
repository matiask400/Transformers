class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    # Use a min-heap to store the heads of each list
    import heapq
    heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(heap)

    dummy = ListNode()
    tail = dummy

    while heap:
        val, list_index, node = heapq.heappop(heap)

        # Connect the current node to the tail of the merged list
        tail.next = node
        tail = tail.next

        # Add the next node from the same list to the heap
        if node.next:
            heapq.heappush(heap, (node.next.val, list_index, node.next))

    return dummy.next


# Example 1:
lists_1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
output_1 = mergeKLists([ListNode(val) for val in lists_1[0]], [ListNode(val) for val in lists_1[1]], [ListNode(val) for val in lists_1[2]])
print(True if output_1 == [1, 1, 2, 3, 4, 4, 5, 6] else False)

# Example 2:
lists_2 = []
output_2 = mergeKLists(lists_2)
print(True if output_2 == [] else False)

# Example 3:
lists_3 = [[]]
output_3 = mergeKLists([ListNode() for val in lists_3[0]])
print(True if output_3 == [] else False)