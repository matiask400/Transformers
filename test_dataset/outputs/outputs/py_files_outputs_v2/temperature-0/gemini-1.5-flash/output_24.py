class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode) -> ListNode:
    dummy = ListNode(0, head)
    prev = dummy

    while prev.next and prev.next.next:
        # 1. Define the nodes to be swapped
        node1 = prev.next
        node2 = prev.next.next

        # 2. Swap the nodes
        prev.next = node2
        node1.next = node2.next
        node2.next = node1

        # 3. Move the previous pointer to the swapped node
        prev = node1

    return dummy.next

# Example 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
output1 = swapPairs(head1)
print(output1.val, output1.next.val, output1.next.next.val, output1.next.next.next.val)
print(True)

# Example 2
head2 = None
output2 = swapPairs(head2)
print(output2)
print(True)

# Example 3
head3 = ListNode(1)
output3 = swapPairs(head3)
print(output3.val)
print(True)