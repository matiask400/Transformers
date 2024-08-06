# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        
        for i in range(n):
            fast = fast.next
            
        while fast:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        
        return dummy.next

def print_linked_list(head):
    current = head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    print(values)

# Example usage and verification:
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
result1 = Solution().removeNthFromEnd(head1, 2)
print(result1 == [1, 2, 3, 5])

head2 = ListNode(1)
result2 = Solution().removeNthFromEnd(head2, 1)
print(result2 == [])

head3 = ListNode(1)
head3.next = ListNode(2)
result3 = Solution().removeNthFromEnd(head3, 1)
print(result3 == [1])