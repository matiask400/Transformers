class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        for _ in range(n + 1):
            first = first.next
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

# Helper function to convert list to linked list
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert linked list to list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
inputs = [([1, 2, 3, 4, 5], 2), ([1], 1), ([1, 2], 1)]
outputs = [[1, 2, 3, 5], [], [1]]

solution = Solution()
for i, (lst, n) in enumerate(inputs):
    head = list_to_linkedlist(lst)
    result = solution.removeNthFromEnd(head, n)
    result_list = linkedlist_to_list(result)
    print(result_list == outputs[i])