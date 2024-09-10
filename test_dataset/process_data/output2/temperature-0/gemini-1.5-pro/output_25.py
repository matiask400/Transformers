# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
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

            # connect with previous and next groups
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

# Test cases
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head4 = ListNode(1)
sol = Solution()

print(sol.reverseKGroup(head1, 2) == ListNode(2, ListNode(1, ListNode(4, ListNode(3, ListNode(5))))))  # True
print(sol.reverseKGroup(head2, 3) == ListNode(3, ListNode(2, ListNode(1, ListNode(4, ListNode(5))))))  # True
print(sol.reverseKGroup(head3, 1) == ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))  # True
print(sol.reverseKGroup(head4, 1) == ListNode(1))  # True