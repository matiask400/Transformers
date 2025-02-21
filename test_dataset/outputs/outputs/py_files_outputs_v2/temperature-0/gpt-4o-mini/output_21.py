def mergeTwoLists(l1, l2):
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
    tail.next = l1 or l2
    return dummy.next

# Example inputs
l1_1 = [1, 2, 4]
l2_1 = [1, 3, 4]
output_1 = mergeTwoLists(l1_1, l2_1)
print(output_1 == [1, 1, 2, 3, 4, 4])  # True

l1_2 = []
l2_2 = []
output_2 = mergeTwoLists(l1_2, l2_2)
print(output_2 == [])  # True

l1_3 = []
l2_3 = [0]
output_3 = mergeTwoLists(l1_3, l2_3)
print(output_3 == [0])  # True