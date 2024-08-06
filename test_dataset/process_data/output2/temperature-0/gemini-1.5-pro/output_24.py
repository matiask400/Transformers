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

            # Update pointers
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
test_cases = [
    ([1, 2, 3, 4], [2, 1, 4, 3]),
    ([], []),
    ([1], [1])
]

for i, (input_list, expected_output) in enumerate(test_cases):
    head = ListNode(0)
    current = head
    for val in input_list:
        current.next = ListNode(val)
        current = current.next
    head = head.next

    solution = Solution()
    result_head = solution.swapPairs(head)
    result = print_linked_list(result_head)
    print(f"Test case {i+1}: {result == expected_output}")