# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # Save pointers
            nxtPair = curr.next.next
            second = curr.next

            # Reverse this pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second

            # Move forward
            prev = curr
            curr = nxtPair
        
        return dummy.next

def print_linked_list(head):
    current = head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    return values

# Test cases
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
output1 = [2, 1, 4, 3]
print(f"Input 1: {print_linked_list(head1) == [1, 2, 3, 4]}")
head1 = Solution().swapPairs(head1)
print(f"Output 1: {print_linked_list(head1) == output1}")

head2 = None
output2 = []
print(f"Input 2: {print_linked_list(head2) == []}")
head2 = Solution().swapPairs(head2)
print(f"Output 2: {print_linked_list(head2) == output2}")

head3 = ListNode(1)
output3 = [1]
print(f"Input 3: {print_linked_list(head3) == [1]}")
head3 = Solution().swapPairs(head3)
print(f"Output 3: {print_linked_list(head3) == output3}")