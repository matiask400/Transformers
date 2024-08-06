class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    dummy = ListNode(0, head)
    groupPrev = dummy

    while True:
        kth = getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next

        # Reverse group
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

# Example 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
output1 = reverseKGroup(head1, 2)
print(output1.val, output1.next.val, output1.next.next.val, output1.next.next.next.val, output1.next.next.next.next.val)  # Output: 2 1 4 3 5
print(True)

# Example 2
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)
output2 = reverseKGroup(head2, 3)
print(output2.val, output2.next.val, output2.next.next.val, output2.next.next.next.val, output2.next.next.next.next.val)  # Output: 3 2 1 4 5
print(True)

# Example 3
head3 = ListNode(1)
head3.next = ListNode(2)
head3.next.next = ListNode(3)
head3.next.next.next = ListNode(4)
head3.next.next.next.next = ListNode(5)
output3 = reverseKGroup(head3, 1)
print(output3.val, output3.next.val, output3.next.next.val, output3.next.next.next.val, output3.next.next.next.next.val)  # Output: 1 2 3 4 5
print(True)

# Example 4
head4 = ListNode(1)
output4 = reverseKGroup(head4, 1)
print(output4.val)  # Output: 1
print(True)