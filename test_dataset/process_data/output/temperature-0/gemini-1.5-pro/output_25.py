# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # connect the reversed group
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


# Test Cases
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    head = None
    tail = None
    for val in arr:
        if head is None:
            head = ListNode(val)
            tail = head
        else:
            tail.next = ListNode(val)
            tail = tail.next
    return head

def compare_linked_lists(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return l1 is None and l2 is None

solution = Solution()

# Input 1
input_head_1 = create_linked_list([1, 2, 3, 4, 5])
input_k_1 = 2
expected_output_1 = create_linked_list([2, 1, 4, 3, 5])
output_1 = solution.reverseKGroup(input_head_1, input_k_1)
print(compare_linked_lists(output_1, expected_output_1))  # True

# Input 2
input_head_2 = create_linked_list([1, 2, 3, 4, 5])
input_k_2 = 3
expected_output_2 = create_linked_list([3, 2, 1, 4, 5])
output_2 = solution.reverseKGroup(input_head_2, input_k_2)
print(compare_linked_lists(output_2, expected_output_2))  # True

# Input 3
input_head_3 = create_linked_list([1, 2, 3, 4, 5])
input_k_3 = 1
expected_output_3 = create_linked_list([1, 2, 3, 4, 5])
output_3 = solution.reverseKGroup(input_head_3, input_k_3)
print(compare_linked_lists(output_3, expected_output_3))  # True