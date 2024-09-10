class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    first = dummy
    second = dummy
    
    for i in range(n):
        first = first.next
    
    while first.next:
        first = first.next
        second = second.next
    
    second.next = second.next.next
    
    return dummy.next

# Example 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
input1 = head1
output1 = removeNthFromEnd(head1, 2)
print(output1 == ListNode(1, ListNode(2, ListNode(3, ListNode(5))))) # True

# Example 2
head2 = ListNode(1)
input2 = head2
output2 = removeNthFromEnd(head2, 1)
print(output2 == None) # True

# Example 3
head3 = ListNode(1, ListNode(2))
input3 = head3
output3 = removeNthFromEnd(head3, 1)
print(output3 == ListNode(1)) # True