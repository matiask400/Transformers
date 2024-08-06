class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
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

# Example 1
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
merged_list = mergeTwoLists(l1, l2)
output_1 = []
while merged_list:
    output_1.append(merged_list.val)
    merged_list = merged_list.next
print(output_1 == [1,1,2,3,4,4])

# Example 2
l1 = None
l2 = None
merged_list = mergeTwoLists(l1, l2)
output_2 = []
while merged_list:
    output_2.append(merged_list.val)
    merged_list = merged_list.next
print(output_2 == [])

# Example 3
l1 = None
l2 = ListNode(0)
merged_list = mergeTwoLists(l1, l2)
output_3 = []
while merged_list:
    output_3.append(merged_list.val)
    merged_list = merged_list.next
print(output_3 == [0])