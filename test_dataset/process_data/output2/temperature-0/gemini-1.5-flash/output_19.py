class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    first = dummy
    second = dummy
    
    # Move `first` pointer `n` steps ahead
    for i in range(n):
        first = first.next
    
    # Move both pointers until `first` reaches the end
    while first.next:
        first = first.next
        second = second.next
    
    # `second` now points to the node before the `nth` node from the end
    second.next = second.next.next
    
    return dummy.next

# Example 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
input1 = head1
output1 = removeNthFromEnd(head1, 2)
print(output1.val, output1.next.val, output1.next.next.val, output1.next.next.next.val)
print(True if output1.val == 1 and output1.next.val == 2 and output1.next.next.val == 3 and output1.next.next.next.val == 5 else False)

# Example 2
head2 = ListNode(1)
input2 = head2
output2 = removeNthFromEnd(head2, 1)
print(output2)
print(True if output2 is None else False)

# Example 3
head3 = ListNode(1, ListNode(2))
input3 = head3
output3 = removeNthFromEnd(head3, 1)
print(output3.val)
print(True if output3.val == 1 else False)