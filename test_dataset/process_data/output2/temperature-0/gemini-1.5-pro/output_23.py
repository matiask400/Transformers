# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
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
        if l2:
            tail.next = l2

        return dummy.next

def arrayToLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

def linkedListToArray(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


inputs = [ [[1,4,5],[1,3,4],[2,6]], [], [[]] ]
outputs = [ [1,1,2,3,4,4,5,6], [], [] ]

# Test the function
for i in range(len(inputs)):
    linked_lists = [arrayToLinkedList(arr) for arr in inputs[i]]
    merged_list = Solution().mergeKLists(linked_lists)
    output = linkedListToArray(merged_list)
    print(output == outputs[i])
