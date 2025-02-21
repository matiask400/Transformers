class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

# Example usage and verification
def list_to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

solution = Solution()
# Example 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n1 = 2
output1 = list_to_array(solution.removeNthFromEnd(head1, n1))
print(output1 == [1, 2, 3, 5])  # Expected: True

# Example 2
head2 = ListNode(1)
n2 = 1
output2 = list_to_array(solution.removeNthFromEnd(head2, n2))
print(output2 == [])  # Expected: True

# Example 3
head3 = ListNode(1, ListNode(2))
n3 = 1
output3 = list_to_array(solution.removeNthFromEnd(head3, n3))
print(output3 == [1])  # Expected: True