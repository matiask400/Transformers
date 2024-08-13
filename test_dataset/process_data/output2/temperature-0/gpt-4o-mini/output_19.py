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

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next

# Example inputs
inputs = [([1, 2, 3, 4, 5], 2), ([1], 1), ([1, 2], 1)]
outputs = [[1, 2, 3, 5], [], [1]]

# Testing the solution
solution = Solution()
for (head, n), expected in zip(inputs, outputs):
    # Create linked list from head
    head_node = ListNode(head[0])
    current = head_node
    for value in head[1:]:
        current.next = ListNode(value)
        current = current.next
    result = solution.removeNthFromEnd(head_node, n)
    # Convert result linked list to Python list
    result_list = []
    while result:
        result_list.append(result.val)
        result = result.next
    print(result_list == expected)