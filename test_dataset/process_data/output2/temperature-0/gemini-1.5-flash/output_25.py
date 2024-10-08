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
output1 = [2,1,4,3,5]

# Example 2
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k2 = 3
output2 = [3,2,1,4,5]

# Example 3
head3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k3 = 1
output3 = [1,2,3,4,5]

# Example 4
head4 = ListNode(1)
k4 = 1
output4 = [1]

print(reverseKGroup(head1, k1) == output1)
print(reverseKGroup(head2, k2) == output2)
print(reverseKGroup(head3, k3) == output3)
print(reverseKGroup(head4, k4) == output4)