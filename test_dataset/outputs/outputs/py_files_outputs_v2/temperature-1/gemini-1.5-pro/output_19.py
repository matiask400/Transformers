# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Example 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n1 = 2
output1 = [1, 2, 3, 5]
solution = Solution()
result1 = print_linked_list(solution.removeNthFromEnd(head1, n1))
print(result1 == output1)  # True

# Example 2
head2 = ListNode(1)
n2 = 1
output2 = []
solution = Solution()
result2 = print_linked_list(solution.removeNthFromEnd(head2, n2))
print(result2 == output2)  # True

# Example 3
head3 = ListNode(1, ListNode(2))
n3 = 1
output3 = [1]
solution = Solution()
result3 = print_linked_list(solution.removeNthFromEnd(head3, n3))
print(result3 == output3)  # True