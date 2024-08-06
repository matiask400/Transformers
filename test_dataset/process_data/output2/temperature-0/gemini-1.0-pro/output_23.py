from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None

    # Create a min-heap to store the heads of the linked lists
    import heapq
    heap = []
    for head in lists:
        if head:
            heapq.heappush(heap, (head.val, head))

    # Initialize the dummy head of the merged linked list
    dummy = ListNode()
    curr = dummy

    # Merge the linked lists until the heap is empty
    while heap:
        _, head = heapq.heappop(heap)
        curr.next = head
        curr = curr.next
        if head.next:
            heapq.heappush(heap, (head.next.val, head.next))

    return dummy.next


# Example 1: Input and Output
input1 = [[1,4,5],[1,3,4],[2,6]]
output1 = merge_k_sorted_lists(input1)
print(output1 == [1,1,2,3,4,4,5,6])  # True

# Example 2: Input and Output
input2 = []
output2 = merge_k_sorted_lists(input2)
print(output2 == [])  # True

# Example 3: Input and Output
input3 = [[]]
output3 = merge_k_sorted_lists(input3)
print(output3 == [])  # True