class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    dummy = ListNode(0, head)
    prev = dummy
    curr = head
    while curr:
        last = prev
        for i in range(k):
            if not curr:
                break
            curr = curr.next
            last = last.next
        if not curr:
            break
        nxt = last.next
        for i in range(k):
            last.next = curr
            curr = curr.next
            last = last.next
        last.next = nxt
        prev = nxt
    return dummy.next

# Example 1: Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
k1 = 2
output1 = reverseKGroup(head1, k1)
print(output1.val == 2 and output1.next.val == 1 and output1.next.next.val == 4 and output1.next.next.next.val == 3 and output1.next.next.next.next.val == 5)

# Example 2: Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)
k2 = 3
output2 = reverseKGroup(head2, k2)
print(output2.val == 3 and output2.next.val == 2 and output2.next.next.val == 1 and output2.next.next.next.val == 4 and output2.next.next.next.next.val == 5)

# Example 3: Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]
head3 = ListNode(1)
head3.next = ListNode(2)
head3.next.next = ListNode(3)
head3.next.next.next = ListNode(4)
head3.next.next.next.next = ListNode(5)
k3 = 1
output3 = reverseKGroup(head3, k3)
print(output3.val == 1 and output3.next.val == 2 and output3.next.next.val == 3 and output3.next.next.next.val == 4 and output3.next.next.next.next.val == 5)

# Example 4: Input: head = [1], k = 1
# Output: [1]
head4 = ListNode(1)
k4 = 1
output4 = reverseKGroup(head4, k4)
print(output4.val == 1)