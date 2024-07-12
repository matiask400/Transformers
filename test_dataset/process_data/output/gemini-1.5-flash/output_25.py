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


def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    return result

# Example 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
k1 = 2
reversed_head1 = reverseKGroup(head1, k1)
output1 = print_linked_list(reversed_head1)

# Example 2
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)
k2 = 3
reversed_head2 = reverseKGroup(head2, k2)
output2 = print_linked_list(reversed_head2)

# Example 3
head3 = ListNode(1)
head3.next = ListNode(2)
head3.next.next = ListNode(3)
head3.next.next.next = ListNode(4)
head3.next.next.next.next = ListNode(5)
k3 = 1
reversed_head3 = reverseKGroup(head3, k3)
output3 = print_linked_list(reversed_head3)

# Example 4
head4 = ListNode(1)
k4 = 1
reversed_head4 = reverseKGroup(head4, k4)
output4 = print_linked_list(reversed_head4)

# Check if the outputs are correct
result1 = output1 == [2, 1, 4, 3, 5]
result2 = output2 == [3, 2, 1, 4, 5]
result3 = output3 == [1, 2, 3, 4, 5]
result4 = output4 == [1]
