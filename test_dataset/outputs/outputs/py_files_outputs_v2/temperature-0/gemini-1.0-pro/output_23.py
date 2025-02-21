import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    for head in lists:
        if head:
            heapq.heappush(heap, (head.val, head))
    dummy = ListNode()
    curr = dummy
    while heap:
        val, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, node.next))
    return dummy.next

# Example 1: Input
lists1 = [ListNode(1), ListNode(4), ListNode(5)]
lists1[0].next = ListNode(4)
lists1[0].next.next = ListNode(5)
lists1[1] = ListNode(1)
lists1[1].next = ListNode(3)
lists1[1].next.next = ListNode(4)
lists1[2] = ListNode(2)
lists1[2].next = ListNode(6)

# Example 1: Output
output1 = mergeKLists(lists1)
print(output1.val == 1 and output1.next.val == 1 and output1.next.next.val == 2 and output1.next.next.next.val == 3 and output1.next.next.next.next.val == 4 and output1.next.next.next.next.next.val == 4 and output1.next.next.next.next.next.next.val == 5 and output1.next.next.next.next.next.next.next.val == 6)

# Example 2: Input
lists2 = []

# Example 2: Output
output2 = mergeKLists(lists2)
print(output2 == None)

# Example 3: Input
lists3 = [[]]

# Example 3: Output
output3 = mergeKLists(lists3)
print(output3 == None)