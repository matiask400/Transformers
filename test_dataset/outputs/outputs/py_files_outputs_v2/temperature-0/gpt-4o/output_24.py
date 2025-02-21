class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head
        while curr and curr.next:
            next_pair = curr.next.next
            second = curr.next
            second.next = curr
            curr.next = next_pair
            prev.next = second
            prev = curr
            curr = next_pair
        return dummy.next

def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example 1
input_1 = [1, 2, 3, 4]
expected_output_1 = [2, 1, 4, 3]
head_1 = list_to_linkedlist(input_1)
output_1 = linkedlist_to_list(Solution().swapPairs(head_1))
print(output_1 == expected_output_1)

# Example 2
input_2 = []
expected_output_2 = []
head_2 = list_to_linkedlist(input_2)
output_2 = linkedlist_to_list(Solution().swapPairs(head_2))
print(output_2 == expected_output_2)

# Example 3
input_3 = [1]
expected_output_3 = [1]
head_3 = list_to_linkedlist(input_3)
output_3 = linkedlist_to_list(Solution().swapPairs(head_3))
print(output_3 == expected_output_3)