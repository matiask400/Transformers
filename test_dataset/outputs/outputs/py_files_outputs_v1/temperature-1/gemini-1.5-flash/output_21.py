class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
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

# Convert input lists to linked lists
def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for i in range(1, len(lst)):
        current.next = ListNode(lst[i])
        current = current.next
    return head

# Convert linked list to list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
l1_1 = list_to_linked_list([1,2,4])
l2_1 = list_to_linked_list([1,3,4])
merged_1 = mergeTwoLists(l1_1, l2_1)
output_1 = linked_list_to_list(merged_1)

l1_2 = list_to_linked_list([])
l2_2 = list_to_linked_list([])
merged_2 = mergeTwoLists(l1_2, l2_2)
output_2 = linked_list_to_list(merged_2)

l1_3 = list_to_linked_list([])
l2_3 = list_to_linked_list([0])
merged_3 = mergeTwoLists(l1_3, l2_3)
output_3 = linked_list_to_list(merged_3)

print(f"Test 1: {output_1 == [1,1,2,3,4,4]}")
print(f"Test 2: {output_2 == []}")
print(f"Test 3: {output_3 == [0]}")