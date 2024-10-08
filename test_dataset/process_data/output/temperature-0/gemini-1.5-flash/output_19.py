class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    first = dummy
    second = dummy
    
    # Move first pointer n+1 steps ahead
    for i in range(n + 1):
        first = first.next
    
    # Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next
    
    # Now second points to the node before the nth node from the end
    second.next = second.next.next
    
    return dummy.next

# Example 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
input_1 = head1
output_1 = removeNthFromEnd(head1, 2)

# Example 2
head2 = ListNode(1)
input_2 = head2
output_2 = removeNthFromEnd(head2, 1)

# Example 3
head3 = ListNode(1, ListNode(2))
input_3 = head3
output_3 = removeNthFromEnd(head3, 1)

# Check if the outputs are correct
print(f"Example 1: {output_1 == [1,2,3,5]}")
print(f"Example 2: {output_2 == []}")
print(f"Example 3: {output_3 == [1]}")