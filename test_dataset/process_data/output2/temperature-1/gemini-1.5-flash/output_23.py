import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    # Create a min-heap to store the heads of all linked lists.
    heap = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

    # Create a dummy head node.
    dummy = ListNode(0)
    tail = dummy

    # While the heap is not empty.
    while heap:
        # Pop the smallest node from the heap.
        _, i, node = heapq.heappop(heap)

        # Add the node to the merged list.
        tail.next = node
        tail = tail.next

        # Add the next node of the popped node to the heap.
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next

# Example 1
lists_1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
output_1 = mergeKLists(lists_1)
print(True if output_1 == [1, 1, 2, 3, 4, 4, 5, 6] else False)

# Example 2
lists_2 = []
output_2 = mergeKLists(lists_2)
print(True if output_2 == [] else False)

# Example 3
lists_3 = [[]]
output_3 = mergeKLists(lists_3)
print(True if output_3 == [] else False)