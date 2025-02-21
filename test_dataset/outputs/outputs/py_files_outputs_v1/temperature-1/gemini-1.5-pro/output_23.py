# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next

def list_to_linked_list(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head):
    lst = []
    curr = head
    while curr:
        lst.append(curr.val)
        curr = curr.next
    return lst

# Example usage
input1 = [[1,4,5],[1,3,4],[2,6]]
input2 = []
input3 = [[]]

# Convert input lists to linked lists
for i in range(len(input1)):
    input1[i] = list_to_linked_list(input1[i])
input2 = list_to_linked_list(input2)
input3 = list_to_linked_list(input3)

solution = Solution()

output1 = solution.mergeKLists(input1)
output2 = solution.mergeKLists(input2)
output3 = solution.mergeKLists(input3)

# Convert output linked lists to lists
output1 = linked_list_to_list(output1)
output2 = linked_list_to_list(output2)
output3 = linked_list_to_list(output3)

print(output1 == [1,1,2,3,4,4,5,6]) # True
print(output2 == []) # True
print(output3 == []) # True