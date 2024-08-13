class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0, head)
    groupPrev = dummy
    
    while True:
        kth = getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next
        
        # reverse group
        prev, curr = kth.next, groupPrev.next
        while curr != groupNext:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
    return dummy.next


def getKth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr

# Example inputs and verification
# Example 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
k1 = 2
output1 = reverseKGroup(head1, k1)
print(f'Example 1: {output1.val == 2 and output1.next.val == 1 and output1.next.next.val == 4 and output1.next.next.next.val == 3 and output1.next.next.next.next.val == 5}')

# Example 2
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)
k2 = 3
output2 = reverseKGroup(head2, k2)
print(f'Example 2: {output2.val == 3 and output2.next.val == 2 and output2.next.next.val == 1 and output2.next.next.next.val == 4 and output2.next.next.next.next.val == 5}')

# Example 3
head3 = ListNode(1)
head3.next = ListNode(2)
head3.next.next = ListNode(3)
head3.next.next.next = ListNode(4)
head3.next.next.next.next = ListNode(5)
k3 = 1
output3 = reverseKGroup(head3, k3)
print(f'Example 3: {output3.val == 1 and output3.next.val == 2 and output3.next.next.val == 3 and output3.next.next.next.val == 4 and output3.next.next.next.next.val == 5}')

# Example 4
head4 = ListNode(1)
k4 = 1
output4 = reverseKGroup(head4, k4)
print(f'Example 4: {output4.val == 1}')