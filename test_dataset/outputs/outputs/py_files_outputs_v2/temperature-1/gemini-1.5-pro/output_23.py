# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists or lists == [[]]:
            return []

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i] if i < len(lists) else None
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
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

        tail.next = l1 or l2
        return dummy.next

def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
    return head

def areLinkedListsEqual(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return l1 is None and l2 is None

# Example input and output
input1 = [[1,4,5],[1,3,4],[2,6]]
output1 = [1,1,2,3,4,4,5,6]
input2 = []
output2 = []
input3 = [[]]
output3 = []

# Convert to linked lists for testing
input1 = [createLinkedList(l) for l in input1]
output1 = createLinkedList(output1)
input2 = [createLinkedList(l) for l in input2]
output2 = createLinkedList(output2)
input3 = [createLinkedList(l) for l in input3]
output3 = createLinkedList(output3)

solution = Solution()
print(f"Input 1: {areLinkedListsEqual(solution.mergeKLists(input1), output1)}")
print(f"Input 2: {areLinkedListsEqual(solution.mergeKLists(input2), output2)}")
print(f"Input 3: {areLinkedListsEqual(solution.mergeKLists(input3), output3)}")