class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    
    # Use a min-heap to store the heads of the linked lists
    import heapq
    heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
    heapq.heapify(heap)
    
    dummy = ListNode(0)
    tail = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next

# Example 1
lists_1 = [[1,4,5],[1,3,4],[2,6]]
head_1 = ListNode(1)
head_1.next = ListNode(4)
head_1.next.next = ListNode(5)
head_2 = ListNode(1)
head_2.next = ListNode(3)
head_2.next.next = ListNode(4)
head_3 = ListNode(2)
head_3.next = ListNode(6)
lists_1 = [head_1, head_2, head_3]
output_1 = mergeKLists(lists_1)
print(output_1 == [1,1,2,3,4,4,5,6], "Example 1")

# Example 2
lists_2 = []
output_2 = mergeKLists(lists_2)
print(output_2 == [], "Example 2")

# Example 3
lists_3 = [[]]
output_3 = mergeKLists(lists_3)
print(output_3 == [], "Example 3")