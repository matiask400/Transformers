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

# Example 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k1 = 2
output1 = reverseKGroup(head1, k1)
print(output1.val, output1.next.val, output1.next.next.val, output1.next.next.next.val, output1.next.next.next.next.val)
print(True)

# Example 2
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k2 = 3
output2 = reverseKGroup(head2, k2)
print(output2.val, output2.next.val, output2.next.next.val, output2.next.next.next.val, output2.next.next.next.next.val)
print(True)

# Example 3
head3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k3 = 1
output3 = reverseKGroup(head3, k3)
print(output3.val, output3.next.val, output3.next.next.val, output3.next.next.next.val, output3.next.next.next.next.val)
print(True)

# Example 4
head4 = ListNode(1)
k4 = 1
output4 = reverseKGroup(head4, k4)
print(output4.val)
print(True)