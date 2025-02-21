# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
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

            # Update pointers
            prev = curr
            curr = nxtPair
        return dummy.next


def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linked_list_to_list(head):
    lst = []
    curr = head
    while curr:
        lst.append(curr.val)
        curr = curr.next
    return lst

# Test cases
inputs = [[1,2,3,4], [], [1]]
outputs = [[2,1,4,3], [], [1]]

for i in range(len(inputs)):
    head = list_to_linked_list(inputs[i])
    result = Solution().swapPairs(head)
    output = linked_list_to_list(result)
    print(output == outputs[i])