from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists or len(lists) == 0:
        return None

    # Create a dummy node to point to the head of the merged list
    dummy = ListNode()
    curr = dummy

    # Create a heap to store the heads of the linked lists
    import heapq
    heap = []
    for node in lists:
        if node:
            heapq.heappush(heap, (node.val, node))

    # Merge the linked lists until the heap is empty
    while heap:
        # Get the node with the smallest value from the heap
        val, node = heapq.heappop(heap)

        # Add the node to the merged list
        curr.next = node
        curr = curr.next

        # If the node has a next node, add it to the heap
        if node.next:
            heapq.heappush(heap, (node.next.val, node.next))

    # Return the head of the merged list
    return dummy.next