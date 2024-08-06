# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next

def printLinkedList(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Example usage and verification
lists1 = [[1,4,5],[1,3,4],[2,6]]
lists2 = []
lists3 = [[]]

solution = Solution()

# Test Case 1
output1 = solution.mergeKLists(createLinkedList(lists1))
print(printLinkedList(output1) == [1,1,2,3,4,4,5,6])

# Test Case 2
output2 = solution.mergeKLists(createLinkedList(lists2))
print(printLinkedList(output2) == [])

# Test Case 3
output3 = solution.mergeKLists(createLinkedList(lists3))
print(printLinkedList(output3) == [])