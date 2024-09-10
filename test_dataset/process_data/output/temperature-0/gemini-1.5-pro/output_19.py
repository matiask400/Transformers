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

        # Delete the node
        left.next = left.next.next
        return dummy.next


def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

# Test cases
inputs = [([1,2,3,4,5], 2), ([1], 1), ([1,2], 1)]
outputs = [[1,2,3,5], [], [1]]

# Run the code with the provided inputs and compare outputs
for i in range(len(inputs)):
    sol = Solution()
    head = list_to_linked_list(inputs[i][0])
    n = inputs[i][1]
    result = linked_list_to_list(sol.removeNthFromEnd(head, n))
    print(result == outputs[i])