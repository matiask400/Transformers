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
l1_example1 = ListNode(1, ListNode(2, ListNode(4)))
l2_example1 = ListNode(1, ListNode(3, ListNode(4)))
merged_list_example1 = mergeTwoLists(l1_example1, l2_example1)
output_example1 = []
while merged_list_example1:
    output_example1.append(merged_list_example1.val)
    merged_list_example1 = merged_list_example1.next

# Example 2
l1_example2 = None
l2_example2 = None
merged_list_example2 = mergeTwoLists(l1_example2, l2_example2)
output_example2 = []
while merged_list_example2:
    output_example2.append(merged_list_example2.val)
    merged_list_example2 = merged_list_example2.next

# Example 3
l1_example3 = None
l2_example3 = ListNode(0)
merged_list_example3 = mergeTwoLists(l1_example3, l2_example3)
output_example3 = []
while merged_list_example3:
    output_example3.append(merged_list_example3.val)
    merged_list_example3 = merged_list_example3.next

# Check if the outputs match
result_example1 = output_example1 == [1, 1, 2, 3, 4, 4]
result_example2 = output_example2 == []
result_example3 = output_example3 == [0]

print(f"Example 1: {result_example1}")
print(f"Example 2: {result_example2}")
print(f"Example 3: {result_example3}")