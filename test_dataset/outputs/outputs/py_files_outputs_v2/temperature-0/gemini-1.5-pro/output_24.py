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
            nextPair = curr.next.next
            second = curr.next

            # Reverse this pair
            second.next = curr
            curr.next = nextPair
            prev.next = second

            # Update pointers
            prev = curr
            curr = nextPair

        return dummy.next


def printLinkedList(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
testCases = [
    ([1, 2, 3, 4], [2, 1, 4, 3]),
    ([], []),
    ([1], [1])
]

for i, (input, expectedOutput) in enumerate(testCases):
    head = ListNode(0)
    current = head
    for val in input:
        current.next = ListNode(val)
        current = current.next
    head = head.next

    solution = Solution()
    result = solution.swapPairs(head)
    output = printLinkedList(result)

    print(f"Test case {i+1}: {output == expectedOutput}")