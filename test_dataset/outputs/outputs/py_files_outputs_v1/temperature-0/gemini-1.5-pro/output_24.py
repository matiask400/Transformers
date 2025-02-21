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
            # save pointers
            first_node = curr
            second_node = curr.next

            # swapping
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # update pointers
            prev = first_node
            curr = first_node.next
        return dummy.next

def to_linked_list(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    curr = head
    for i in range(1, len(nums)):
        curr.next = ListNode(nums[i])
        curr = curr.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
inputs = [[1,2,3,4], [], [1]]
outputs = [[2,1,4,3], [], [1]]

for i in range(len(inputs)):
    head = to_linked_list(inputs[i])
    result = Solution().swapPairs(head)
    result_list = linked_list_to_list(result)
    print(f'Test case {i+1}: {result_list == outputs[i]}')