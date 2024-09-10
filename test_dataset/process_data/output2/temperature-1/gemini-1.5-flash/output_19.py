class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy
    
    for _ in range(n + 1):
        fast = fast.next
        
    while fast:
        fast = fast.next
        slow = slow.next
        
    slow.next = slow.next.next
    return dummy.next

# Example 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
output1 = removeNthFromEnd(head1, 2)
print(output1 == ListNode(1, ListNode(2, ListNode(3, ListNode(5)))))  # Output: True

# Example 2
head2 = ListNode(1)
output2 = removeNthFromEnd(head2, 1)
print(output2 == None)  # Output: True

# Example 3
head3 = ListNode(1, ListNode(2))
output3 = removeNthFromEnd(head3, 1)
print(output3 == ListNode(1))  # Output: True
