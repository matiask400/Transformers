class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            first.next = second.next
            second.next = first
            current.next = second

            current = first

        return dummy.next

def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
inputs = [
    [1, 2, 3, 4],
    [],
    [1]
]

outputs = [
    [2, 1, 4, 3],
    [],
    [1]
]

solution = Solution()
for i, input_list in enumerate(inputs):
    ll = list_to_linkedlist(input_list)
    swapped = solution.swapPairs(ll)
    output_list = linkedlist_to_list(swapped)
    print(output_list == outputs[i])
