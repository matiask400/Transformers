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
            nxt = curr.next
            tmp = nxt.next

            # swap nodes
            curr.next = tmp
            nxt.next = curr
            prev.next = nxt

            # update pointers
            prev = curr
            curr = tmp

        return dummy.next

# Example inputs and expected outputs
inputs = [[1,2,3,4], [], [1]]
outputs = [[2,1,4,3], [], [1]]

# Test the solution with example inputs
for i in range(len(inputs)):
    # Create linked list from input
    head = ListNode(inputs[i][0]) if inputs[i] else None
    curr = head
    for j in range(1, len(inputs[i])):
        curr.next = ListNode(inputs[i][j])
        curr = curr.next
    
    # Swap nodes in pairs
    sol = Solution()
    result_head = sol.swapPairs(head)

    # Convert result linked list to list for comparison
    result = []
    while result_head:
        result.append(result_head.val)
        result_head = result_head.next

    # Compare output to expected output
    print(result == outputs[i])